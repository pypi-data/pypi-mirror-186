"""
Binding to handler methods.
"""
import re
import inspect
import urllib.parse

from miniapp.comm.coerce import coerce_param_to_annotation
from miniapp.errs import GeneralError, Unauthorized401, AccessDenied403
from miniapp.utils.file_utils import open_file_tweaked
from miniapp.utils.misc import quote_once

REGEX_PATH_ARG = r'([^/]*)'
REGEX_PATH_ARG_WILDCARD = r'(.*?)'


def create_endpoint_decorator(permission_checker=None):
    """
    Generates a decorator for endpoints.  Usage (without permission checking):

        endpoint = create_endpoint_decorator()

        class MyCategory(object):
            @endpoint(method="get", path="my_entrypoint")
            def my_entrypoint(self, x: int=0):
                return {"ok": True, "x": x}

    :param permission_checker:  A function that checks permissions.  The first argument is the instance of the
        API category class and the second is the data about the required permission.  If it returns True,
        permission is granted.  False or None deny access.  None implies a non-logged in state, whereas False
        implies permission is not allowed to the current user.
    """

    class Endpoint(object):
        def __init__(
                self, method: (str, tuple, list)="get", path: str="",
                subdomain: str="", permission_required=None,
                response_type: str="json", sequence=None,
                update_session_timer: bool=True, post_data_as_stream: bool=False, raw_paths: bool=False,
                activity_analysis=None,
        ):
            """
            Create an endpoint decorator.

            :param method:   Which HTTP method(s) to support.
            :param path:     Path to capture, with {name} for path arguments and {name:*} for multi-path args.  Note
                             that there should be no initial '/' in this path.
            :param subdomain: Regex string to match on the host name, if this entrypoint should only be used in
                             certain subdomains.
            :param permission_required:   Permission identifier to pass to the supplied permission_checker.
            :param response_type:  Data type of HTTP response, i.e. 'json'.
            :param sequence:        Determines sequence of presentation, i.e. in Swagger, JSON.
            :param update_session_timer:    False means this endpoint does not count as an activity which would
                                reset the timeout for the current session.
            :param post_data_as_stream: When True, the 'post_data' value is supplied as a stream, not a 'bytes'.
            :param raw_paths:   When False (the default), arguments in paths are unquoted.  When True they are
                                passed through unchanged.
            :param activity_analysis:  Specifies how to log user activity.  This can be False, which inhibits such
                                reporting altogether, "*" which records all parameters, an iterable, which records just
                                certain parameters, or a function which returns the information to log.  See
                                capture_user_activity for more information.
            """
            self.method = method.lower() if isinstance(method, str) else [m.lower() for m in method]
            self.path = path
            self.permission_required = permission_required
            self.subdomain = subdomain
            self.response_type = response_type
            self.sequence = sequence
            self.update_session_timer = update_session_timer
            self.activity_analysis = activity_analysis
            self.post_data_as_stream = post_data_as_stream
            self.raw_paths = raw_paths
            self.enabled = True

        def __call__(self, f):
            def f_w(*args, **kwargs):
                if self.permission_required and permission_checker:
                    allowed = permission_checker(args[0], self.permission_required)
                    if allowed is None:
                        raise Unauthorized401()
                    if not allowed:
                        raise AccessDenied403(
                            private_details={
                                "required-permission": self.permission_required[0]
                            }
                        )
                    if isinstance(allowed, str):
                        raise AccessDenied403(
                            public_details={
                                "reason": allowed
                            }
                        )
                    if isinstance(allowed, dict):
                        raise AccessDenied403(
                            **allowed
                        )
                return f(*args, **kwargs)

            f_w.__name__ = f.__name__
            f_w.__doc__ = f.__doc__
            f_w.endpoint = self
            f_w.original = f
            return f_w

    return Endpoint


