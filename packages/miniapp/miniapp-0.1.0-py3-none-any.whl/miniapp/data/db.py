"""
Interface to Data

An extremely simple interface is defined which lets us easily implement in memory, or connect to real databases.

The interface looks like, and can be thought of, as a very much simplified MongoDB client.
"""
import uuid
import re
import time
import sys

from miniapp.data.const import *
from miniapp.errs import InternalError


class SimplestDb(object):
    """
    The abstract interface, defining minimal database functionality.
    """

    def new_connection(self):
        """
        Makes a new, separate connection to the same database.  Useful when forking, since some database drivers are not
        fork-safe.
        """
        return self

    def lookup(self, collection: str, what_to_lookup, fields=None):
        """
        Get a single record.  Shortcut for querying on a row id.

        :param collection:      Which collection.
        :param what_to_lookup:  Row ID (or a query string).

        :returns:  Record, if found, or None if not found.
        """
        rr = self.query(collection, query=what_to_lookup, fields=fields, limit=2)
        if not isinstance(rr, list):
            rr = list(rr)
        if len(rr) >= 2:
            raise InternalError(
                "lookup() had multiple results - 'what_to_lookup' must be guaranteed to be unique",
                private_details={"what_to_lookup": what_to_lookup}
            )
        return rr[0] if rr else None

    def query(self, collection: str, query=None, fields=None, sort=None, limit=None):
        """
        Scan for documents, or retrieve a specific document.

        :param collection:   Name of collection.
        :param query:        JSON-style query with named fields to exactly match.
        :param fields:       Which fields to return, None for all.  [] for list to include {f:0} for fields to exclude.
        :param sort:         A list of sort keys.  Each is a tuple: (fieldName, ascending(1)/descending(-1))
        :param limit:        Maximum number of records.

        :return:    An iteration of matched documents, or a generator.
        """
        return []

    def insert(self, collection: str, doc):
        """
        Add a document to a collection.  Note that field names cannot start with '$' since we use them for queries.
        :returns:  ID of new row.
        """
        return ""

    def update(self, collection: str, what_to_update, changes: dict, upsert=False):
        """
        Update fields in a collection.
        :param collection:  Name of collection we're working on.
        :param what_to_update: ID of record we'll be changing, or a query.
        :param changes: A {} with named changes to make.  $set, $push and $inc are supported.
        :param upsert: If True, a new row will be created if none exists.
        """

    def replace(self, collection: str, id_to_replace: str, new_doc):
        """
        Replace a document in a collection.  $ operators are not allowed.
        """

    def delete(self, collection: str, what_to_delete):
        """
        Delete a document from a collection.
        :param what_to_delete:  Usually the ID of a row, but can also be a query to delete multiple rows.
        """

    def file_create(self, properties: dict):
        """
        Create a new file with the given properties.
        :param properties:  Properties to associate with the file.
        :return:   A tuple: the ID of the new file, and a file-like interface for writing.
        """
        file_id = self.insert(self.FILES_COLLECTION, properties)
        return file_id, ChunkWriter(self._writer(file_id), chunk_size=self.FILES_CHUNK)

    def file_read(self, file_id: str):
        """
        Open a stream on a file with a given ID.
        :param file_id:   Which file.
        :return:   A file-like interface.
        """
        chunk_ids = [_ for _ in
                     self.query(self.FILES_DATA, {"file_id": file_id}, fields=["_id", "size"], sort=[("sequence", 1)])]
        reader = lambda chunk_id: self.lookup(self.FILES_DATA, chunk_id, fields=["data"])["data"]
        return ChunkReader(chunk_ids, reader)

    def file_list(self, query: dict=None):
        """
        Query files based on properties.
        :param query:  A query of the same sort as query().
        :return:   An iteration of results.
        """
        return self.query(self.FILES_COLLECTION, query)

    def file_write(self, file_id: str, append: bool=False):
        """
        Write or append to a given file.
        :param file_id:   Which file.
        :param append:      Append or replace.
        :return:    A file-like interface.
        """
        if not append:
            self.delete(self.FILES_DATA, {"file_id": file_id})
        return ChunkWriter(self._writer(file_id), chunk_size=self.FILES_CHUNK)

    def file_delete(self, file_id: str):
        """
        Delete a file.
        """
        self.delete(self.FILES_COLLECTION, file_id)
        self.delete(self.FILES_DATA, {"file_id": file_id})

    def ensure_index(self, collection: str, fields: (list, tuple), ttl: int=None, unique: bool=False):
        """
        Make sure a given index is defined.
        :param collection:  Name of collection which needs the index.
        :param fields:      Iterable of field_name.
        :param ttl:         Signals for the underlying engine to delete old rows, following the convention of MongoDB.
        :param unique:      Enforces uniqueness.
        """

    def status(self):
        """
        Get server status.
        """
        return {}

    def drop_collection(self, collection: str):
        """
        Drop a named collection.
        """

    def drop_database(self, name: str):
        """
        Drop a named database.
        """

    def _to_field_selector(self, fields):
        """
        Convert various types of field selector into a consistent {}.
        """
        if isinstance(fields, FieldList):
            return fields.compile()
        #!!!
        return fields

    def _to_query_obj(self, query: (str, dict)=None):
        """
        Convert the various supported types of query into a consistent {}.
        :param query:   A str to look for a particular row ID or a {} with query rules.
        :return:        A {} which follows the rules for queries.
        """
        if isinstance(query, str):
            return {ROW_ID: query}
        return query

    def _assert_valid_for_storage(self, obj, name: str = None):
        """
        Enforce storable data types.
        """
        if isinstance(obj, (int, bool, float, str, bytes, bytearray, type(None))):
            return True
        name = name or ""
        if isinstance(obj, dict):
            for k, v in obj.items():
                # TODO verify valid keys for mongo (no start with $, etc.)
                self._assert_valid_for_storage(v, ((name + ".") if name else "") + k)
            return True
        if isinstance(obj, (list, tuple)):
            for n, v in enumerate(obj):
                self._assert_valid_for_storage(v, ((name + ".") if name else "") + str(n))
            return True
        raise ValueError(f"Invalid data type for storage: {type(obj)}, path={name or ''}")

    def _writer(self, file_id: str):
        sequence = [0]
        def writer(chunk):
            sequence[0] += 1
            self.insert(self.FILES_DATA, {"file_id": file_id, "size": len(chunk), "data": chunk, "sequence": sequence[0]})
        return writer

    FILES_COLLECTION = "files"
    FILES_DATA = "files_data"
    FILES_CHUNK = 16*1024*1024


