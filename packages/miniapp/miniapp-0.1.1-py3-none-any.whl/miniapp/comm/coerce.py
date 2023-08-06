"""
Conversion of HTTP arguments into python method arguments.
"""
import json

from miniapp.errs import BadRequest

STR_TO_BOOL = {"false": False, "true": True, "0": False, "1": True}


def coerce_param_to_annotation(query_args: dict, arg_name: str, annotation):
    """
    Convert a parsed HTTP GET or POST argument value into a value suitable for a parameter to a method.  The
    target type is given by 'annotation', as defined by type hints in the method declaration.

    If my method is declared like this:
      def f(x: int)

    Then 'annotation' will be <int>.

    If the value from the query string was ["7"] we would convert that into an int, i.e. int("7").

    :param query_args:      Set of arguments.
    :param arg_name:        Name of argument.
    :param annotation:      The annotation value from inspect.Parameter.annotation, i.e. a type.
    :return:   Modified value.
    """
    if arg_name not in query_args:
        return
    value_list = query_args[arg_name]
    if isinstance(value_list, str):
        str_v = value_list
    else:
        str_v = value_list[0] if len(value_list) == 1 else None
    # list types
    if annotation in {list, set, tuple}:
        return _param_to_list(str_v, value_list, annotation, arg_name)
    # dict
    if annotation is dict:
        return _param_to_dict(str_v, arg_name)
    # compound type
    if isinstance(annotation, tuple):
        return _param_to_compound(str_v, annotation, arg_name)
    # convert values
    if annotation in {bool, int, float}:
        if str_v is not None:
            str_v = STR_TO_BOOL.get(str_v.lower(), str_v)
            return annotation(str_v)
        value_list = list(map(annotation, value_list))
    # fall back to string or list of strings
    if str_v is not None:
        return str_v
    return value_list


def _safe_json_loads(str_v, arg_name: str = None, expect=None):
    try:
        out = json.loads(str_v)
        if expect and not isinstance(out, expect):
            raise BadRequest(message="invalid type for %s, expected %s" % (arg_name, expect))
        return out
    except ValueError as err:
        raise BadRequest(
            code="invalid-argument-format", message="expected json for %s" % arg_name,
            public_details={"arg_name": arg_name, "error": str(err)}
        )


def _param_to_list(str_v, value_list, annotation, arg_name):
    if str_v and str_v.startswith("["):
        # parse JSON string
        return annotation(_safe_json_loads(str_v, arg_name))
    elif not value_list or value_list == [""]:
        # blank
        return annotation()
    else:
        # fall back to string array, i.e. "url?a=1&a=2&a=3" --> ["1","2","3"]
        if isinstance(value_list, str):
            value_list = [value_list]
        return annotation(value_list)


def _param_to_dict(str_v, arg_name):
    if not str_v:
        return {}
    else:
        return _safe_json_loads(str_v, arg_name, expect=dict)


def _param_to_compound(str_v, annotation, arg_name):
    # bool allowed, check for distinctly bool-like values
    if bool in annotation:
        if not str_v:
            return False
        if str_v.lower() in STR_TO_BOOL:
            return STR_TO_BOOL[str_v.lower()]
    # convert from JSON string
    try:
        if list in annotation and (not str_v or str_v.startswith("[")):
            return _safe_json_loads(str_v or '[]', arg_name)
        elif dict in annotation and (not str_v or str_v.startswith("{")):
            return _safe_json_loads(str_v or '{}', arg_name)
    except BadRequest:
        if str in annotation:
            return str_v
        raise
    # string and byte types allowed?
    # int allowed and present?
    if int in annotation and str_v.isdigit():
        return int(str_v)
    elif str in annotation:
        return str_v
    elif bytes in annotation:
        return str_v.encode("utf-8")
    # JSON required?
    elif list in annotation or dict in annotation:
        raise BadRequest(code="invalid-argument-format", message="expected json for %s" % arg_name,
                         public_details={"arg_name": arg_name})