class CallSpec(object):
    """
    Details about a given API call.
    """
    def __init__(self, base_path, fn_path, handler_inst=None, handler_fn=None, title=None, response_type="json", post_data_as_stream=False, raw_paths=False):
        self.title = title
        self.base_url = "/" + base_path.strip("/")
        self.rel_url = fn_path.strip("/")
        all_parts = [self.base_url[1:]] if len(self.base_url) > 1 else []
        if self.rel_url:
            all_parts.append(self.rel_url)
        self.full_url = "/" + "/".join(all_parts)
        self.handler_inst = handler_inst
        self.handler_fn = handler_fn
        self.doc = doc_split(inspect.getdoc(handler_fn) or "")
        original = handler_fn.original if hasattr(handler_fn, "original") else handler_fn
        self.params = inspect.signature(original).parameters
        self.response_type = response_type
        self.post_data_as_stream = post_data_as_stream
        self.raw_paths = raw_paths

    def as_json(self, var_props: dict=None, include_docs: bool=True):
        def param_json(param):
            out = {"name": param.name, "type": _annot_to_str(param.annotation)}
            if var_props and param.name in var_props:
                out.update(var_props[param.name])
            if param.default is not inspect.Parameter.empty:
                out["default"] = param.default
            return out
        if hasattr(self.handler_inst, "category_name"):
            category = self.handler_inst.category_name()
        else:
            category = self.handler_inst.__class__.__name__.lower() if self.handler_inst else None
        return {
            "title": self.title,
            "url": self.full_url,
            "category": category,
            "description": self.doc if include_docs else ("", {}),
            "parameters": [
                param_json(param)
                for param in self.params.values()
                if param.name not in {"self", "request"} and not param.name.startswith("_")
                   and param.kind not in {inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL}
            ],
            "response": self.response_type
        }


