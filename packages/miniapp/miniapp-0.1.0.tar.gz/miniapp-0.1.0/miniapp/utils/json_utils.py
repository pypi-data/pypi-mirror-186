import traceback
import math
import re
import jsonschema

from miniapp.utils.misc import format_iso_datetime, format_iso_date


def json_safe_value(value):
    """
    Cause a value to become JSON serializable.
    """
    xlt = _TO_SAFE_JSON.get(value.__class__.__name__)
    if xlt:
        return xlt(value)
    if isinstance(value, Exception):
        tb = traceback.extract_tb(value.__traceback__)
        tbf = traceback_to_json(tb)
        return {"exception": {"message": str(value), "traceback": tbf}}
    if hasattr(value, "as_datetime") and hasattr(value.as_datetime, "__call__"):
        return format_iso_datetime(value.as_datetime())
    if hasattr(value, "to_pydatetime") and hasattr(value.to_pydatetime, "__call__"):
        return format_iso_datetime(value.to_pydatetime())
    if hasattr(value, "_to_json") and hasattr(value._to_json, "__call__"):
        return value._to_json()
    raise Exception("Unsupported type: %s" % type(value))


def traceback_to_json(tb):
    """
    Turn a traceback or a stack trace into JSON.
    """
    stk = tb
    if tb.__class__.__name__ == "traceback":
        stk = traceback.extract_tb(tb)
    return [{"name": lvl.name, "filename": lvl.filename, "line": lvl.lineno} for lvl in stk]


class _JsonXPath(object):
    def __init__(self, data):
        self.data = data

    @staticmethod
    def type_for_index(index):
        return [] if isinstance(index, int) else {}

    def _into_list(self, index, create, get_type):
        if index < 0 or index >= len(self.data):
            if not create or not get_type:
                # index not found, and create not enabled
                return False
            self.data.insert(index, get_type())
        index = 0 if index < 0 else len(self.data) - 1
        self.data = self.data[index]
        return True

    def _into_dict(self, index, create, get_type):
        key = str(index)
        if key not in self.data:
            if not create or not get_type:
                # index not found, and create not enabled
                return False
            self.data[key] = get_type()
        self.data = self.data[key]
        return True

    def descend(self, index, create=None, get_type: callable=None):
        if isinstance(index, int) and isinstance(self.data, (list, tuple)):
            return self._into_list(index, create, get_type)
        if isinstance(self.data, dict):
            return self._into_dict(index, create, get_type)
        # reached a leaf node that can't be descended
        return False

    def descend_list(self, indexes, create=None):
        def get_type(pos):
            if pos < len(indexes):
                return self.type_for_index(indexes[pos])
            return (create or dict)()
        for n_index, index in enumerate(indexes):
            if not self.descend(index, create, lambda: get_type(n_index)):
                return
        return self.data


def json_xpath(data, xpath: list, create=None):
    """
    Dig into JSON data.
    :param data:   Data to explore.
    :param xpath:  An iterable of ints (for arrays) or strings (for dicts).
    :param create: Whether to create members as we go, and if so, default type for final member.
    :return:   Discovered value, or None.
    """
    return _JsonXPath(data).descend_list(xpath, create=create)


def json_dotted_write(data, key, value):
    """
    Write into JSON.
    :param data:   JSON to modify.
    :param key:    A string with dots separating each component.
    :param value:  Value to write.
    """
    parts = key.split(".")
    last = json_xpath(data, parts[:-1], create=dict)
    last[parts[-1]] = value


