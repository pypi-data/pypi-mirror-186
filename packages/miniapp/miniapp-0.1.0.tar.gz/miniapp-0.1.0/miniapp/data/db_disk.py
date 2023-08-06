import os
import threading
import collections
import time
import pickle
import json
import shutil
import uuid
import hashlib

from miniapp.data.const import ROW_ID
from miniapp.data.impl import apply_update, compile_query, apply_sort_fields_limit, InMemoryDb


class SimplestDiskDb(InMemoryDb):
    """
    Implement InMemoryDb using only files, and a little in-memory caching for small tables.
    """
    def __init__(self, folder: str, save_interval: float=0.25, threshold_switch_to_folder=1000000):
        super(SimplestDiskDb, self).__init__()
        if not folder:
            raise ValueError("missing 'folder'")
        if "~" in folder:
            folder = os.path.expanduser(folder)
        self.folder = folder
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)
        self.rd_locks = collections.defaultdict(threading.Lock)
        self.wr_lock = threading.Lock()
        self.need_write = set()
        self.writer = None
        self.save_interval = save_interval
        self.idle_cycles = 10
        self.threshold_switch_to_folder = threshold_switch_to_folder

    def _bg_write(self):
        idle = 0
        while idle < self.idle_cycles:
            time.sleep(self.save_interval)
            with self.wr_lock:
                to_write = set(self.need_write)
                self.need_write.clear()
                if not to_write:
                    idle += 1
                    continue
                idle = 0
                if not os.path.exists(self.folder):
                    # if the folder gets deleted we stop writing to it
                    #  (i.e. during a unit test)
                    return
                for collection in to_write:
                    coll_data = self.data[collection]
                    if isinstance(coll_data, FilesystemTable):
                        # TODO have folders also write in the background
                        pass
                    else:
                        fn = os.path.join(self.folder, collection)
                        coll_data = dict(coll_data)
                        with open(fn, 'w') as f_w:
                            f_w.write("{\n")
                            first = True
                            for k, v in sorted(coll_data.items()):
                                if not first:
                                    f_w.write(",\n")
                                first = False
                                f_w.write(json.dumps(k))
                                f_w.write(": ")
                                f_w.write(json.dumps(v))
                            f_w.write("\n}\n")
        self.writer = None

    def _sched_write(self, collection: str):
        self.need_write.add(collection)
        if not self.writer:
            bg = threading.Thread(target=self._bg_write, daemon=True, name="db_disk.sched_write")
            bg.start()
            self.writer = bg

    def _load_coll(self, collection: str):
        """
        Load either a whole collection (small), or set up a FilesystemTable() for large tables.
        """
        if "/" in collection or collection.startswith("."):
            raise Exception("invalid collection: %s" % collection)
        lock = self.rd_locks[collection]
        with lock:
            if collection not in self.data:
                fn = os.path.join(self.folder, collection)
                if os.path.isdir(fn):
                    # if the named collection has a folder, it is stored as separate files
                    self.data[collection] = FilesystemTable(fn)
                elif os.path.exists(fn):
                    with open(fn, 'rb') as f_r:
                        raw = f_r.read()
                    # if it's a regular file it's a single JSON file
                    try:
                        self.data[collection] = json.loads(raw) if raw else {}
                    except ValueError:
                        try:
                            self.data[collection] = pickle.loads(raw)
                        except Exception as err:
                            # we throw away corrupted data for now
                            import tempfile
                            with tempfile.NamedTemporaryFile(suffix="_save-%s" % collection, mode='wb', delete=False) as f_tmp:
                                f_tmp.write(raw)
                            print("COLLECTION CORRUPTED: %s - saved to %s" % (fn, f_tmp.name))
                            self.data[collection] = {}
        return self.data[collection]

    def query(self, collection: str, query=None, fields=None, **kwargs):
        data = self._load_coll(collection)
        if isinstance(data, FilesystemTable):
            query = self._to_query_obj(query)
            fields = self._to_field_selector(fields)
            return data.find(query, fields=fields, **kwargs)
        return super(SimplestDiskDb, self).query(collection, query, fields=fields, **kwargs)

    def insert(self, collection, record):
        data = self._load_coll(collection)
        if isinstance(data, FilesystemTable):
            id = record.get(ROW_ID)
            if not id:
                id = str(uuid.uuid4())
            return data.set(id, record, is_new=True)
        with self.wr_lock:
            resp = super(SimplestDiskDb, self).insert(collection, record)
            if not self._consider_upgrade_to_folder(collection, data):
                self._sched_write(collection)
            return resp

    def update(self, collection: str, what_to_update, changes: dict, upsert=False):
        data = self._load_coll(collection)
        if isinstance(data, FilesystemTable):
            # single record
            if isinstance(what_to_update, str):
                data.update(what_to_update, changes)
                return
            # bulk update
            # TODO we should scan each shard separately - currently we read, then write for every record we modify!
            for rec in self.query(collection, query=what_to_update, fields=(ROW_ID,)):
                data.update(rec[ROW_ID], changes)
        with self.wr_lock:
            super(SimplestDiskDb, self).update(collection, what_to_update, changes=changes, upsert=upsert)
            if not self._consider_upgrade_to_folder(collection, data):
                self._sched_write(collection)

    def replace(self, collection, id_to_replace, new_doc):
        data = self._load_coll(collection)
        if isinstance(data, FilesystemTable):
            data.set(id_to_replace, new_doc)
            return
        with self.wr_lock:
            super(SimplestDiskDb, self).replace(collection, id_to_replace, new_doc)
            if not self._consider_upgrade_to_folder(collection, data):
                self._sched_write(collection)

    def delete(self, collection, what_to_delete):
        data = self._load_coll(collection)
        if isinstance(data, FilesystemTable):
            data.delete(what_to_delete)
            return
        with self.wr_lock:
            super(SimplestDiskDb, self).delete(collection, what_to_delete)
            self._sched_write(collection)

    def _consider_upgrade_to_folder(self, collection, data):
        """
        We store small collections in memory, backed up as single files.  When they grow above a certain size we turn
        them into folders with sharded subsets of the overall data set.
        :param collection:  Which collection.
        :param data:        The in-memory data.

        :return:   True if we upgraded to a folder.
        """
        fn = os.path.join(self.folder, collection)
        if not os.path.exists(fn):
            return
        file_size = os.stat(fn).st_size
        if file_size > self.threshold_switch_to_folder:
            folder = os.path.join(self.folder, collection)
            os.remove(folder)
            table = FilesystemTable(folder)
            self.data[collection] = table
            for id, rec in data.items():
                table.set(id, rec)
            return True

    def _file_fn(self, file_id: str):
        if "/" in file_id or "." in file_id or " " in file_id or len(file_id) < 10 or len(file_id) > 40:
            raise Exception("invalid file_id %s" % file_id)
        return os.path.join(self.folder, "_files_", file_id)

    def file_create(self, properties: dict):
        file_id = self.insert(self.FILES_COLLECTION, properties)
        f_folder = os.path.join(self.folder, "_files_")
        if not os.path.exists(f_folder):
            os.mkdir(f_folder)
        return file_id, open(self._file_fn(file_id), 'wb')

    def file_list(self, query: dict=None):
        return self.query(self.FILES_COLLECTION, query)

    def file_read(self, file_id: str):
        fn = self._file_fn(file_id)
        if os.path.exists(fn):
            return open(fn, 'rb')

    def file_write(self, file_id: str, append: bool=False):
        fn = self._file_fn(file_id)
        if os.path.exists(fn):
            return open(self._file_fn(file_id), 'ab' if append else 'wb')

    def file_delete(self, file_id: str):
        self.delete(self.FILES_COLLECTION, file_id)
        fn = self._file_fn(file_id)
        if os.path.exists(fn):
            os.remove(fn)


