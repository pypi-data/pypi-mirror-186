import datetime
import time


def make_object(**kwargs):
    """
    Create an object with the given named fields.
    """
    strict = bool(kwargs.pop("__strict__", None))
    class GenericObject(object):
        def __getitem__(self, item):
            if strict:
                return kwargs[item]
            return kwargs.get(item)

        def __getattr__(self, item):
            if item == "__call__":
                raise AttributeError
            if strict:
                if item not in kwargs:
                    raise AttributeError
                return kwargs[item]
            return kwargs.get(item)

        def __dir__(self):
            return kwargs.keys()

        def __contains__(self, item):
            return item in kwargs

        def __repr__(self):
            return repr(kwargs)

        def __iter__(self):
            return iter(kwargs)

        def __bool__(self):
            return bool(kwargs)

        def _to_json(self):
            """ Convert back to a dict. """
            return dict(kwargs)

        def _extend(self, params):
            """ Add more properties. """
            kwargs.update(params)
            return self

        def _plus(self, updates):
            """ Return a modified version. """
            out = dict(kwargs)
            out.update(updates)
            return make_object(**out)

    return GenericObject()


def make_object_from_json(data, strict: bool=False, rename=None):
    """
    Convert JSON data into an object.
    :param data:    []s and {}s
    :param strict:  False = generated object tolerates misspelled keys, returning None, True = KeyError in those cases.
    :param rename:  A method that will rename object keys.
    """
    rename = rename or (lambda x: x)
    if isinstance(data, (list, tuple)):
        return [make_object_from_json(elem, strict=strict, rename=rename) for elem in data]
    if isinstance(data, dict):
        return make_object(**{rename(k): make_object_from_json(v, strict=strict, rename=rename) for k, v in data.items()}, __strict__=strict)
    return data


def jsonify_object(node, depth: int=16):
    """
    The reverse of make_object_from_json().
    """
    if depth <= 0:
        raise Exception(f"jsonify_object(): internal error, depth exceeded")
    if isinstance(node, (str, int, float, bool, type(None))):
        return node
    if isinstance(node, dict):
        return {k: jsonify_object(v, depth-1) for k, v in node.items()}
    if isinstance(node, (list, tuple, set)):
        return [jsonify_object(v, depth-1) for v in node]
    if isinstance(node, datetime.datetime):
        # special case: timestamps from yaml become ISO datetime strings
        return time.strftime("%Y-%m-%dT%H:%M:%SZ", node.timetuple())
    # objects
    obj = {}
    for attr in dir(node):
        v = getattr(node, attr)
        if not attr.startswith("_") and not hasattr(v, "__call__"):
            obj[attr] = jsonify_object(v, depth-1)
    return obj
