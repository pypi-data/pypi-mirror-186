import collections
import time
import threading


class LruCache:
    """
    Very simple in-memory cache with an upper limit for maximum records, an upper limit
    for how long to retain information, and a flag to choose between two modes of
    expiration.
    """

    def __init__(self, max_size=0, expiration_time=0, refresh_expiration_on_read=False, enabled=True,
                 expiration_handler=None):
        """
        Set up a cache.
        :param max_size:                 Maximum entries to allow before letting them 'fall off the other side', i.e.
                                        before discarding the oldest entries.
        :param expiration_time:          How long to keep entries before automatically discarding them (seconds).
        :param refresh_expiration_on_read: Whether read access causes the expiration timer to be reset.
        :param enabled:                 Completely enables or disables the cache.  A disabled cache always
                                        fails to find anything on read.
        """
        self.max_size = max_size
        self.expiration_time = expiration_time
        self.refresh_expiration_on_read = refresh_expiration_on_read and expiration_time
        self.cache = collections.OrderedDict() if max_size else {}
        self.times = {}
        self.enabled = enabled
        self.lock = threading.RLock()
        self.expiration_handler = expiration_handler

    def _on_expired(self, key, value):
        if self.expiration_handler:
            self.expiration_handler(key, value)

    def _now(self):
        return time.time()

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        if key in self.cache:
            del self.cache[key]
            del self.times[key]

    def __iter__(self):
        now = self._now()
        with self.lock:
            expired = []
            for k in self.cache.keys():
                if not self.expiration_time or self.times.get(k) >= now:
                    yield k
                else:
                    expired.append(k)
            for exp in expired:
                self._on_expired(exp, self.cache[exp])
                del self.cache[exp]
                del self.times[exp]

    def __len__(self):
        if not self.enabled:
            return 0
        with self.lock:
            self._purge_expired()
            return len(self.cache)

    def __contains__(self, item):
        if item not in self.cache:
            return False
        if self.expiration_time and self.times.get(item) < self._now():
            self._on_expired(item, self.cache[item])
            del self.cache[item]
            del self.times[item]
            return False
        return True

    def clear(self):
        with self.lock:
            self.cache.clear()
            self.times.clear()

    def keys(self):
        return self.cache.keys()

    def items(self):
        """
        Iterate all keys and values.  Iterating with this method does NOT reset expiration times.
        """
        return self.cache.items()

    def _purge_expired(self):
        if not self.expiration_time:
            return
        now = self._now()
        expired = []
        for k in self.cache.keys():
            if self.times.get(k) < now:
                expired.append(k)
        for k in expired:
            self._on_expired(k, self.cache[k])
            del self[k]

    def get(self, key, default=None):
        if not self.enabled:
            return None
        with self.lock:
            # check for value
            if self.max_size:
                value = self.cache.pop(key, None)
            else:
                value = self.cache.get(key, None)
            if value is not None:
                # found - check for expiration
                if self.expiration_time:
                    now = self._now()
                    if self.times.get(key) < now:
                        # expired - don't return the data
                        self._on_expired(key, value)
                        self.__delitem__(key)
                        return None
                    # refresh expiration time
                    if self.refresh_expiration_on_read:
                        self.times[key] = now + self.expiration_time
                # refresh LRU sequence
                if self.max_size:
                    self.cache[key] = value
            return value if value is not None else default

    def set(self, key, value):
        if not self.enabled:
            return
        with self.lock:
            # check for value (and remove it)
            # enforce record limit
            if self.cache.pop(key, None) is None \
                    and self.max_size and len(self.cache) >= self.max_size:
                old = self.cache.popitem(last=False)
                self.times.pop(old[0])
            # put value back on top (or insert for the first time)
            self.cache[key] = value
            # refresh or set expiration time
            self.times[key] = self._now() + self.expiration_time

    def pop(self, key, default=None):
        with self.lock:
            old = self.get(key, default)
            if key in self.cache:
                self.cache.pop(key, None)
                self.times.pop(key, None)
            return old
