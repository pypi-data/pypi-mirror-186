"""
Keeps track of number of distinct sessions over time.
"""
import time


class DistinctSessionTimeline(object):
    def __init__(self, interval=15*60, keep_intervals=24*4):
        self.interval = interval
        self.keep_intervals = keep_intervals
        self.timeline = []
        self.bucket_n = None
        self.current_sessions = set()

    def _bucket_now(self):
        return time.time() // self.interval

    def _update(self):
        bucket = self._bucket_now()
        if bucket == self.bucket_n:
            return
        if not self.bucket_n:
            self.bucket_n = bucket
            self.timeline.append(0)
        while self.bucket_n < bucket:
            self.timeline.append(0)
            self.current_sessions.clear()
            self.bucket_n += 1
        if len(self.timeline) > self.keep_intervals:
            self.timeline = self.timeline[-self.keep_intervals:]

    def add_sample(self, session_id):
        """
        Record activity under a given session ID.
        """
        if not session_id:
            return
        self._update()
        self.current_sessions.add(session_id)
        self.timeline[-1] = len(self.current_sessions)

    def get_timeline(self):
        """
        Get the current timeline.  This is a [] with the number of distinct sessions.  The last entry represents the
        current (incomplete) interval.
        """
        self._update()
        return self.timeline

    def _inject_class_method(self, target_object, method_name: str):
        orig = getattr(target_object, method_name)
        def intercept(session_id, *args, **kwargs):
            self.add_sample(session_id)
            return orig(session_id, *args, **kwargs)
        setattr(target_object, method_name, intercept)

    def inject_into_session_handler(self, session_handler):
        self._inject_class_method(session_handler, "load_session")
        self._inject_class_method(session_handler, "save_session")
