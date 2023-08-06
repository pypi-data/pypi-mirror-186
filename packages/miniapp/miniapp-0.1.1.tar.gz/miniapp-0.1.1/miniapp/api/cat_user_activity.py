"""
Logging & analysis of user activity.
"""
import time
import json
from dslibrary.sql.parser import SqlParserException

from miniapp.api.base import endpoint
from miniapp.api.cat_base import ApiCategoryBaseCRUD
from miniapp.data.const import ROW_ID
from miniapp.data.db_lock import DbLock
from miniapp.data.query_db import query_mini_db
from miniapp.errs import GeneralError
from miniapp.utils.generic_obj import make_object
from miniapp.utils.json_utils import json_safe_value
from miniapp.utils.misc import fast_informal_hash, unobfuscate


class UserActivityBase(ApiCategoryBaseCRUD):
    """
    User activity logging.

    Use 'record()' to record activity.

    Maintenance:
    * Call aggregate_sessions() occasionally to keep the aggregate data ('user sessions') up to date.
    * Call transfer_batch() occasionally to transfer the activity data elsewhere.
    * Call purge_old() occasionally to implement a data retention policy.

    Endpoints are provided for administrators to review the activity.
    """
    def __init__(self, api, time_bin=None, session_table_name=None, collection_name=None, transfer_events=None, log_target=None, source_field_name=None, sequence=0):
        """
        See generate_user_activity_api_category() for parameter details.
        """
        super(UserActivityBase, self).__init__(api, collection_name=collection_name or "user_activity", validator="user_activity_record.json", sequence=sequence)
        self.log_target = log_target or "db"
        self.time_bin = time_bin or 5*60
        self.session_table_name = session_table_name or "user_activity_sessions"
        self.tmp_collection_name = "tmp_" + self._collection_name
        self.bookmark_coll = "tmp_" + self.session_table_name
        self.source_field_name = source_field_name
        if self.log_target == "db" and api.start_up():
            if source_field_name:
                self.api.get_db().ensure_index(self._collection_name, [self.source_field_name])
            # index on user_id, which should be the most usual query
            self.api.get_db().ensure_index(self._collection_name, ["user_id"])
            # this index is used for time range queries and for clean-up
            self.api.get_db().ensure_index(self._collection_name, ["timestamp"])
            # session/burst table
            self.api.get_db().ensure_index(self.session_table_name, ["active"])
            # FIXME consider automated clean-up like so
            # db.ensure_index(self._collection_name, ["timestamp"], ttl=30*86400)
        self._user_cache = api.setup_cache("useractivity_userid", max_size=1000, expiration_time=30*60)
        self.transfer_events = transfer_events
        self._maintenance_lock = DbLock(api.get_db(), "user_activity_maintenance")

    def add_recommended_maintenance(self, task_runner, do_aggregation: bool=True):
        """
        Add background tasks to a TaskRunner instance which will perform periodic maintenance.

        :param do_aggregation:  Whether to build the session data.  You might choose to only do this in the central
                                place where user activity is sent.
        """
        # clean out old user activity data
        task_runner.add_task(self.purge_old, interval=7200, initial_delay=1800, name="purge-old-user-activity", use_thread=True)
        # transfer user activity records upstream
        if self.transfer_events:
            task_runner.add_task(self.transfer_batch, interval=3*60, initial_delay=30, name="send_user_activity_batch", use_thread=True)
        # session aggregation
        if do_aggregation and self.log_target == "db":
            task_runner.add_task(self.aggregate_sessions, interval=60, initial_delay=30, name="user_activity_aggregation", use_thread=True)

    def _log(self, msg, level="INFO"):
        """
        Log messages related to maintenance.
        """
        self.api.log(msg, level=level, caller_detail="USER_ACTIVITY_MAINTENANCE")

    def purge_all_data(self):
        """
        Erase all data.
        """
        self.api.get_db().delete(self._collection_name, {})
        self.api.get_db().delete(self.tmp_collection_name, {})
        self.api.get_db().delete(self.bookmark_coll, {})
        self.api.get_db().delete(self.session_table_name, {})

    def record_activity(self, username: str=None, session_id: str=None, count: int=1, timestamp=None, **kwargs):
        """
        Store a user activity record.  Much information comes from the current user information, i.e.
        self.api.current_username() etc..
        :param username:  Override username, i.e. attribute to a different user.
        :param session_id: Override session ID.
        :param count:   Optionally indicate more than one of the given event occurred.
        :param timestamp: The timestamp can be specified if the event is coming from another source.
        :param kwargs:  Explanation of the activity.  See schema.
        """
        content = kwargs
        username = username or self.api.current_username()
        user_id = self.api.current_user_id()
        if not user_id and username:
            # look it up from username
            user_id = self._lookup_user_id(username)
        record = {
            "timestamp": timestamp or time.time(),
            "user_id": user_id,
            "username": username,
            "session_id": session_id or self.api.current_session_id(),
            **content
        }
        self._validation(None, record)
        event_id = self.id_for_event(**record)
        if self.log_target == "db":
            upd = {"$set": record, "$inc": {"count": count}}
            self.api.get_db().update(self._collection_name, event_id, upd, upsert=True)
            if self.transfer_events:
                self.api.get_db().update(self.tmp_collection_name, event_id, upd, upsert=True)
        elif self.log_target == "logs":
            self.api.log(
                json.dumps(record), level="INFO", caller_detail="USER_ACTIVITY"
            )

    def transfer_batch(self):
        """
        Send accumulated events.

        NOTE: this feature is not yet fork-safe or multi-worker safe.
        """
        if not self.transfer_events:
            return
        with self._maintenance_lock:
            batch = self.pull_queue_batch()
        if not batch:
            return
        # send events to remote system
        self._log(f"sending user activity, batch_size={len(batch)}")
        self.transfer_events(batch)

    def purge_old(self, max_age__raw=30*86400, max_age__sessions=90*86400):
        """
        Delete records older than a given age.
        """
        threshold_raw = time.time() - max_age__raw
        threshold_sessions = time.time() - max_age__sessions
        self.api.get_db().delete(self._collection_name, {"timestamp": {"$lt": threshold_raw}})
        self.api.get_db().delete(self.session_table_name, {"timestamp": {"$lt": threshold_sessions}})

    def aggregate_sessions(self, **kwargs):
        """
        Analyze user activity to determine start/stop times for each distinct burst of user activity.  A user's
        actual session key may last for quite a while but if they are idle for a while we assume a new burst has
        begun.  So, by 'session', here, we mean a contiguous series of actions on the part of the user.

        :param idle_timeout: How long a user is assumed to still be paying attention after the last known action.
        :param assume_lag:   If there are no events, assume there really have been no events for this much time.
        :param padding_after_last_activity:  User attention is a bit longer then the span of time from the first
            to the last event.  Some time is spent looking at results, for instance.
        """
        if self.log_target != "db":
            return
        with self._maintenance_lock:
            self._do_aggregation(**kwargs)

    def _do_aggregation(self, idle_timeout=30*60, assume_lag=15*60, padding_after_last_activity=4*60):
        t0 = time.time()
        db = self.api.get_db()
        saved = db.lookup(self.bookmark_coll, "bookmark")
        # scan records after bookmark
        start_time = saved.get("value") if saved else None
        if start_time:
            start_time += 0.0001
        latest_time = None
        # gather currently active sessions
        in_progress = {}
        for ssn in db.query(self.session_table_name, {"active": True}):
            in_progress[ssn["session_id"]] = ssn
        if start_time:
            sql = f"select * from table where timestamp > {start_time} order by timestamp"
        else:
            sql = f"select * from table order by timestamp"
        n_events = 0
        n_updates = 0
        n_new = 0
        for rec in self._do_query(self._collection_name, sql=sql):
            n_events += 1
            timestamp = rec["timestamp"]
            if not latest_time or timestamp > latest_time:
                latest_time = timestamp
            session_id = rec.get("session_id")
            if not session_id:
                continue
            user_id = rec.get("user_id")
            username = rec.get("username")
            source = rec.get(self.source_field_name)
            action_count = rec.get("count", 1)
            burst = in_progress.get(session_id)
            # no activity for idle_timeout >> mark this burst as no longer active
            if burst and timestamp - burst["end"] <= idle_timeout:
                # log new activity as part of this burst
                db.update(
                    self.session_table_name, burst["_id"],
                    {"$set": {"end": timestamp}, "$inc": {"actions": action_count}}
                )
                n_updates += 1
            else:
                # start new burst
                burst = {
                    "active": True, "start": timestamp, "end": timestamp, "user_id": user_id,
                    "username": username, "session_id": session_id, "actions": action_count,
                }
                if self.source_field_name:
                    burst[self.source_field_name] = source or ''
                burst_id = db.insert(self.session_table_name, burst)
                in_progress[session_id] = {"_id": burst_id, **burst}
                n_new += 1
        # log
        elapsed = time.time() - t0
        self._log(f"aggregating user activity: n_events={n_events}, n_new={n_new}, n_updates={n_updates}, starting_mark={start_time or 0:.2f}, elapsed={elapsed:.3f}")
        # if there are no events we may still need to emit sessions -- assume a 'latest_time'
        if not latest_time:
            if not in_progress:
                return
            latest_time = max(start_time or 0, time.time() - assume_lag)
        # close off every burst whose 'end' time is far enough in the past
        emit_threshold = latest_time - idle_timeout
        for burst in in_progress.values():
            if burst["end"] < emit_threshold:
                db.update(self.session_table_name, burst["_id"], {"active": False, "end": burst["end"] + padding_after_last_activity})
        # update the bookmark
        db.replace(self.bookmark_coll, "bookmark", {"value": latest_time})

    def id_for_event(self, timestamp, **kwargs):
        """
        Generate an ID which will be distinct with respect to event content and time bin.
        """
        time_bin = hex(int(timestamp/self.time_bin))[2:]
        hash = fast_informal_hash(json.dumps(kwargs, sort_keys=True)).replace("-", "")
        return f"{time_bin}-{hash[:24]}"

    def timestamp_for_event(self):
        """
        A truncated timestamp representing the beginning of the current interval.
        """
        t = int(time.time())
        t -= t % self.time_bin
        return t

    def pull_queue_batch(self):
        """
        Grab all events from the queue and reset the queue.
        """
        batch = []
        last_id = ""
        for rec in self.api.get_db().query(self.tmp_collection_name):
            last_id = max(last_id, rec.pop(ROW_ID))
            batch.append(rec)
        if batch:
            self.api.get_db().delete(self.tmp_collection_name, {ROW_ID: {"$lte": last_id}})
        return batch

    def _lookup_user_id(self, username: str):
        """
        Quick look-up of user ID from user name.
        """
        out = self._user_cache.get(username)
        if not out:
            user_cat = self.api.find_category(has_methods=["get_user", "normalize_id"])
            user_id = user_cat.normalize_id(username) or username
            out = self._user_cache[username] = user_id
        return out

    def _do_query(self, coll_name: str, sql: str):
        """
        Low level query method.
        """
        try:
            cols, rows = query_mini_db(sql, self.api.get_db().query, default_collection=coll_name, allowed_collections=[self._collection_name, self.session_table_name])
            cols = list(cols)
            for row in rows:
                yield json_safe_value({col: row[n] for n, col in enumerate(cols) if row[n] is not None})
        # TODO there are surely other exceptions we would want to translate here
        except SqlParserException as err:
            raise GeneralError(code="sql-error", message=err.message, public_details={"sql": sql, "coll_name": coll_name})


