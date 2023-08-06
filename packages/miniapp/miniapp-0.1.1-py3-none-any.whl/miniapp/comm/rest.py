import os
import time
import re
from collections import defaultdict
import traceback

from miniapp.comm.binding import HandlerInfo, CallSpec, parse_path_spec
from miniapp.comm.http import MiniHttp
from miniapp.comm.request import MiniRequest, Response
from miniapp.comm.swagger import ApiSwagger
from miniapp.utils.generic_obj import make_object

ALL_METHODS = ("get", "post", "put", "delete", "head")
PTN_METHOD_NAME = re.compile(r'(get|post|put|delete|head)_(.*)')
DEFAULT_FORCE_SESSION_FLUSH = 15


class MiniREST(MiniHttp):
    """
    A very simple REST server, built on top of MiniHttp.
    """
    def __init__(self, *args, **kwargs):
        super(MiniREST, self).__init__(*args, **kwargs)
        self.handlers = defaultdict(list)
        # you can plug in a monitor here
        self.monitor = None
        # sessions are not written immediately when the only thing that changed was 'time of last activity'
        #  - the default makes sure we update the time of last activity at least once a minute
        self.force_session_flush = DEFAULT_FORCE_SESSION_FLUSH

    def _sort_handlers(self):
        """
        Put handlers in order from most specific to least.
        """
        for method in self.handlers:
            hh = self.handlers[method] = sorted(self.handlers[method], key=HandlerInfo.sort_key)
            # detect duplicate/ambiguous mappings
            HandlerInfo.detect_conflict(hh, method)

    def add_category(self, base_path, handler_inst):
        """
        Add a set of REST methods from a class.  Every method tagged with the endpoint decorator
        (see create_endpoint_decorator) will be connected as a REST endpoint.

        :param base_path:      The base path for the set of API calls, i.e. "/api/v1/somecalls".
        :param handler_inst:   The class which will be inspected, and whose methods will be called.
        """
        base_path = base_path.strip("/")
        for fn in dir(handler_inst):
            fn_callable = getattr(handler_inst, fn)
            if hasattr(fn_callable, "endpoint"):
                endpoint = fn_callable.endpoint
                if not endpoint.enabled:
                    continue
                method = endpoint.method
                path = endpoint.path.strip("/")
                methods = [method] if isinstance(method, str) else method
                full_path = base_path + ("/" if base_path and path else "") + path
                regex, var_names = parse_path_spec(full_path)
                subdomain_regex = re.compile(endpoint.subdomain) if endpoint.subdomain else None
                spec = CallSpec(
                    base_path, path, handler_inst=handler_inst, handler_fn=fn_callable, title=fn,
                    response_type=endpoint.response_type, post_data_as_stream=endpoint.post_data_as_stream,
                    raw_paths=endpoint.raw_paths
                )
                h_i = HandlerInfo(
                    path_regex=regex, var_names=var_names, subdomain_regex=subdomain_regex,
                    handler_fn=fn_callable, spec=spec, sequence=endpoint.sequence, methods=methods
                )
                h_i.update_session_timer = endpoint.update_session_timer
                h_i.activity_analysis = endpoint.activity_analysis
                for m in methods:
                    self.handlers[m].append(h_i)
        self._sort_handlers()

    def add_static_folder(self, base_path, content_folder: (str, list, tuple)):
        """
        Add a static folder from which normal web content is served.
        :param base_path:       Root path that browser will request.
        :param content_folder:  Folder where content to serve is located.
        """
        folder_list = [content_folder] if isinstance(content_folder, str) else content_folder
        def handler(rel_path, **kwargs):
            for folder in folder_list:
                file_to_send = os.path.join(folder, rel_path)
                if os.path.exists(file_to_send) and not os.path.isdir(file_to_send):
                    return self.send_file(file_to_send)
        path = base_path.strip("/")
        path_spec = path + ("/" if path else "") + "{rel_path:*}"
        regex, var_names = parse_path_spec(path_spec)
        h_i = HandlerInfo(
            path_regex=regex, var_names=var_names, handler_fn=handler, methods=["get"], update_session_timer=False
        )
        self.handlers["get"].append(h_i)
        self._sort_handlers()

    def add_path_handler(self, path, handler, verb="get"):
        """
        Handle a specific path with a specific handler.
        :param path:        Path that browser will request.
        :param handler:     Method which produces response.
        :param verb:        Which HTTP method to respond to.
        """
        regex, var_names = parse_path_spec(path)
        h_i = HandlerInfo(path_regex=regex, var_names=var_names, handler_fn=handler, methods=[verb])
        self.handlers[verb].append(h_i)
        self._sort_handlers()

    def add_redirect(self, path_in: (str, re.Pattern), path_out: str):
        """
        Redirect a specific path.
        :param path_in:    Incoming path.  A string or a compiled regex.
        :param path_out:   Redirected path.
        """
        if not path_out.startswith("/"):
            path_out = "/" + path_out
        def handler(**kwargs):
            return Response(status_code=302, headers={"Location": path_out})
        if hasattr(path_in, "match"):
            regex, var_names = path_in, []
        else:
            regex, var_names = parse_path_spec(path_in.strip("/"))
        h_i = HandlerInfo(path_regex=regex, var_names=var_names, handler_fn=handler)
        self.handlers["get"].append(h_i)
        self._sort_handlers()

    def add_rewrite(self, path_in, path_out, to_server=None):
        """
        Rewrite a specific path.
        :param path_in:    Incoming path.  A string or a compiled regex.
        :param path_out:   Rewritten path.  Or a method that takes arguments (request) and returns a request.
        :param to_server:  Rewrite can send request to a different Server instance.
        """
        if isinstance(path_out, str) and not path_out.startswith("/"):
            path_out = "/" + path_out
        if hasattr(path_in, "match"):
            regex, var_names = path_in, []
        else:
            regex, var_names = parse_path_spec(path_in.strip("/"))
        h_i = HandlerInfo(path_regex=regex, var_names=var_names, rewrite=path_out, rewrite_server=to_server)
        for method in ALL_METHODS:
            self.handlers[method].append(h_i)
        self._sort_handlers()

    def add_proxy(self, path_in, path_out: (str, callable)):
        """
        Proxy calls to (path_in) to (path_out)
        :param path_in:     A path specification like "/root/{path:*}", or a compiled regex.
        :param path_out:    A format string including host and path, like "HOST/abc/{path}", or a function
                            that generates a URL from a request.
        """
        from miniapp.comm.proxy import proxy_request
        def handler(request, **kwargs):
            if isinstance(path_out, str):
                url = path_out.format(**kwargs) + request.query_string
            else:
                url = path_out(request)
            if not url:
                return
            return proxy_request(request, url)
        if hasattr(path_in, "match"):
            regex, var_names = path_in, []
        else:
            regex, var_names = parse_path_spec(path_in.strip("/"))
        h_i = HandlerInfo(path_regex=regex, var_names=var_names, handler_fn=handler, spec=None)
        self.handlers["get"].append(h_i)
        self.handlers["post"].append(h_i)
        self.handlers["put"].append(h_i)
        self.handlers["delete"].append(h_i)
        self._sort_handlers()

    def handle(self, method, request):
        """
        Calls appropriate handler.
        """
        t_session_stale = time.time() - self.force_session_flush
        path = request.path.strip("/")
        h_i = None
        use_kwargs = None
        out = None
        for h_i in self.handlers[method]:
            path_match = h_i.check_match(path, request.host)
            if path_match is None:
                continue
            if h_i.rewrite:
                rewrite_to = h_i.rewrite
                rewrite_server = h_i.rewrite_server or self
                if hasattr(rewrite_to, "__call__"):
                    rq2 = rewrite_to(request)
                else:
                    rq2 = MiniRequest(request.server, rewrite_to, args=request.args, headers=request.headers, post_data=request.post_data)
                # NOTE: we have to set the current request for rewrite_server since we are bypassing do_all()
                #   where this normally happens
                rewrite_server.current.request = rq2
                return rewrite_server.handle(method, rq2)
            use_kwargs = h_i.args_from_request(
                request, path_match, post_data_as_stream=h_i.spec.post_data_as_stream if h_i.spec else False,
                raw_paths=h_i.spec.raw_paths if h_i.spec else False
            )
            out = h_i.handler_fn(**use_kwargs)
            if out is None:
                continue
        # inform monitor
        if self.monitor and h_i:
            try:
                self.monitor(method=method, request=request, function=h_i.handler_fn, kwargs=use_kwargs, output=out)
            except Exception as err:
                tb = traceback.format_exc()
                # don't let internal errors in monitor break api calls
                print("API_MONITOR_ERROR url=%s, error=%s, trace=%s" % (request.path, err, tb))
        # force session to update
        if h_i and h_i.update_session_timer:
            # this request is meant to update the session timestamp
            if not request.session.timestamp or request.session.timestamp < t_session_stale:
                # session timestamp is not set, or is older than the staleness threshold
                request.session._flush()
        # handle possible return values
        return self._transform_handler_response(out)

    @staticmethod
    def _transform_handler_response(out):
        """
        Initial simplification of responses.  Converts everything vaguely object-like into a {}.
        """
        if out is not None and out.__class__.__name__ == "GenericObject":
            # object-dict wrapper
            return out._to_json()
        elif out and out.__class__.__name__ == "Response":
            return out
        elif hasattr(out, "read"):
            # a stream
            return out
        elif out is not None and not isinstance(out, (list, tuple, dict, set, str, bytes, bytearray)) and hasattr(out, "__dict__"):
            # object with attributes
            return out.__dict__
        else:
            # dict, etc.
            return out

    @staticmethod
    def handler_requires_authentication(handler_fn):
        if hasattr(handler_fn, "endpoint"):
            return handler_fn.endpoint.permission_required

    def describe_api(self, include_docs: bool=True, enable_authenticated_calls: bool=True):
        """
        Return JSON describing all REST methods.  Call this from an API handler to make a self-describing API.
        """
        gen = ApiSwagger(self, include_docs=include_docs, enable_authenticated_calls=enable_authenticated_calls)
        return gen.describe_api()

    def describe_api_swagger(self, title: str, server_url: str, include_docs: bool=True, enable_authenticated_calls: bool=True):
        """
        A Swagger description of the API.
        """
        gen = ApiSwagger(self, title=title, server_url=server_url, include_docs=include_docs, enable_authenticated_calls=enable_authenticated_calls)
        return gen.describe_api_swagger()

    @staticmethod
    def response(**kwargs):
        """
        Generate a response object with named fields.
        """
        return make_object(**kwargs)