def gen_json_size_limiter(max_array=50, max_str=300):
    """
    Generate a method that will limit the size of JSON objects.
    :param max_array:   Maximum length for arrays.
    :param max_str:     Maximum length for strings.
    :return:    The size-limiting method.
    """
    def limit_size(node):
        if isinstance(node, (int, float, type(None).__class__)):
            return node
        if isinstance(node, (list, tuple, set)):
            if len(node) > max_array:
                node = node[:max_array] + ["..."]
            return [limit_size(sub) for sub in node]
        if isinstance(node, dict):
            return {k: limit_size(v) for k, v in node.items()}
        if isinstance(node, (bytes, bytearray)):
            node = node.decode("utf-8", errors="ignore")
        if isinstance(node, str) and len(node) > max_str:
            return node[:max_str] + "..."
        return node

    return limit_size


def repair_to_schema(data, schema: dict):
    """
    Try to make some data conform to a JSON schema.
    """
    repairs = False
    if not isinstance(data, dict) or schema.get("additionalProperties", True):
        return repairs
    # remove invalid fields
    invalid_fields = set()
    if "properties" in schema:
        allowed_fields = set(schema["properties"].keys())
        invalid_fields = set(data) - allowed_fields
    if "patternProperties" in schema:
        ptns = []
        for f in schema["patternProperties"]:
            ptns.append(re.compile(f))
        invalid_fields = set()
        for f in data:
            any_ptn_matches = any(ptn.match(f) is not None for ptn in ptns)
            if not any_ptn_matches:
                invalid_fields.add(f)
    if invalid_fields:
        repairs = True
        for f in invalid_fields:
            del data[f]
    return repairs


def merge_json_schemas(a: dict, b: dict):
    """
    Combine two sets of jsonschema validation rules.  It is assumed that 'b' is a newer set, and its properties
    will be preferred to 'a'.  In no case, however, will this logic (knowingly) allow 'b' to violate 'a'.  That is,
    the resulting validation is intended to be no less strict than either 'a' or 'b' on any point.
    """
    def c_default(x, y):
        return y
    def c_props(p1, p2):
        return {p: _mjs_combine(p1, p2, p, merge_json_schemas) for p in set(p1) | set(p2)}
    known = {
        "type": _mjs_types,
        "minimum": max,
        "maximum": min,
        "exclusiveMinimum": max,
        "exclusiveMaximum": min,
        "minItems": max,
        "maxItems": min,
        "properties": c_props,
        "additionalProperties": lambda v1, v2: v1 and v2,
        "items": merge_json_schemas,
        "uniqueItems": lambda v1, v2: v1 or v2,
        "required": lambda v1, v2: list(sorted(set(v1) | set(v2)))
    }
    out = {}
    for prop_name in set(a) | set(b):
        out[prop_name] = _mjs_combine(a, b, prop_name, known.get(prop_name, c_default))
    return out


def _mjs_types(t1, t2):
    t1s = {t1} if isinstance(t1, str) else set(t1)
    t2s = {t2} if isinstance(t2, str) else set(t2)
    if "integer" in t1s and "number" in t2s:
        t2s.remove("number")
        t2s.add("integer")
    if "integer" in t2s and "number" in t1s:
        t1s.remove("number")
        t1s.add("integer")
    t = t1s & t2s
    if not t:
        raise Exception("no overlap between types: %s and %s" % (t1, t2))
    return list(sorted(t)) if len(t) > 1 else list(t)[0]


def _mjs_combine(src1, src2, prop, combiner):
    if prop in src1 and prop not in src2:
        return src1[prop]
    if prop not in src1 and prop in src2:
        return src2[prop]
    if prop in src1 and prop in src2:
        return combiner(src1[prop], src2[prop])