class HandlerInfo(object):
    """
    Metadata about the MiniREST handler.
    """
    def __init__(self, path_regex, var_names: list=None, subdomain_regex=None, handler_fn=None, spec: CallSpec=None,
                 rewrite=None, rewrite_server=None, sequence=None, methods=None, update_session_timer=True):
        self.path_regex = path_regex
        self.var_names = var_names or []
        self.subdomain_regex = subdomain_regex
        self.handler_fn = handler_fn
        self.spec = spec
        self.rewrite = rewrite
        self.rewrite_server = rewrite_server
        self.sequence = sequence
        self.update_session_timer = update_session_timer
        self.activity_analysis = None
        self.methods = methods

    def __str__(self):
        return str(self.path_regex) + "->" + str(self.handler_fn)

    def sort_key(self):
        """
        Determine sort order.
        """
        subdomains_first = 1 if self.subdomain_regex is None else 0
        path_str = str(self.path_regex)
        specific_paths_first = -len(path_str.split('/'))
        return subdomains_first, specific_paths_first, len(path_str)

    def check_match(self, path: str, host: str):
        """
        Check for a match on path and host.
        :return:   The regex match object with matched path-based attributes, or None.
        """
        path_match = self.path_regex.match(path)
        #print("%d %20s %s" % (bool(path_match), path, self.path_regex))
        subdomain_ok = self.subdomain_regex.match(host) is not None if self.subdomain_regex else True
        if not subdomain_ok:
            return None
        return path_match

    def conflicts_with(self, other):
        if self.subdomain_regex != other.subdomain_regex:
            return False
        PATH_ARG = '__PATH_ARG__'
        PATH_ALL = '__PATH_ALL__'
        def normalize(regex):
            ptn = regex.pattern
            ptn = ptn.replace(REGEX_PATH_ARG, PATH_ARG)
            ptn = ptn.replace(REGEX_PATH_ARG_WILDCARD, PATH_ALL)
            ptn = re.sub(r'\(.*?\)\??', '', ptn)
            return ptn.strip('/').split('/')
        r1 = normalize(self.path_regex)
        r2 = normalize(other.path_regex)
        while r1 and r2:
            p1 = r1.pop(0)
            p2 = r2.pop(0)
            # if first case is more specific than the second, there is possibility of overlap, but it is allowed
            if p1 != PATH_ARG and p1 != PATH_ALL and p2 in (PATH_ARG, PATH_ALL):
                return False
            # trailing wildcard
            if p1 == PATH_ALL or p2 == PATH_ALL:
                return True
            # any constant section that is different
            if p1 != PATH_ARG and p2 != PATH_ARG and p1 != p2:
                return False
        if r1 or r2:
            return False
        return True

    @staticmethod
    def detect_conflict(handlers, category):
        """
        Detect overlapping path specifications
        :param handlers:
        """
        for n in range(len(handlers) - 1):
            if handlers[n].conflicts_with(handlers[n+1]):
                raise Exception(f"{category}: conflicting paths: {handlers[n].path_regex.pattern} and {handlers[n+1].path_regex.pattern}")

    def spec_json(self, include_docs: bool=True):
        return self.spec.as_json({name: {"qualifier": qual} for name, qual in self.var_names}, include_docs=include_docs)

    def args_from_request(self, request, matched_paths, post_data_as_stream=False, raw_paths=False):
        """
        Extract arguments for a handler from a request.
        :param request:         Request from client.
        :param matched_paths:   Path-based argument values: result of a regex match on the path.
        :return:        A {} of argument name to argument value.
        """
        # extract arguments first from query/post arguments
        use_kwargs = {k: v if len(v) > 1 else v[0] for k, v in request.args.items()}
        # extract path-based arguments
        for n_var, (var_name, var_qualifier) in enumerate(self.var_names):
            path_value = matched_paths.group(n_var + 1)
            if raw_paths:
                path_value = quote_once(path_value)
            else:
                path_value = urllib.parse.unquote(path_value) if var_qualifier == "*" \
                    else urllib.parse.unquote_plus(path_value)
            use_kwargs[var_name] = path_value
        use_kwargs = self._special_args(use_kwargs, request, post_data_as_stream=post_data_as_stream)
        # flag for internal use - no access to this flag through REST
        use_kwargs.pop("_internal", None)
        return use_kwargs

    def _special_args(self, use_kwargs, request, post_data_as_stream: bool=False):
        if self.spec:
            params = self.spec.params
        else:
            params = inspect.signature(self.handler_fn).parameters
        # ignore unrecognized arguments
        if "kwargs" not in params:
            use_kwargs = {k: v for k, v in use_kwargs.items() if k in params}
        # adjust argument types
        for param in params.values():
            if param.name in use_kwargs:
                use_kwargs[param.name] = coerce_param_to_annotation(use_kwargs, param.name, param.annotation)
        if "request" in params:
            use_kwargs["request"] = request
        # FIXME hardcoded name is bad, add something to the decorator
        if "post_data" in params:
            if post_data_as_stream:
                stream_h, stream_len = request.post_stream
                use_kwargs["post_data"] = open_file_tweaked(stream_h, mode='rb', byte_range=[0, stream_len] if stream_len is not None else None)
            else:
                raw = request.post_data
                if "www-form-urlencoded" in request.headers.get("Content-Type", ""):
                    raw = _from_urlencoded(raw)
                use_kwargs["post_data"] = raw
        if "self" in use_kwargs:
            del use_kwargs["self"]
        return use_kwargs


