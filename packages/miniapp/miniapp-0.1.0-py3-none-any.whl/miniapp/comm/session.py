import threading
import time

from miniapp.data.impl import compile_query


class SessionDict(object):
    """
    Simple wrapper for an object that calls a method when anything is changed.  This is used to save session data as
    soon as it is changed.
    """
    def __init__(self, initial=None, writer=None):
        self._writer = writer
        self._values = dict(initial) if initial else {}
        self._modified = {}
        self._lock = threading.RLock()

    def __bool__(self):
        return bool(self._values)

    def __contains__(self, item):
        return item in self._values

    def __getattr__(self, item):
        if item in {"ALL", "_values"}:
            return self._values
        return self._values.get(item)

    def __getitem__(self, item):
        return self._values.get(item)

    def __setattr__(self, key, value):
        if key in {"_writer", "_values", "_modified", "_lock"}:
            super(SessionDict, self).__setattr__(key, value)
            return
        with self._lock:
            if self._values.get(key) == value:
                return
            self._values[key] = value
            self._modified[key] = value
            self._flush()

    def _flush(self):
        if self._writer:
            with self._lock:
                self._values["timestamp"] = self._modified["timestamp"] = time.time()
                v = self._modified
                self._modified = {}
                self._writer(v)


class SessionHandler(object):
    """
    The base interface for persisting session data, and also the default implementation which just stores sessions
    in memory.
    """

    def __init__(self):
        self._sessions = {}

    def load_session(self, session_id):
        """
        Retrieve session data.
        """
        if session_id:
            data = self._sessions.get(session_id, {})
            return data

    def save_session(self, session_id, data):
        """
        Store session data.
        """
        if session_id not in self._sessions:
            self._sessions[session_id] = {"_id": session_id}
        if isinstance(data, SessionDict):
            data = data._values
        self._sessions[session_id].update(data)

    def session_id_exists(self, session_id):
        """
        Test for existence of a session with a given ID.
        """
        return session_id in self._sessions

    def purge_old(self, max_age=None, filter: callable = None, remove: bool = True):
        """
        Delete old sessions, or sessions that match a given filter.
        :param max_age:     Sessions older than this number of seconds will be removed.
        :param filter:      If given, this function is called with the session data and should return False to cause
                            it to be deleted or True to retain it.
        """
        to_remove = set()
        removed = []
        if max_age:
            t_threshold = time.time() - max_age
            for k, v in self._sessions.items():
                if v["timestamp"] < t_threshold:
                    to_remove.add(k)
                    removed.append(v)
        if filter:
            for k, v in self._sessions.items():
                if filter(v) is False:
                    to_remove.add(k)
                    removed.append(v)
        if remove:
            for k in to_remove:
                self._sessions.pop(k, None)
        return removed

    def __iter__(self):
        """
        Iterate sessions.
        """
        return iter(self._sessions.values())

    def query(self, filter_expr: dict = None):
        """
        Search for particular sessions, i.e. by user name, etc..
        """
        filter_fn = compile_query(filter_expr)
        return filter(filter_fn, self._sessions.values())


class DbSessionHandler(SessionHandler):
    def __init__(self, db):
        super(DbSessionHandler, self).__init__()
        self.db = db
        # TODO we should probably use built-in session expiration
        # db.ensure_index(self.COLL_SESSIONS, ["timestamp"], ttl=6*3600)

    def load_session(self, session_id):
        if session_id:
            data = self.db.lookup(self.COLL_SESSIONS, session_id) or {}
            return data

    def save_session(self, session_id, data):
        if isinstance(data, SessionDict):
            data = data._values
        data = dict(data)
        self.db.update(self.COLL_SESSIONS, session_id, {"$set": data}, upsert=True)

    def session_id_exists(self, session_id):
        return bool(self.load_session(session_id))

    def purge_old(self, max_age=None, filter: callable = None, remove: bool = True):
        removed = []
        if max_age not in (None, ""):
            query = {"timestamp": {"$lt": int(time.time()) - int(float(max_age))}}
            removed += list(self.db.query(self.COLL_SESSIONS, query))
            if remove:
                self.db.delete(self.COLL_SESSIONS, query)
        if filter:
            to_remove = set()
            for ssn in self.db.query(self.COLL_SESSIONS):
                if filter(ssn) is False:
                    to_remove.add(ssn["_id"])
                    removed.append(ssn)
            if remove:
                for ssn_id in to_remove:
                    self.db.delete(self.COLL_SESSIONS, ssn_id)
        return removed

    def __iter__(self):
        return iter(self.db.query(self.COLL_SESSIONS))

    def query(self, filter_expr: dict = None):
        return self.db.query(self.COLL_SESSIONS, filter_expr, limit=1000)

    COLL_SESSIONS = "sessions"

