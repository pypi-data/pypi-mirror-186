from miniapp.data.const import ROW_ID
from miniapp.data.db import SimplestDb, RealMongoDb
from miniapp.data.db_disk import SimplestDiskDb
from miniapp.data.impl import InMemoryDb


def connect_to_db(db_uri: str, logger: callable=None) -> SimplestDb:
    """
    Connect to a SimplestDb instance, given a URI.
    :param db_uri:  'memory': an in-memory instance,
                    'disk:<folder>': an on-disk instance,
                    'mongodb:...': connect to a remote MongoDb engine.
    :param logger:  To print connection messages.
    :return:        A SimplestDb instance.
    """
    import time
    import os
    from miniapp.utils.misc import split_url, join_url
    logger = logger or (lambda msg: None)
    if db_uri in ("mock", "memory"):
        return InMemoryDb()
    if db_uri.startswith("disk:"):
        db_folder = db_uri.split(":")[1]
        if "~" in db_folder:
            db_folder = os.path.expanduser(db_folder)
        return SimplestDiskDb(db_folder)
    if db_uri.startswith("mongodb:"):
        u_p = split_url(db_uri, omit_password=True)
        clean_uri = join_url(u_p)
        t0 = time.time()
        logger("connecting to db on %s" % clean_uri)
        db = RealMongoDb(db_uri, default_database="wbdash")
        t_connect = time.time() - t0
        logger("  connected in %.3fs" % t_connect)
        return db
    raise ValueError(f"Unrecognized database URI: {db_uri}")
