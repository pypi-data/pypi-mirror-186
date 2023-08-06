"""
In-memory implementations and helpers.
"""
import copy
import uuid
from collections import defaultdict

from .const import *
from .db import SimplestDb, FieldList
from ..errs import InternalError


class InMemoryDb(SimplestDb):
    """
    An in-memory database that fully implements 'SimplestDb', but happens not to be persistent.
    """
    def __init__(self):
        self.data = defaultdict(dict)
        self.files = {}

    def query(self, collection, query=None, fields=None, sort=None, limit=None, _raw: bool=False):
        query = self._to_query_obj(query)
        fields = self._to_field_selector(fields)
        coll = self.data[collection]
        if not query and fields is None and not sort and not limit:
            return map(dict, coll.values())
        if not query:
            out = coll.values()
        elif list(query.keys()) == [ROW_ID]:
            match = coll.get(query[ROW_ID])
            out = [match] if match else []
        else:
            compiled_filter = compile_query(query)
            out = filter(compiled_filter, coll.values())
        return apply_sort_fields_limit(out, sort=sort, fields=None if _raw else fields if fields is not None else {}, limit=limit)

    def insert(self, collection, doc):
        self._assert_valid_for_storage(doc)
        doc = copy.deepcopy(doc)
        return self._insert(collection, doc)

    def _insert(self, collection, doc):
        row_id = doc.get(ROW_ID)
        if row_id in (None, ""):
            row_id = doc[ROW_ID] = str(uuid.uuid4())
        coll = self.data[collection]
        coll[row_id] = doc
        return row_id

    def update(self, collection, what_to_update, changes: dict, upsert=False):
        self._assert_valid_for_storage(changes)
        query = self._to_query_obj(what_to_update)
        found_any = False
        for rec in self.query(collection, query, _raw=True):
            found_any = True
            apply_update(rec, changes)
        if upsert and not found_any:
            rec = {}
            if what_to_update and not isinstance(what_to_update, dict):
                rec[ROW_ID] = what_to_update
            apply_update(rec, changes)
            self._insert(collection, rec)

    def replace(self, collection, id_to_replace, new_doc):
        self._assert_valid_for_storage(new_doc)
        if UPDATE_SET in new_doc or UPDATE_PUSH in new_doc or UPDATE_INC in new_doc:
            raise Exception("$ keys not supported here")
        new_doc = copy.deepcopy(new_doc)
        new_doc[ROW_ID] = id_to_replace
        coll = self.data[collection]
        old_doc = coll.get(id_to_replace, {})
        apply_update(old_doc, new_doc)
        coll[id_to_replace] = old_doc

    def delete(self, collection, what_to_delete):
        coll = self.data[collection]
        query = self._to_query_obj(what_to_delete)
        if isinstance(what_to_delete, str):
            coll.pop(what_to_delete, None)
        else:
            compiled_filter = compile_query(query)
            rows_to_delete = [row_id for row_id, row in coll.items() if compiled_filter(row)]
            for row_id in rows_to_delete:
                coll.pop(row_id, None)

    def drop_collection(self, collection: str):
        self.data.pop(collection, None)

    def purge(self):
        """
        Completely erase all data.
        """
        self.data.clear()


def compile_query(query: dict):
    """
    Compile a query into a form that can be quickly evaluated.  The query must only make use of the supported features.
    
    Examples:
        {"field1": {QUERY_LT: 100}}   =  field1 < 100
        {"x": 1, "y": 2}           =  x=1 and y=2
    """
    if not query:
        return lambda record: True
    tests = _compile_query_level(query)
    def check(record):
        for test in tests:
            if not test(record):
                return False
        return True
    if len(tests) == 1:
        return tests[0]
    return check


def match_query(query, value):
    """
    Test whether a given 'value' matches the supplied 'query'.  This method currently compiles the query in order to
    evaluate it, so if more than one value will be tested it is much more efficient to use compile_query() instead.

    :param query:    A {} with the search criteria.
    :param value:    A {} with record values to test.
    :return:         True if matched, False if not matched.
    """
    if not query:
        return True
    return compile_query(query)(value)


def _do_lt(a, b):
    if a is None:
        return False
    if b is None:
        return False
    return a < b


