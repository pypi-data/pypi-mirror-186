"""
Tools for running SQL against SimplestDb databases.
"""
from dslibrary.sql.compiled import Node_Field, Node_Op, node_is_literal
from dslibrary.sql.compiler import SqlCompiler
from dslibrary.sql.data import SqlDataSupplier, SqlTableStream, SqlFieldInfo
from dslibrary.sql.eval_utils import SqlEvaluationContext
from dslibrary.sql.misc import loose_table_match
from dslibrary.sql.parser import SqlParser

from miniapp.data.impl import combine_filters_and


def query_mini_db(sql: str, query_method, default_collection=None, allowed_collections=None, base_filter: dict=None):
    """
    Run SQL against a simple mongodb-style database.
    :param sql:             SQL to run
    :param query_method:            Query method which takes these arguments: (collection_name, query, limit, sort)
    :param default_collection:      This collection is queried by default.
    :param allowed_collections:     List of collections which can be referenced.
    :param base_filter:             The view can be limited.
    :return:    A tuple of (0): column names and (1): row values.
    """
    data = MiniDbDataSupplier(query_method, default_collection, allowed_collections, base_filter=base_filter)
    c = SqlCompiler()
    sel = SqlParser(sql).parse_select_only()
    ctx = SqlEvaluationContext(compiler=c)
    ctx.addDataSupplier(data)
    compiled = c.compile_select(sel, ctx)
    compiled.supplyContext(ctx)
    rows = list(compiled.getRowIterator())
    cols = tuple(field.alias or field.field for field in compiled.getFields())
    return cols, rows


class MiniDbDataSupplier(SqlDataSupplier):
    """
    Provides table data from data in memory.
    """
    def __init__(self, query_method, default_collection, allowed_collections=None, db_name: str=None, base_filter: dict=None):
        self.query_method = query_method
        self.default_collection = default_collection
        self.allowed_collections = allowed_collections or ([default_collection] if default_collection else [])
        self.db_name = db_name
        self.base_filter = base_filter
        self.col_name_cache = {}

    def getTableStream(self, table_spec):
        table_name = table_spec[-1]
        db_name = table_spec[-2] if len(table_spec) > 1 else None
        if self.db_name or db_name:
            if not self.db_name or not db_name:
                return None
            if db_name.lower() != self.db_name.lower():
                return None
        real_table_name = loose_table_match(table_name, self.allowed_collections) if self.allowed_collections else table_name
        if not real_table_name:
            if self.default_collection:
                real_table_name = self.default_collection
            else:
                return None
        return MiniDbStream(real_table_name, self, table_name)

    def _find_col_names(self, table, max_rows=None):
        out = self.col_name_cache.get(table)
        if out is None:
            # Sorting descending on _id should usually give us the most recently created rows, which should include
            # more recently introduced fields.
            rows = list(self.query_method(table, limit=max_rows, sort=[("_id", -1)]))
            col_names = set()
            for row in rows:
                for col in row.keys():
                    col_names.add(col)
            out = list(sorted(col_names))
            self.col_name_cache[table] = out
        return out


class MiniDbStream(SqlTableStream):
    def __init__(self, real_table_name, supplier, requested_table_name):
        super(SqlTableStream, self).__init__()
        self.supplier = supplier
        self.real_table_name = real_table_name
        self.table_name = requested_table_name
        # TODO this is not a very reliable way to determine field names - see DSW-3592
        col_names = supplier._find_col_names(real_table_name, max_rows=1000)
        self.fields = [SqlFieldInfo(requested_table_name, field) for field in col_names]

    def _query(self, query, limit=None, sort=None):
        return self.supplier.query_method(self.real_table_name, query, limit=limit, sort=sort)

    def supplyContext(self, context):
        self.context = context.derive(fields=self.getFields())

    def getFields(self):
        return self.fields

    def getRowIterator(self, where=None, sort=None, start=0, count=-1):
        where_query = where_to_query(where)
        if self.supplier.base_filter:
            where_query = combine_filters_and(self.supplier.base_filter, where_query)
        for row in self._query(where_query, limit=count if count >= 0 else None, sort=orderby_to_sort(sort)):
            out = tuple(row.get(field.field) for field in self.fields)
            yield out

    def canLimit(self, start, count):
        # TODO support 'start' (mini.db doesn't support it yet)
        if start:
            return False
        return True

    def canWhere(self, where):
        if where and where_to_query(where):
            return True
        return not where

    def canSort(self, sort):
        if not sort or orderby_to_sort(sort):
            return True
        return False

    # TODO pass down list of needed fields (i.e. SELECT a, b FROM table WHERE c < 4 ==> we only need a, b & c)


def orderby_to_sort(orderby):
    """
    Convert a compiled OrderBy clause into a list of (fieldName, -1/+1).
    """
    if not orderby:
        return
    sort = []
    for field, asc in orderby.levels:
        if not isinstance(field, Node_Field):
            return
        sort.append((field.fieldName[-1], 1 if asc else -1))
    return sort


def where_to_query(where):
    """
    Convert a compiled WHERE expression into a MongoDB-style query. i.e. {"f": {"$lt": 100}}.  The target query
    is only the subset of MongoDB filters, supported by wbcommon.mini.db.
    """
    out = {}
    _where_to_query(where, out)
    return out


def _where_to_query(where, out):
    if isinstance(where, Node_Op) and where.operator == "and":
        for sub in where.children:
            if not _where_to_query(sub, out):
                return False
        return True
    if isinstance(where, Node_Op) and where.operator in {"=", "<", ">", "<=", ">=", "<>", "!="}:
        upd = None
        if isinstance(where.children[0], Node_Field) and node_is_literal(where.children[1]):
            upd = COMPARISON_OPS[where.operator](where.children[0].fieldName[-1], where.children[1].eval(None))
        elif isinstance(where.children[1], Node_Field) and node_is_literal(where.children[0]):
            op = COMPARISON_OPPOSITE[where.operator]
            upd = COMPARISON_OPS[op](where.children[1].fieldName[-1], where.children[0].eval(None))
        if upd:
            if upd[0] in out and isinstance(out[upd[0]], dict) and isinstance(upd[1], dict):
                out[upd[0]].update(upd[1])
            else:
                out[upd[0]] = upd[1]
            return True
    # unsupported operation
    return False


COMPARISON_OPS = {
    "=": lambda f, v: (f, v),
    "<": lambda f, v: (f, {"$lt": v}),
    ">": lambda f, v: (f, {"$gt": v}),
    "<=": lambda f, v: (f, {"$lte": v}),
    ">=": lambda f, v: (f, {"$gte": v}),
    "!=": lambda f, v: (f, {"$ne": v}),
    "<>": lambda f, v: (f, {"$ne": v}),
}
COMPARISON_OPPOSITE = {"=": "=", "<": ">", ">": "<", "<=": ">=", ">=": "<=", "!=": "!=", "<>": "<>" }