class FieldList(object):
    """
    A set of inclusions and exclusions, to determine which fields to include.
    """

    def __init__(self, spec: (list, tuple, set, dict) = None):
        self._fields = {}
        self._default = False
        if spec is None or isinstance(spec, dict) and not spec:
            # NOTE: empty lists mean 'only the ID field', whereas empty {}s or None mean 'all fields'
            self._default = True
        elif isinstance(spec, dict):
            any_1 = False
            for k, v in spec.items():
                if v:
                    self.include(k)
                    any_1 = True
                else:
                    self.exclude(k)
            if not any_1:
                self._default = True
            elif ROW_ID not in self._fields:
                self._fields[ROW_ID] = True
        elif hasattr(spec, "__iter__"):
            for k in spec:
                self.include(k)
            if ROW_ID not in self._fields:
                self._fields[ROW_ID] = True

    def filter(self, record: dict):
        return {k: v for k, v in record.items() if self.test(k)}

    def test(self, field: str):
        return self._fields.get(field, self._default)

    def include(self, field: str):
        self._fields[field] = True

    def exclude(self, field: str):
        self._fields[field] = False

    def clear(self, field: str = None):
        if field:
            self._fields.pop(field, None)
        else:
            self._fields.clear()

    def compile(self):
        """
        Simplify down to a python object.  A [] when only including fields, or a {} when excluding is involved.
        """
        # FIXME reconcile value of self._default - it might not be possible to represent it as an object
        if any(not v for v in self._fields.values()):
            out = {k: int(v) for k, v in self._fields.items()}
            if self._default is False:
                out.pop(ROW_ID, None)
            return out
        return [k for k in self._fields if k != ROW_ID]