def _do_gt(a, b):
    if a is None:
        return False
    if b is None:
        return False
    return a > b


def _do_lte(a, b):
    if a is None:
        return b is None
    if b is None:
        return False
    return a <= b


def _do_gte(a, b):
    if a is None:
        return b is None
    if b is None:
        return False
    return a >= b


def _do_ne(a, b):
    if a is None:
        return b is not None
    return a != b


def _do_in(a, b):
    return a in b


def _list_eq(a, b):
    """
    List-like equality operator: true if any element of a matches any element in b.
    """
    if isinstance(a, list):
        if isinstance(b, list):
            return bool(set(a) & set(b))
        return b in a
    if isinstance(b, list):
        return a in b
    return a == b


def _wrap(fn, key, rhv):
    if "." in key:
        def test_dotted_field(record):
            v_g, _, _ = _json_find_using_dotted_notation(record, key)
            vl = v_g() if v_g else None
            return fn(vl, rhv)
        return test_dotted_field
    def test_field(record):
        return fn(record.get(key), rhv)
    return test_field


def _wrap_eq(key, rhv):
    if "." in key:
        def eq_dotted_field(record):
            v_g, _, _ = _json_find_using_dotted_notation(record, key)
            vl = v_g() if v_g else None
            return _list_eq(vl, rhv)
        return eq_dotted_field
    def eq_field(record):
        return _list_eq(record.get(key), rhv)
    return eq_field


def _wrap_exists(key, rhv):
    positive = bool(rhv)
    if "." in key:
        def test_dotted_field(record):
            v_g, _, _ = _json_find_using_dotted_notation(record, key, if_exists=True)
            return bool(v_g) == positive
        return test_dotted_field
    def test_field(record):
        return (key in record) == positive
    return test_field


def _make_or(or_list):
    def do_or(value):
        for test in or_list:
            if test(value):
                return True
        return False
    return do_or


def _make_not(tests):
    def fn(record):
        return any(not test(record) for test in tests)
    return fn


FILTER_FUNCTIONS = {
    QUERY_LT: _do_lt, QUERY_GT: _do_gt, QUERY_LE: _do_lte, QUERY_GE: _do_gte,
    QUERY_NE: _do_ne,
    QUERY_IN: _do_in
}


def _compile_query_level(query: dict):
    tests = []
    for k, v in query.items():
        if k.startswith("$"):
            if k == QUERY_AND:
                for sub in v:
                    tests += _compile_query_level(sub)
                continue
            if k == QUERY_OR:
                or_list = []
                for sub in v:
                    or_list += _compile_query_level(sub)
                tests.append(_make_or(or_list))
                continue
            if k == QUERY_NOT:
                sub = _compile_query_level(v)
                tests.append(_make_not(sub))
                continue
            raise InternalError(f"Invalid query operator: {k}")
        if not isinstance(v, dict) or not any(v_k.startswith("$") for v_k in v.keys()):
            # 'v' is data for an equality test
            tests.append(_wrap_eq(k, v))
            continue
        # 'v' is a set of tests
        for op, op_v in v.items():
            if op == QUERY_EXISTS:
                tests.append(_wrap_exists(k, op_v))
                continue
            op_fn = FILTER_FUNCTIONS.get(op)
            if not op_fn:
                raise InternalError(f"internal error: unrecognized query filter {op}")
            tests.append(_wrap(op_fn, k, op_v))
    return tests


def find_all_referenced_fields_in_query(query: dict) -> list:
    """
    Find all the fields referenced by a given query.
    """
    out = []
    if not query:
        return out
    for k, v in query.items():
        if not k.startswith("$"):
            out.append(k)
            continue
        if k in (QUERY_AND, QUERY_OR):
            for sub in v:
                out += find_all_referenced_fields_in_query(sub)
        if k == QUERY_NOT:
            out += find_all_referenced_fields_in_query(v)
    return out


