import http.server
import socketserver
import os
import threading
import time
import urllib.parse
import mimetypes
import typing
import re
from collections import defaultdict

from miniapp import __version__ as miniapp_version
from miniapp.comm.request import MiniRequest
from miniapp.comm.session import SessionHandler
from miniapp.comm.session_activity import DistinctSessionTimeline
from miniapp.comm.utils import json_dumps, ChunkStreamWrapper, StreamFromChunks
from miniapp.errs import wrap_exception, ReportedException, InternalError
from miniapp.utils.file_utils import open_file_tweaked

MIME_JSON = "application/json"
PTN_ENCODED = r'%[0-9a-fA-F][0-9a-fA-F]'
DEFAULT_SESSION_COOKIE_NAME = "session"


class MiniHttp(object):
    """
    Base class for a very simple web server.
    """
    def __init__(self, port: int, logger=None, session_handler=None, host: str=None, handler_config=None, max_session_expire: int=24*3600):
        self.port = port
        self.host = host or ("0.0" + ".0.0")
        self.session_handler = session_handler or SessionHandler()
        self.logger = logger
        self.running = True
        self.started = False
        self._mode = "threads"
        self.handler_config = handler_config or HandlerConfig()
        self._server = None
        self.max_session_expire = max_session_expire
        # current request goes here, in current.request
        self.current = threading.local()
        # enables CSRF
        self.csrf = None
        # tracks session activity
        self.session_activity = None
        # name for session cookies
        self.session_cookie_name = DEFAULT_SESSION_COOKIE_NAME
        # header overrides - tuples of (regex, {name: value}, override)
        self._custom_headers = []

    def current_request(self):
        """
        The current request that is being processed.
        """
        if hasattr(self.current, "request"):
            return self.current.request

    def current_session(self):
        """
        Access to the session data for the current request that is being processed.
        """
        if hasattr(self.current, "request"):
            return self.current.request.session

    def track_session_activity(self, **kwargs):
        """
        Insert a session activity tracker.
        """
        # TODO this overlaps quite a bit with, and is inferior to, the 'user_activity' functionality
        #   - remove?
        self.session_activity = DistinctSessionTimeline(**kwargs)
        self.session_activity.inject_into_session_handler(self.session_handler)

    def active_users(self):
        """
        Report on recently active users.
        """
        by_user = defaultdict(list)
        for session in self.session_handler:
            last_activity = session.get("timestamp")
            if not last_activity:
                continue
            user_name = session.get("user_name") or ""
            by_user[user_name].append(last_activity)
        for user_name, user_activity in by_user.items():
            yield {
                "user_name": user_name,
                "last_activity": max(user_activity),
                "n_sessions": len(user_activity)
            }

    def add_custom_headers(self, path_pattern: (str, re.Pattern), headers: dict, override: bool = False) -> None:
        """
        Add HTTP headers for certain URLs.

        :param path_pattern: Which paths should receive the headers.
        :param headers:      HTTP headers to add to the response for these URLs.
        :param override:     False - if the generated response already contains a given header it will be kept,
                             True - headers will override headers in the generated response.
        """
        if not headers:
            return
        if isinstance(path_pattern, str):
            path_pattern = re.compile(path_pattern)
        self._custom_headers.append((path_pattern, headers, override))

    def _apply_custom_headers(self, path: str, headers: dict) -> None:
        """
        Add headers based on URL.  Adds headers for responses based on configuration supplied via
        self.add_custom_headers().

        :param path:        Path from request.
        :param headers:     Headers to modify.
        """
        for ptn, mods, override in self._custom_headers:
            if ptn.match(path):
                if override:
                    # all values in 'mods' replace values in 'headers'
                    headers.update(mods)
                else:
                    # don't overwrite any existing headers
                    headers.update({k: v for k, v in mods.items() if k not in headers})

    @staticmethod
    def send_file(filename, mime_type=None, delete_after_use=False, byte_range: list=None):
        """
        Generates a response containing the content of a given file.  Call from within a request handler, and return
        what it returns.

        :param filename:   File to send to client.
        :param delete_after_use: Deletes file afterward.
        :param byte_range: Optional range for what to send.
        :return:  A response to return from handle_get() or handle_post()
        """
        if not os.path.exists(filename):
            return
        mime_type = mime_type or mimetypes.guess_type(filename)[0] or "text/plain"
        stream = open_file_tweaked(filename, 'rb', delete_after_use=delete_after_use, byte_range=byte_range)
        return stream, mime_type

    def handle(self, method, request):
        """
        Derived classes fill in this method.  Return either:
          tuple(response, mime_type) -> custom response
          tuple(response, mime_type, headers) -> custom response with custom headers
          list, dict, set --> JSON response
          str --> UTF-8 encoded response
          bytes --> raw response
          None --> 404
        """

    def wrap_requests(self, wrapper: callable):
        """
        Cause all requests & responses to go through a given wrapper method.
        :param wrapper:     A method which is passed the original handle method.  See handle().
        """
        setattr(self, "handle", wrapper(self.handle))

    def _occasionally(self, context):
        """
        Background clean-up.
        """
        if "t_prev" not in context:
            context["t_prev"] = time.time()
        else:
            # NOTE: this logout has no effect in SSO mode because the next request through SSO just logs in again
            # - applications should call purge_old() themselves and cause their UIs to redirect to the SSO logout URL
            if time.time() - context["t_prev"] > self.max_session_expire/50:
                # do session clean-up in a background thread
                def run():
                    self.session_handler.purge_old(self.max_session_expire)
                threading.Thread(target=run, name="mini.web.background_clean").start()
                context["t_prev"] = time.time()

    def start(self, mode: str=None, wait_for_start=False, wait_for_shutdown=False, daemon_threads: bool=False):
        """
        Start up the web service.

        :param mode:        'threads' - each HTTP request is handled in a separate thread
                            'subprocesses' - each HTTP request is handled in a forked subprocess
                            'single_thread' - all HTTP requests are handled sequentially by one thread
        :param wait_for_start:  True: return after server starts up,
                                False: return immediately (unless wait_for_shutdown is selected).
        :param wait_for_shutdown: True: do not return until the server is stopped through a call to shutdown().
                                  False: return immediately (unless wait_for_start is selected).
        :param daemon_threads:  True: handler threads die immediately on server termination (server shuts down quickly),
                                False: handler threads are allowed to continue until they finish (server shuts down
                                  slowly).
                                This option applies only when mode=='threads'.
        """
        self._mode = mode or self._mode
        handler_class = self.handler_class_factory(self, logger=self.logger, config=self.handler_config)
        if self._mode == "threads":
            self._server = self.ThreadedHTTPServer((self.host, self.port), handler_class)
            # IMPORTANT: setting this to True (which is the default!) causes every thread for every request
            #  to be held in an array, creating a serious memory leak
            self._server.block_on_close = False
            self._server.daemon_threads = daemon_threads
        elif self._mode == "subprocesses":
            self._server = self.ForkingHTTPServer((self.host, self.port), handler_class)
        elif self._mode == "single_thread":
            self._server = http.server.HTTPServer((self.host, self.port), handler_class)
        else:
            raise InternalError(f"invalid mode: {self._mode}")
        def run():
            self.started = True
            context = {}
            while self.running:
                self._server.handle_request()
                self._occasionally(context)
            self._server.server_close()
            self._server = None

        if wait_for_shutdown:
            # run in foreground
            run()
        else:
            # run the background thread which runs the server, and if requested wait for it to begin
            thread = threading.Thread(target=run, name=f"http server port {self.port}")
            thread.daemon = True
            thread.start()
            if wait_for_start:
                self.wait_for_start()

    def wait_for_start(self, timeout_s=3):
        """
        Wait for the server to officially start running.
        """
        retry = 0
        while not self.started:
            time.sleep(0.1)
            retry += 1
            if retry == int(timeout_s*10):
                raise Exception("timeout")

    def wait_for_shutdown(self):
        """
        Wait until server shuts down.
        """
        while self._server:
            time.sleep(0.1)

    def _request_shutdown(self):
        """
        Request a shutdown.  See note.
        """
        self.running = False

    def _kill_subproceses(self):
        """
        When running in subprocess mode, a shutdown cannot occur until all child processes end.  This method forces
        them all to end.
        """
        if self._mode != "subprocesses":
            return
        try:
            import psutil
        except ImportError:
            return
        for child in psutil.Process().children(recursive=True):
            try:
                child.kill()
            except OSError:
                pass

    def shutdown(self, timeout_s=3, wait_for_shutdown: bool=True):
        """
        Shut down the server and wait for it to stop.

        :param timeout_s:               How long to wait for shutdown to complete.
        :param wait_for_shutdown:       Whether to wait for shutdown.
        """
        self._request_shutdown()
        self._kill_subproceses()
        if wait_for_shutdown:
            retry = 0
            while self._server:
                time.sleep(0.1)
                retry += 1
                if retry >= int(timeout_s*10):
                    # print(f"server({self.port}) shutdown timed out")
                    break

    class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
        """ Extends the base server to handle requests in separate threads. """

    class ForkingHTTPServer(socketserver.ForkingMixIn, http.server.HTTPServer):
        """ Extends the base server to handle requests in separate processes. """

    @staticmethod
    def handler_class_factory(server, logger=None, _wbufsize=None, config=None):
        """
        Build a Handler class for MiniHttp.
        """
        class Handler(HandlerBase):
            def __init__(self, *args, **kwargs):
                self._logger = logger
                self._server = server
                self._config = config or HandlerConfig()
                # this is only used to facilitate unit tests
                if _wbufsize:
                    self.wbufsize = _wbufsize
                super(Handler, self).__init__(*args, **kwargs)
        return Handler