def generate_user_activity_api_category(
        api, query_permission, time_bin=None,
        transfer_events=None, sequence=13,
        source_field_name=None,
        log_target=None,
        raw_table_name=None,
        session_table_name=None,
        delete_permission=None
):
    """
    Generate an API category for recording and analyzing user activity.
    :param api:                 API into which this category will go.
    :param query_permission:    Permission required for accessing the recorded data, i.e. some admin-level permission.
    :param time_bin:            Size of time bin, for session aggregation, in seconds.  Default is 5 minutes.
    :param sequence:            Sequence of category within API.
    :param transfer_events:     A method to send batches of events somewhere else.  It will be passed a list of raw
                                session records to send to an external system.  On receiving the events, the 'source'
                                field should be added indicating where they came from (see 'source_field_name').
    :param source_field_name:   Name of field indicating source of external data.  This is used only by a central
                                repository of aggregated data from other systems.
    :param log_target:          'db' to store in database, 'logs' to store as log messages.
    :param raw_table_name:      Name for table to hold raw activity data.
    :param session_table_name:  Name for table to hold aggregated session information.
    :param delete_permission:   Permission required to delete data.
    """
    class UserActivity(UserActivityBase):
        """
        User activity logging.
        """
        DESCRIPTION = "User activity logging."

        def __init__(self, api):
            super(UserActivity, self).__init__(
                api, log_target=log_target, time_bin=time_bin,
                collection_name=raw_table_name, session_table_name=session_table_name,
                transfer_events=transfer_events, source_field_name=source_field_name, sequence=sequence
            )
            # the endpoint to delete all the data is only enabled if the caller provides a specific permission
            #   to enable it, i.e. a high-level admin permission
            if not delete_permission:
                self.disable_endpoint("purge_user_activity")

        @endpoint(["post"], "query", permission_required=query_permission, sequence=1, activity_analysis="*")
        def query_user_activity(self, sql: str):
            """
            Fetch user activity records.  "select * from table order by timestamp desc limit 100" for instance.
            :param sql:    SQL to query.  Fields: user_id, username, session_id, timestamp, source.  Specify 'table'
                    to access the user_activity table, or specify actual collection name (both user activity and user
                    session tables are allowed).
            :return:    results
            """
            sql = unobfuscate(sql)
            results = list(self._do_query(self._collection_name, sql=sql))
            return make_object(results=results)

        @endpoint(["post"], "query_sessions", permission_required=query_permission, sequence=2, activity_analysis="*")
        def query_user_sessions(self, sql: str):
            """
            Fetch user session records.
            :param sql:    SQL to query.  Fields: user_id, username, session_id, timestamp, source.  Specify 'table'
                    to access the (session_table_name) table, or specify actual collection name (both user activity and user
                    session tables are allowed).
            :return:    results
            """
            sql = unobfuscate(sql)
            results = list(self._do_query(self.session_table_name, sql=sql))
            return make_object(results=results)

        @endpoint("delete", "", permission_required=delete_permission, sequence=10, activity_analysis="*")
        def purge_user_activity(self):
            """
            Delete all user activity.
            """
            self.purge_all_data()
            return make_object()

    return UserActivity(api)