def modify_field_list(fields=None, exclude=None, include=None):
    """
    Modify or generate a field list.

    :param fields:      Existing field list to modify, or None to create a new one.
    :param exclude:     List (or iterable) of fields to exclude.
    :param include:     List (or iterable) of fields to include.
    """
    if fields is None:
        if exclude:
            fields = {}
        else:
            fields = []
    if exclude:
        if isinstance(fields, list):
            fields = list(filter(lambda f: f not in exclude, fields))
        elif isinstance(fields, dict):
            if all(fields.values()):
                fields = [f for f in fields if f not in exclude]
            else:
                fields = {**fields, **{f: 0 for f in exclude}}
        if not fields:
            fields = {f: 0 for f in exclude}
    if include:
        if isinstance(fields, list):
            fields = list(set(fields) | set(include))
        elif isinstance(fields, dict):
            if all(fields.values()):
                fields = list(set(fields) | set(include))
            else:
                fields = {**fields, **{f: 0 for f in set(fields) - set(include)}}
    return fields


def _apply_push(rec: dict, changes: dict):
    for k, v in changes.items():
        v_g, v_s, _ = _json_find_using_dotted_notation(rec, k, create=True)
        if not v_g:
            raise Exception(f"No path to '{k}', cannot append")
        v0 = v_g()
        if not isinstance(v0, (type(None), list)):
            raise Exception("Cannot append to type %s" % type(v0))
        if isinstance(v, dict) and "$each" in v:
            v1 = (v0 or []) + v["$each"]
            sort = v.get("$sort")
            if sort:
                v1 = apply_sort_fields_limit(v1, sort=sort)
            slice = v.get("$slice")
            if slice:
                if slice > 0:
                    v1 = v1[:slice]
                elif slice < 0:
                    v1 = v1[slice:]
            v_s(v1)
        elif v0 is None:
            v_s([v])
        else:
            v0.append(v)


def _apply_inc(rec: dict, changes: dict):
    for k, v in changes.items():
        v_g, v_s, _ = _json_find_using_dotted_notation(rec, k, create=True)
        if not v_g:
            raise Exception(f"No path to '{k}', cannot increment")
        elif v_g() is None:
            v_s(v)
        else:
            v0 = v_g()
            if isinstance(v0, (int, float, bool)):
                v_s(v0 + v)
            else:
                raise Exception("Cannot increment type %s" % type(v0))


def _apply_set(rec: dict, changes: dict):
    for k, v in changes.items():
        v_g, v_s, _ = _json_find_using_dotted_notation(rec, k, create=True)
        if v_s:
            v_s(v)


def _apply_unset(rec: dict, changes: dict):
    for k, v in changes.items():
        _, _, v_d = _json_find_using_dotted_notation(rec, k, create=True)
        if v_d:
            v_d()


def apply_update(rec: dict, changes: dict):
    """
    Apply an update.  The fields in 'changes' can use dotted notation.
    :param rec:     Record to modify.
    :param changes:  A {} mapping strings which identify fields to update, in dot notation, to values to update/append.
    """
    do_set = True
    if UPDATE_PUSH in changes:
        _apply_push(rec, changes[UPDATE_PUSH])
        do_set = False
    if UPDATE_SET in changes:
        _apply_set(rec, changes[UPDATE_SET])
        do_set = False
    if UPDATE_UNSET in changes:
        _apply_unset(rec, changes[UPDATE_UNSET])
        do_set = False
    if UPDATE_INC in changes:
        _apply_inc(rec, changes[UPDATE_INC])
        do_set = False
    if do_set:
        _apply_set(rec, changes)
    else:
        if any(not k.startswith("$") for k in changes):
            raise ValueError(f"Invalid update request, mixed $ with non-$ keys ({', '.join(changes.keys())})")


def prepend_update(update: dict, field: str):
    """
    Given a set of updates to make to a field within a document, and the name of the field, cause those changes to
    be modified such that they can be applied at the document level.  That is, given the update {"x": 2}, for instance,
    and a record {"a": {"x": 1}}, where I want to update the field 'a', the update would become
    {"$set": {"a": {"x": 2}}}.
    """
    # simple overwrite of the whole field
    if not any(k.startswith("$") for k in update):
        return {UPDATE_SET: {field: update}}
    # directives
    out = {}
    prefix = field + "."
    for cmd, fields in update.items():
        # targets of all directives are in the form {field: something} -- prefix field names
        if cmd.startswith("$") and isinstance(fields, dict):
            out[cmd] = {prefix + fk: fv for fk, fv in fields.items()}
    return out