def fast_json_schema_validation(data, schema: dict, ctx_d=None, ctx_s=None):
    """
    The jsonschema library has become intolerably slow.  Here's a fast alternative for simpler schemas.
    """
    def err(msg, lvl_d, lvl_s):
        raise jsonschema.ValidationError(
            msg,
            path=tuple((ctx_d or []) + ([lvl_d] if lvl_d else [])),
            schema_path=tuple((ctx_s or []) + [lvl_s])
        )
    def d_type():
        return data.__class__.__name__
    _vfy_types(schema, data, err)
    enum = schema.get("enum")
    if enum and data not in enum:
        err(f"expected one of {', '.join(map(str, enum))}", None, "enum")
    props = schema.get("properties")
    required = schema.get("required")
    if props or required:
        if not isinstance(data, dict):
            err(f"expected object, not {d_type()}", None, "properties" if props else "required")
        for name, spec in (props or {}).items():
            if name not in data:
                continue
            fast_json_schema_validation(data[name], spec, (ctx_d or []) + [name], (ctx_s or []) + ["properties", name])
        if required:
            missing = set(required) - set(data)
            if missing:
                err(f"missing required fields: {', '.join(missing)}", None, "required")
    if schema.get("additionalProperties") is False and isinstance(data, dict):
        extra = set(data) - set(schema.get("properties", {}))
        if extra:
            err(f"unrecognized fields: {', '.join(extra)}", None, "additionalProperties")
    _vfy_numeric(schema, data, err)
    items = schema.get("items")
    if items and isinstance(data, (list, tuple)):
        for idx, sub in enumerate(data):
            fast_json_schema_validation(sub, items, (ctx_d or []) + [idx], (ctx_s or []) + ["items"])
    x_ptn = schema.get("pattern")
    if x_ptn and not re.match(x_ptn, str(data)):
        err(f"does not match pattern '{x_ptn}'", None, "pattern")
    # TODO detect other features and fall back to jsonschema


def _vfy_types(schema, data, err):
    def d_type():
        return data.__class__.__name__
    x_type = schema.get("type")
    if x_type == "number" and not isinstance(data, (int, float)):
        err(f"expected number, not {d_type()}", None, "type")
    if x_type == "integer" and not isinstance(data, int):
        err(f"expected integer, not {d_type()}", None, "type")
    if x_type == "string" and not isinstance(data, str):
        err(f"expected string, not {d_type()}", None, "type")
    if x_type == "array" and not isinstance(data, (list, tuple)):
        err(f"expected array, not {d_type()}", None, "type")
    if x_type == "object" and not isinstance(data, dict):
        err(f"expected object, not {d_type()}", None, "type")


def _vfy_numeric(schema, data, err):
    x_min = schema.get("minimum")
    if x_min is not None and data < x_min:
        err(f"{data} is below minimum of {x_min}", None, "minimum")
    x_max = schema.get("maximum")
    if x_max is not None and data > x_max:
        err(f"{data} is above maximum of {x_max}", None, "maximum")



_TO_SAFE_JSON = {
    "tuple": lambda v: tuple(map(json_safe_value, v)),
    "set": lambda v: tuple(map(json_safe_value, v)),
    "list": lambda v: list(map(json_safe_value, v)),
    "dict": lambda v: {k: json_safe_value(v) for k, v in v.items()},
    "OrderedDict": lambda v: {k: json_safe_value(v) for k, v in v.items()},
    "datetime": format_iso_datetime,
    "date": format_iso_date,
    "Decimal": float,
    "bytes": lambda v: v.decode("iso-8859-1"),
    "bytearray": lambda v: v.decode("iso-8859-1"),
    "BytesIO": lambda v: v.getvalue().decode("iso-8859-1"),
    "int": lambda v: v,
    "str": lambda v: v,
    "bool": lambda v: v,
    "NoneType": lambda v: v,
    "float": lambda v: v if math.isfinite(v) else None,
    "int8": int,
    "int16": int,
    "int32": int,
    "int64": int,   # i.e. numpy int
    "Int64": int,   # i.e. bson.int64.Int64
    "float16": lambda v: float(v) if math.isfinite(v) else None,
    "float32": lambda v: float(v) if math.isfinite(v) else None,
    "float64": lambda v: float(v) if math.isfinite(v) else None,
    "NaTType": lambda v: None,
    "NAType": lambda v: None,
    "UUID": str,
}