class HandlerBase(http.server.BaseHTTPRequestHandler):
    """
    Translates HTTP requests into calls to MiniHTTP handlers.
    """
    protocol_version = "HTTP/1.1"
    def __init__(self, *args, **kwargs):
        super(HandlerBase, self).__init__(*args, **kwargs)
        if not hasattr(self, "_logger"):
            self._logger = None
        if not hasattr(self, "_server"):
            self._server = None
        if not hasattr(self, "_config"):
            self._config = HandlerConfig()

    def log_message(self, format, *args, _level=None, _detail=None):
        if self._logger:
            formatted = format % args if args else format
            if _level:
                return self._logger(formatted, level=_level, caller_detail=_detail)
            # add elapsed time since request was received
            if hasattr(self._server.current, "request"):
                request = self._server.current.request
                elapsed = " %.3f" % (time.time() - request.start_time)
            else:
                elapsed = " -"
            self._logger(formatted + elapsed, level="INFO", caller_detail=_detail)

    def _send_all_headers(self, headers):
        for k, v in headers.items():
            if isinstance(v, list):
                for v1 in v:
                    self.send_header(k, v1)
            else:
                self.send_header(k, v)

    def _send_response__response_object(self, resp):
        """
        Simplified path for responses of type Response
        """
        self.send_response(resp.status_code)
        self._server._apply_custom_headers(self.path, resp.headers)
        self._send_all_headers(resp.headers)
        if "Content-Length" not in resp.headers:
            self.send_header("Content-Length", len(resp.content))
        self.end_headers()
        content = resp.content
        if isinstance(content, str):
            content = content.encode("UTF-8")
        self.wfile.write(content)

    def version_string(self) -> str:
        return f"miniapp/{miniapp_version}"

    def _send_response(self, resp, response_code=200, request: MiniRequest=None):
        """
        Send all types of responses.
        """
        server = self._server
        if resp is None:
            self.send_error(404)
            return
        if resp.__class__.__name__ == "Response":
            self._send_response__response_object(resp)
            return
        mime_type = "text/plain"
        headers = {}
        if isinstance(resp, tuple):
            if len(resp) > 2:
                headers = resp[2] or {}
                if headers:
                    headers.pop("Content-Type", None)
                    headers.pop("Date", None)
                    headers.pop("Server", None)
            resp, mime_type = resp[:2]
        elif isinstance(resp, (list, dict, set)):
            mime_type = MIME_JSON
            resp = json_dumps(resp)
        elif not isinstance(resp, (str, bytes, bytearray)) and not hasattr(resp, "read") and isinstance(resp, typing.Iterable):
            mime_type = MIME_JSON
            resp = json_dumps(list(resp))
        # establish or update session id cookie
        sid_client = server.current.request.cookie(server.session_cookie_name)
        sid_server = server.current.request.session_id
        if sid_server and sid_server != sid_client:
            s_secure = "; Secure" if self._config.https_only else ""
            headers["Set-Cookie"] = [
                f"{server.session_cookie_name}={sid_server}; Path={path}; HttpOnly{s_secure}"
                for path in self._config.logged_in_paths
            ]
        # add configured headers
        server._apply_custom_headers(self.path, headers)
        # verify content type against accept header
        if request:
            if not request.accepts_content_type(mime_type):
                self.send_error(406)
                return
        # start sending response
        # NOTE: we are not calling self.send_response() here because it won't let the user override the 'Server' header
        # self.log_request(response_code)
        self.send_response_only(response_code, None)
        if "Server" not in headers:
            self.send_header('Server', self.version_string())
        self.send_header('Date', self.date_time_string())

        self.send_header("Content-type", mime_type)
        if isinstance(resp, str):
            resp = resp.encode("UTF-8")
        # streams
        if hasattr(resp, "read"):
            return self._send_stream(resp, headers)
        # force end with linefeed...
        # if resp and not resp.endswith(b"\n"):
        #     resp += b"\n"
        headers["Content-length"] = len(resp)
        self._send_all_headers(headers)
        self.end_headers()
        self.wfile.write(resp)

    def _send_stream(self, stream, headers):
        """
        Send a file-like object as a response.
        """
        chunked = False
        if stream.seekable():
            # known size
            stream.seek(0, 2)
            size = stream.tell()
            stream.seek(0)
            headers["Content-length"] = size
        else:
            # unknown size
            chunked = True
            headers["Transfer-Encoding"] = "chunked"
            headers.pop("Content-length", None)
        self._send_all_headers(headers)
        self.end_headers()
        while True:
            chunk = stream.read(400000)
            if not chunk:
                break
            if chunked:
                self.wfile.write(f"{hex(len(chunk))[2:]}\r\n".encode("utf-8"))
            self.wfile.write(chunk)
            if chunked:
                self.wfile.write(b'\r\n')
        if chunked:
            self.wfile.write(b'0\r\n\r\n')
        stream.close()

    @staticmethod
    def _need_to_log(exception):
        # unrecognized exception type
        if not hasattr(exception, "has_private_details"):
            return True
        # private details to report
        if exception.has_private_details():
            return True

    def do_POST(self):
        return self.do_all("post")

    def do_PUT(self):
        return self.do_all("put")

    def do_GET(self):
        return self.do_all("get")

    def do_DELETE(self):
        return self.do_all("delete")

    def do_HEAD(self):
        return self.do_all("head")

    def do_all(self, method):
        server = self._server
        # parse the request
        url_parts = urllib.parse.urlparse(self.path)
        attrs = urllib.parse.parse_qs(url_parts.query)
        length = int(self.headers.get('content-length') or 0)
        xfr_enc = self.headers.get("transfer-encoding") or ""
        rqline = self.requestline if hasattr(self, "requestline") else " "
        full_path = rqline.split(" ")[1]
        query_string = "?" + full_path.split("?", maxsplit=1)[1] if "?" in full_path else ""
        # values that go into every type of request
        rqst_props = {
            "method": method,
            "path": url_parts.path,
            "query_string": query_string,
            "args": attrs,
            "headers": self.headers,
            "client_address": self.client_address[0],
            "session_cookie_name": server.session_cookie_name if server else DEFAULT_SESSION_COOKIE_NAME
        }
        # where is our post data?
        if xfr_enc.lower() == "chunked":
            # chunked post data
            post_data = self._read_chunked()
            request = MiniRequest(server, post_data=post_data, **rqst_props)
        elif length and method in {"put", "post", "delete", "patch"}:
            # fixed-length post data
            if length > 80000:
                # turn post data into a reasonably functional stream if it's large-ish
                post_data = ChunkStreamWrapper(self.rfile, length), length
            else:
                # read post data fully if it's small-ish
                post_data = self.rfile.read(length)
            request = MiniRequest(server, post_data=post_data, **rqst_props)
        else:
            # no post data
            request = MiniRequest(server, **rqst_props)
            request.connection = self.connection if hasattr(self, "connection") else None
        # set the current request (server.current is a thread local)
        server.current.request = request
        try:
            # enforce CSRF
            if server.csrf and method in {"put", "post", "delete", "patch"}:
                server.csrf.verify_request(request)
            # handle the request
            resp = server.handle(method, request)
            resp_args = resp,
        except Exception as e:
            e = wrap_exception(e)
            if self._need_to_log(e):
                self.log_message(e.to_log(), _level="ERROR", _detail=f"API_ERROR:{request.path}")
            elif hasattr(e, "remove_tracking_code"):
                e.remove_tracking_code()
            resp_args = e.http_response()
        self._really_send_response(resp_args, request)

    def _read_chunked(self):
        """
        Read from a chunked response.  Converts the chunk sequence into a readable stream.
        """
        def iter_chunks():
            while True:
                buf = self.rfile.readline().strip()
                if not buf:
                    break
                length = int(buf, 16)
                if length <= 0:
                    break
                yield self.rfile.read(length)
                self.rfile.read(2)
        return StreamFromChunks(iter_chunks())

    def _really_send_response(self, resp_args, request=None):
        """
        Try to sent response.  There can often be encoding errors in the preparation of the response, so we try to send
        a simple error message in this case.  If the socket is closed or something serious like that this attempt
        will also fail.  In that final case we issue a log error.
        """
        try:
            self._send_response(*resp_args, request=request)
        except Exception as e:
            # try to log the error in detail
            if isinstance(e, BrokenPipeError):
                self.log_message(f"broken-pipe, url={self.path}", _level="WARN", _detail=f"WEB.SEND")
                return
            try:
                err = ReportedException(e)
                err.private_details["url"] = self.path
                self.log_message(err.to_log(), _level="ERROR", _detail=f"WEB.SEND")
            except:
                pass
            # failure during sending of response - send back generic error message
            try:
                self._send_response({"ok": False, "message": "unable to send response, see logs for details"}, request=request)
            except:
                pass


class HandlerConfig(object):
    def __init__(self, logged_in_paths: list=None, https_only: bool=True):
        self.logged_in_paths = logged_in_paths or ["/"]
        self.https_only = https_only