class _DocSplitter(object):
    """
    Analysis of inspect-ed code documentation.
    """
    def __init__(self):
        self.main = []
        self.bits = {"parameters": [], "raises": [], "keywords": []}

    def handle_param(self, m):
        param_name = m.group(3)
        param_descr = m.group(4)
        params = self.bits["parameters"]
        if param_name:
            params.append([param_name, param_descr or ""])

            def _more(v):
                params[-1][1] += "\n" + v

            return _more

    def handle_raises(self, m):
        param_name = m.group(3)
        param_descr = m.group(4)
        excepts = self.bits["raises"]
        if param_name:
            excepts.append([param_name, param_descr or ""])

            def _more(v):
                excepts[-1][1] += "\n" + v

            return _more

    def handle_keywords(self, param):
        keywords = self.bits["keywords"]
        if param:
            keywords.append(param)

    def split(self, doc: str):
        simplify = {
            "parameter": "param", "argument": "param", "arg": "param", "var": "param",
            "raise": "raises", "except": "raises", "exception": "raises",
            "return": "returns",
            "key": "keywords", "keyword": "keywords"
        }
        PTN = re.compile(
            "^:(param|parameter|raise|raises|rtype|returns|return|arg|argument|cvar|except|exception|ivar|key|keyword|type|var)(\s+([A-Za-z0-9_]+):\s*(.*)|.+)?$")
        more = None
        for line in doc.split("\n"):
            line = line.strip()
            m = PTN.match(line)
            if m is None:
                if more:
                    more(line)
                else:
                    self.main.append(line)
                continue
            more = None
            marker = simplify.get(m.group(1), m.group(1))
            param = (m.group(2) or "").strip(" \t:")
            if marker == "param":
                more = self.handle_param(m) or more
            elif marker == "raises":
                more = self.handle_raises(m) or more
            elif marker == "keywords":
                self.handle_keywords(param)
            elif param:
                self.bits[marker] = param

                def _more(v):
                    self.bits[marker] += "\n" + v

                more = _more
        return "\n".join(self.main).strip(), self.bits


def doc_split(doc: str):
    """
    Split a function/class document string into named parts.
    :returns:  A tuple with the main document string, and a {} with...
      * 'parameters' - an array with pairs of name and documentation
      * 'raises' - an array with pairs of name and documentation
      * 'keywords' - an array with a list of keywords
      * 'returns' - return value
      * 'cvar', 'ivar', 'type', ...
    """
    return _DocSplitter().split(doc)


def parse_path_spec(path_spec):
    """
    A path_spec is a specification for a URL with embedded parameters.  Like...

    leading_path/{named_path}/another_path/{trailing_path:*}

    :returns:   A tuple with a compiled regex to match the path, and a list of parameter names associated with each
        matched group.  Ex.  path/{var}  -->  r'path/[^/]+', [("var", "")].
        The param_names array (2nd element of returned tuple) consists of a variable name and any type-specifier string
        appended to it, i.e. "*".
    """
    m_valid = re.match(r'[^{}]*(({([a-z_][a-z0-9_]*)(:\*)?\})[^{}]*)*$', path_spec)
    if m_valid is None:
        raise GeneralError(code="invalid-path", message=f"invalid path: {path_spec}",
                           public_details={"path": path_spec})
    regex_out = "^%s$" % path_spec
    param_names = []
    for param_spec in re.finditer(r'{([^:}]+)(:([^}]*))?\}', path_spec):
        whole_spec = param_spec.group(0)
        param_name = param_spec.group(1)
        qualifiers = param_spec.group(3)
        before = path_spec[:param_spec.start()]
        regex_part = REGEX_PATH_ARG_WILDCARD if qualifiers == '*' else REGEX_PATH_ARG
        if qualifiers == '*' and before.endswith("/"):
            regex_out = regex_out.replace("/" + whole_spec, "(?:$|/)" + regex_part)
        else:
            regex_out = regex_out.replace(whole_spec, regex_part)
        param_names.append((param_name, qualifiers or ""))
    return re.compile(regex_out), param_names


def _annot_to_str(a):
    if a is inspect.Parameter.empty:
        return None
    if hasattr(a, "__name__"):
        return a.__name__
    if isinstance(a, tuple):
        if a in ((list, tuple), (list, set), (list, set, tuple)):
            return "list"
        return ", ".join(map(_annot_to_str, a))
    return str(a)


def _from_urlencoded(raw):
    if isinstance(raw, bytes):
        raw = raw.decode("utf-8")
    if raw:
        raw = urllib.parse.unquote(raw)
    return raw