class RealMongoDb(SimplestDb):
    """
    A real mongo database, following the abstract interface.
    """
    def __init__(self, mongo_uri, default_database: str=None):
        # we only import pymongo when this class gets used
        import pymongo
        bare_uri, db_name = self.parse_uri(mongo_uri, default_database=default_database)
        self.database_name = db_name
        # connect, with retries
        for retry in [1, 1, 1, 1, 0]:
            try:
                conn = pymongo.MongoClient(bare_uri, connect=True, serverSelectionTimeoutMS=10000)
                # verify connection
                conn.server_info()
                self.conn = conn
                self.db = conn[db_name]
                self.db_uri = mongo_uri
                break
            except Exception as err:
                if retry:
                    print("problem connecting to database, retrying - %s" % err)
                    sys.stdout.flush()
                    time.sleep(15)
                else:
                    raise

    def new_connection(self):
        return RealMongoDb(self.db_uri)

    def query(self, collection: str, query=None, fields=None, sort=None, limit=None):
        return self.db[collection].find(self._to_query_obj(query), self._to_field_selector(fields), sort=sort, limit=limit or 0)

    def insert(self, collection: str, doc):
        row_id = doc.get(ROW_ID)
        if not row_id:
            doc = dict(doc)
            doc[ROW_ID] = str(uuid.uuid4())
        # TODO if ROW_ID is taken (i.e. custom user value), the expectation of SimplestDB is that the row will
        #   be replaced -- is that what happens in MongoDB?
        resp = self.db[collection].insert_one(doc)
        return str(resp.inserted_id)

    def update(self, collection: str, what_to_update, update: dict, upsert=False):
        if is_special_update(update):
            use_upd = update
        else:
            # TODO detect unsupported $ keys
            use_upd = {UPDATE_SET: update}
        if isinstance(what_to_update, str):
            return self.db[collection].update_one(self._to_query_obj(what_to_update), use_upd, upsert=upsert)
        else:
            return self.db[collection].update_many(self._to_query_obj(what_to_update), use_upd, upsert=upsert)

    def replace(self, collection: str, id_to_update, update):
        return self.db[collection].replace_one({ROW_ID: id_to_update}, update, upsert=True)

    def delete(self, collection: str, what_to_delete):
        query = self._to_query_obj(what_to_delete)
        if isinstance(what_to_delete, str):
            return self.db[collection].delete_one(query).deleted_count
        return self.db[collection].delete_many(query).deleted_count

    def ensure_index(self, collection: str, fields: (list, tuple), ttl: int=None, unique: bool=False):
        more = {
            "background": True
        }
        if ttl:
            more["expireAfterSeconds"] = ttl
        if unique:
            more["unique"] = True
        self.db[collection].create_index([(f, 1) for f in fields], **more)

    def status(self):
        return self.db.command("serverStatus")

    def drop_database(self, name: str):
        self.conn.drop_database(name)

    def drop_collection(self, collection: str):
        self.db[collection].drop()

    @staticmethod
    def parse_uri(uri: str, default_database: str=None):
        m = RealMongoDb.PTN_DBNAME.match(uri)
        if m is None:
            raise InternalError("MongoDB URI syntax not recognized", private_details={"uri": uri})
        return m.group(1), m.group(4) or default_database

    # see https://docs.mongodb.com/manual/reference/connection-string/
    #  mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[database][?options]]
    PTN_DBNAME = re.compile(r'^(mongodb([-+][a-z0-9-]+)?://[^#?]+?)(/([^/#?]+)(\?(.*))?)?$')


