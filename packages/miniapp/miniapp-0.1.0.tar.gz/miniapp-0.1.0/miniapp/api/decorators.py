"""
A decorator to apply caching to class methods, using a cache field belonging to their enclosing class.

class MyClass(object):
    def __init__(self):
        self._cache = {}

    @apply_class_cache(key='a')
    def a(self):
        ....

    @apply_class_cache(key=lambda inst, arg: arg)
    def b(self, arg):
        ...
"""
import functools


class apply_class_cache(object):
    def __init__(self, key: (str, callable), cache_field: str="_cache"):
        self.key = key
        self.cache_field = cache_field

    def __call__(self1, wrapped_fn):
        @functools.wraps(wrapped_fn)
        def f_w(self, *args, **kwargs):
            if isinstance(self1.key, str):
                key = self1.key
            else:
                key = self1.key(self, *args, **kwargs)
            cache = getattr(self, self1.cache_field)
            value_out = cache.get(key)
            if value_out is None:
                value_out = wrapped_fn(self, *args, **kwargs)
                cache[key] = value_out
            return value_out
        return f_w
