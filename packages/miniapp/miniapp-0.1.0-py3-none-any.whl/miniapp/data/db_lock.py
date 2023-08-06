"""
Database-based lock, for preventing concurrent activity in the database.
"""
import random
import uuid
import time

from miniapp.data.const import ROW_ID


class DbLock(object):
    def __init__(self, db, name: str, timeout: float=15, abandonment_timeout: int=10*60, table_name: str="locks"):
        """
        A database-based lock that prevents concurrent activity.  Note that this is a re-entrant lock.

        :param db:          The database.
        :param name:        Unique name for this lock.
        :param timeout:     How long to wait before considering it a failure.
        :param abandonment_timeout: How long before we consider a lock to be invalid.  Set this longer than you ever
                            expect the locked operation to take.
        :param table_name:  Table where locks are kept.
        """
        self._db = db
        self._name = name
        self._timeout = timeout
        self._abandonment_timeout = abandonment_timeout
        self._table_name = table_name
        self._my_id = str(uuid.uuid4())     # ID for this specific worker
        self._lock_test_interval = 0.05     # polling interval when waiting for lock to clear
        self._conflict_clear_delay = 0.40   # maximum delay when trying to clear conflicts (see code)
        self._conflict_retries = 4          # number of retries when trying to clear conflicts (see code)
        # we count failures to help the recipient of an exception know how serious the problem is
        self._failing_since = None

    def start(self):
        """
        Start holding the lock.
        """
        time_started = time.time()
        retries = self._conflict_retries
        timeout_per_try = self._timeout / retries
        for n_try in range(retries):
            # wait for lock to clear, then set the lock - we give up on timeout
            if not self._wait_for_unlocked(self._timeout - n_try * timeout_per_try):
                break
            self._set_lock()
            # wait long enough to detect locks from another worker that missed our signal
            time.sleep(self._lock_test_interval * 5)
            # if the lock is clear we're done
            #  - we reset the failure count here, each time a lock is successfully obtained
            if not self._lock_state():
                self._failing_since = None
                return
            # the other worker didn't see our signal but they soon will
            #   - both workers will politely withdraw their lock requests and wait
            #   - whoever waits the shortest will get the lock
            self._clear_own_lock()
            time.sleep(random.uniform(self._lock_test_interval, self._conflict_clear_delay))
        # failed
        self._raise_error(operation_started=time_started)

    def stop(self):
        """
        Stop holding the lock.
        """
        self._clear_own_lock()

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def _set_lock(self):
        t_now = time.time()
        rec = {
            "name": self._name,
            "worker": self._my_id,
            "started": t_now,
            "expires": t_now + self._abandonment_timeout
        }
        self._db.insert(self._table_name, rec)

    def _clear_own_lock(self):
        """
        Remove any lock placed by this worker.
        """
        self._db.delete(self._table_name, {"name": self._name, "worker": self._my_id})

    def _wait_for_unlocked(self, how_long: float) -> bool:
        """
        Wait for lock state to clear or detect timeout.

        :returns:   True if lock is available, False if there was a timeout.
        """
        interval = self._lock_test_interval
        for _ in range(0, int(how_long/interval)):
            if not self._lock_state():
                return True
            time.sleep(interval)

    def _raise_error(self, operation_started: float):
        if not self._failing_since:
            self._failing_since = operation_started
        raise DbLockFailure(self._name, time.time() - self._failing_since)

    def _lock_state(self):
        """
        Test the current state of the lock.
        """
        for rec in self._read_lock_records():
            if rec["worker"] == self._my_id:
                # ignore our own lock
                continue
            if rec["expires"] > time.time():
                return True
            # this record appears to be abandoned and should be deleted
            try:
                self._db.delete(self._table_name, rec[ROW_ID])
            except:
                # ignore error, in case another worker already deleted this
                pass
        return False

    def _read_lock_records(self):
        """
        Get the current lock record.
        """
        return list(self._db.query(self._table_name, {"name": self._name}))


class DbLockFailure(Exception):
    """
    Failure to obtain lock.

    Use failure_duration to determine how serious it is.
    """
    def __init__(self, lock_name: str, failure_duration: float):
        super(DbLockFailure, self).__init__(f"database lock '{lock_name}' has been failing for {failure_duration:.1f}s")
        self.lock_name = lock_name
        self.failure_duration = failure_duration