class ChunkReader(object):
    """
    This class is used to turn the stored file chunks into a stream.  See SimplestDb.file_read().
    """
    def __init__(self, chunk_info: list, reader: callable):
        """
        A file-like object that reads data in chunks.

        :param chunk_info:  A list of chunk records with "_id" and "size".
        :param reader:      Method to read each chunk.
        """
        self.buf = None
        self.all_chunks = chunk_info
        self.chunks = chunk_info[:]
        self.reader = reader
        self.pos = 0

    def seekable(self):
        return True

    def seek(self, n, rel=0):
        if rel == 1 and n >= 0:
            rel = 0
            n += self.pos
        if rel == 1:
            raise InternalError("ChunkReader: not supported, seeking backwards from current position")
        if rel == 0:
            # seek forward
            if n == self.pos:
                return
            self.buf = None
            self.chunks = self.all_chunks[:]
            self.pos = 0
            while n > 0 and self.chunks:
                chunk = self.chunks.pop(0)
                chunk_size = chunk["size"]
                if chunk_size < n:
                    n -= chunk_size
                    self.pos += chunk_size
                else:
                    self.pos += n
                    self.buf = bytearray(self.reader(chunk["_id"])[n:])
                    break
        if rel == 2:
            # seek backwards from end
            filesize = sum(chunk["size"] for chunk in self.all_chunks)
            if filesize + n == self.pos:
                return
            self.pos = filesize
            self.buf = None
            self.chunks = []
            tail = self.all_chunks[:]
            while n < 0 and tail:
                chunk = tail.pop(-1)
                chunk_size = chunk["size"]
                if chunk_size < -n:
                    n += chunk_size
                    self.pos -= chunk_size
                    self.chunks.insert(0, chunk)
                else:
                    chunk_data = self.reader(chunk["_id"])
                    self.buf = bytearray(chunk_data[n:])
                    self.pos += n
                    break

    def tell(self):
        return self.pos

    def read_all(self):
        chunks = []
        while True:
            chunk = self.read_chunk(1000000000)
            if chunk:
                chunks.append(chunk)
            else:
                break
        return b"".join(chunks)

    def read_chunk(self, n: int):
        if not self.buf:
            if self.chunks:
                chunk_id = self.chunks.pop(0)["_id"]
                self.buf = bytearray(self.reader(chunk_id))
            else:
                return None
        out = self.buf[:n]
        self.buf = self.buf[n:]
        return out

    def read(self, n: int = -1):
        if self.buf is not None and n < 0:
            n = 1000000000
        if n >= 0:
            chunks = []
            while n > 0:
                chunk = self.read_chunk(n)
                if not chunk:
                    break
                chunks.append(chunk)
                n -= len(chunk)
            return b''.join(chunks)
        else:
            return self.read_all()

    def close(self):
        self.buf = None


class ChunkWriter(object):
    def __init__(self, writer: callable, chunk_size: int):
        """
        A file-like object that writes data in chunks.

        :param writer:          Writes each chunk.
        :param chunk_size:      How big to make the chunks.
        """
        self.chunk_size = chunk_size
        self.writer = writer
        self.written = 0

    def write(self, data):
        n_wr = len(data)
        if isinstance(data, str):
            data = data.encode("utf-8")
        while data:
            out = data[:self.chunk_size]
            data = data[self.chunk_size:]
            self.writer(out)
        self.written += n_wr
        return n_wr

    def flush(self):
        """ write out pending changes (placeholder) """

    def close(self):
        """ clean up (placeholder) """


def is_special_update(update: dict) -> bool:
    """
    Detect update commands.

    :param update: An update request, i.e. for SimplestDb.update().
    :return:    True if any special update commands were found.
    """
    if not update:
        return False
    for f in UPDATE__ALL:
        if f in update:
            return True
    return False
