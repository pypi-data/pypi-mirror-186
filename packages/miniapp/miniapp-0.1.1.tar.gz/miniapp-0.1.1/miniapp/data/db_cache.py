import time
import random

from .db import SimplestDb


def generate_db_cache(db: SimplestDb, collection: str, expiration_time: int=None, random_range: int=0):
    """
    Generate a dict-like object based on a database.
    :param db:              Which database.
    :param collection:      Which collection.
    :param expiration_time: How soon objects expire in the cache.
    :param random_range:    Optionally extends 'expiration_time' by a random amount to prevent 'clumping' of
                            expirations.
    :return:  Cache instance.
    """
    return DbCache(db, collection, expiration_time, random_range)


class DbCache(object):
    def __init__(self, db, collection, expiraton_time, random_range):
        self.db = db
        self.collection = collection
        self.expiration_time = expiraton_time
        self.random_range = random_range
        # TODO use a 'ttl' index to ensure objects get expired when that feature is available
        #  - i.e. db.ensure_index(..., ttl=...)

    def __getitem__(self, item):
        v = self.get(item)
        if v is None:
            raise KeyError(item)
        return v

    def __setitem__(self, key, value):
        t_now = time.time()
        exp_time = t_now + self.expiration_time
        if self.random_range:
            exp_time += random.randint(-self.random_range, self.random_range)
        self.db.replace(self.collection, str(key), {"_id": str(key), "expires": exp_time, "value": value})

    def __delitem__(self, key):
        self.db.delete(self.collection, str(key))

    def get(self, item, default=None):
        t_now = time.time()
        rec = self.db.lookup(self.collection, str(item))
        if rec:
            expires = rec.get("expires")
            if expires and expires < t_now:
                return
            return rec.get("value")
        return default

    def __contains__(self, item):
        v = self.get(item)
        return v is not None

    def __iter__(self):
        t_now = time.time()
        for rec in self.db.query(self.collection):
            expires = rec.get("expires")
            if expires and expires < t_now:
                continue
            yield rec.get("_id")

    def keys(self):
        return iter(self)

    def clear(self):
        """
        Clear the cache.
        """
        self.db.delete(self.collection, {})