def add_to_update_operation(update: dict, k, v):
    """
    Amend an update operation to set a given value.  If an update uses '$' operations we can't just store 'k' and 'v'
    normally, we have to work them in around the previously established operations.

    For instance:
      {"$set": {"x": 1}} - if we also want to set 'y', we have to amend the '$set' operation.
    """
    keys = list(update)
    if not keys or not keys[0].startswith("$"):
        update[k] = v
        return update
    if UPDATE_SET in update:
        update[UPDATE_SET][k] = v
        return update
    if UPDATE_UNSET in update:
        update[UPDATE_UNSET].pop(k, None)
    update[UPDATE_SET] = {k: v}
    return update


def combine_filters_and(*args):
    """
    Combine all supplied filters with a logical AND.
    """
    if not args:
        return {}
    out = dict(args[0])
    for f in args[1:]:
        if not f:
            continue
        for k, v in f.items():
            if k not in out:
                out[k] = v
            elif QUERY_AND in out:
                out[QUERY_AND].append({k: v})
            else:
                out[QUERY_AND] = [{k: out.pop(k)}, {k: v}]
    return out


def _json_find_using_dotted_notation(data, spec, create=False, if_exists: bool=False):
    """
    Find a value within JSON data, using "dotted string notation" as per MongoDB.  In order to support internal
    manipulation of data structures with fields containing ".", the alternate separator "//" can be used.

    :param data:        JSON data in which to store a new value.
    :param spec:        A string with '.' separating
    :param create:      True to create structure as needed.
    :param if_exists:   Only return a getter if the field exists.
    :returns:   A tuple with a getter, a setter, and a deleter.  All will be None if the path cannot be reached.
    """
    def list_part(data_in, part):
        i_part = int(part)
        if 0 <= i_part < len(data_in):
            return data_in[i_part]
        # NOTE: creation not supported yet
    if "//" in spec:
        sep = "//"
    else:
        sep = "."
    spec_parts = spec.split(sep)
    for n, part in enumerate(spec_parts[:-1]):
        if isinstance(data, dict):
            data = _json_dict_part(data, part, spec_parts[n+1], create)
            if data is None:
                return None, None, None
        elif isinstance(data, list):
            data = list_part(data, part)
            if data is None:
                return None, None, None
    # last path component
    part = spec_parts[-1]
    if isinstance(data, dict):
        if if_exists and part not in data:
            return None, None, None
        return lambda: data.get(part), lambda v: data.__setitem__(part, v), lambda: data.__delitem__(part) if part in data else None
    elif isinstance(data, list):
        n_p = int(part)
        if if_exists and (n_p < 0 or n_p >= len(data)):
            return None, None, None
        return lambda: data[n_p], lambda v: data.__setitem__(n_p, v), lambda: data.__delitem__(n_p)
    return None, None, None


def _json_dict_part(data_in, part, next_part, create):
    def type_for_part(part):
        return [] if part.isdigit() else {}
    if part in data_in:
        data_next = data_in[part]
        if create and not hasattr(data_next, "__getitem__"):
            data_next = data_in[part] = type_for_part(next_part)
        return data_next
    elif create:
        data_in[part] = type_for_part(next_part)
        return data_in[part]


def apply_sort_fields_limit(records, sort=None, limit=None, fields=None):
    """
    Apply sorting, a restricted field list, row limit.
    :param records:     Enumeration of {}s to apply these features to.
    :param sort:        Mongoish sort order.
    :param limit:       Maximum  number of rows.
    :param fields:      Fields to include.
    :return:        Enumeration of {}s with decorations applied.
    """
    out = records
    if sort:
        # NOTE: full sort options not supported wrt 'descending'
        def key(r):
            return tuple(r.get(f) for f, o in sort)
        rev = sort[0][1] < 0
        out = sorted(out, key=key, reverse=rev)
    if limit:
        out = list(out)[:limit]
    if fields is not None:
        field_filt = FieldList(fields)
        out = map(field_filt.filter, out)
    return out