class FilesystemTable(object):
    """
    Manages a single "mongoish" table in a folder.
    """
    def __init__(self, folder: str, n_bins=37):
        self.folder = folder
        self.n_bins = n_bins
        if not os.path.exists(folder):
            os.mkdir(folder)
        self.lock = threading.Lock()

    def file_for_id(self, id):
        bin = _id_hash(id) % self.n_bins
        return os.path.join(self.folder, "bin_%02x" % bin)

    def iter_bins(self):
        for f in os.listdir(self.folder):
            if f.startswith("bin_"):
                yield os.path.join(self.folder, f)

    def read_bin(self, bin_file: str):
        out = {}
        if os.path.exists(bin_file):
            with open(bin_file, 'r') as f_r:
                for line in f_r:
                    row = json.loads(line)
                    out[row[ROW_ID]] = row
        return out

    def write_bin(self, bin_file: str, records):
        with open(bin_file, 'w') as f_w:
            for row in records:
                f_w.write(json.dumps(row))
                f_w.write("\n")

    def append_bin(self, bin_file: str, record):
        with open(bin_file, 'a') as f_w:
            f_w.write(json.dumps(record))
            f_w.write("\n")

    def get(self, id):
        """
        Retrieve the record with a given ID.
        """
        records_in_bin = self.read_bin(self.file_for_id(id))
        return records_in_bin.get(id)

    def set(self, id, record: dict, is_new: bool=False):
        """
        Store a record with a given ID.
        """
        if record.get(ROW_ID) != id:
            record = dict(record)
            record[ROW_ID] = id
        with self.lock:
            bin_file = self.file_for_id(id)
            if is_new:
                self.append_bin(bin_file, record)
                return
            records_in_bin = self.read_bin(bin_file)
            if id in records_in_bin:
                records_in_bin[id] = record
                self.write_bin(bin_file, records_in_bin.values())
            else:
                records_in_bin[id] = record
                self.append_bin(bin_file, record)

    def update(self, id: str, changes: dict):
        # FIXME we were doing a deepcopy here -- why?
        #   record = copy.deepcopy(self.get(id))
        record = self.get(id)
        if record is not None:
            apply_update(record, changes)
            self.set(id, record)

    def delete(self, id):
        """
        Delete a given row.
        """
        if isinstance(id, dict):
            return self._delete_bulk(query=id)
        with self.lock:
            bin_file = self.file_for_id(id)
            records_in_bin = self.read_bin(bin_file)
            if records_in_bin.pop(id, None):
                self.write_bin(bin_file, records_in_bin.values())

    def _delete_bulk(self, query: dict):
        compiled_filter = compile_query(query)
        with self.lock:
            for bin_file in self.iter_bins():
                records_in_bin = self.read_bin(bin_file)
                len0 = len(records_in_bin)
                records_in_bin = {k: v for k, v in records_in_bin.items() if not compiled_filter(v)}
                len1 = len(records_in_bin)
                if len1 != len0:
                    self.write_bin(bin_file, records_in_bin.values())

    def find(self, query: dict=None, fields=None, sort=None, limit=None):
        """
        Scan the whole table for matches.
        """
        rows = list(self._find(query))
        if fields or sort or limit:
            rows = apply_sort_fields_limit(rows, sort=sort, fields=fields, limit=limit)
        return rows

    def _find(self, query: dict=None):
        if query and list(query.keys()) == [ROW_ID]:
            match = self.get(query[ROW_ID])
            if match:
                yield match
            return
        compiled_filter = compile_query(query)
        with self.lock:
            for bin_file in self.iter_bins():
                records_in_bin = self.read_bin(bin_file)
                for rec in records_in_bin.values():
                    if compiled_filter(rec):
                        yield rec

    def purge(self):
        """
        Remove all data.
        """
        shutil.rmtree(self.folder)


def _id_hash(id):
    """
    Generate a shardable value for a row ID.
    """
    if isinstance(id, str):
        id = id.encode("UTF-8")
    elif not isinstance(id, (bytes, bytearray)):
        id = str(id).encode("UTF-8")
    # NOTE: not used as a cipher, ok to use md5 here
    raw = hashlib.md5(id).digest()[-2:]
    return abs(raw[0] * 256 + raw[1])
