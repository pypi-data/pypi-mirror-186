import io
import re
import uuid
import time
import urllib.parse

from miniapp.comm.session import SessionDict
from miniapp.utils.misc import is_uuid


class MiniRequest(object):
    """
    Description of a request, passed into the REST API handlers.
    """

    def __init__(self, server, path, query_string: str=None, args=None, headers=None, post_data=None, method: str = None, session=None,
                 session_id: str = None, session_cookie_name: str=None, client_address: str=None):
        """
        :param server:      The server that received the request.
        :param path:        Path not including query string.
        :param args:        'get' parameters (from the query string)
        :param headers:     Incoming HTTP headers.
        :param post_data:   Either raw data (bytes, bytearray, str), or a tuple of (stream, length).
        :param method:      Request method.
        :param session:     A dict-like session variable storage object.
        :param session_id:  Identifier for sessions - comes from a cookie if not supplied.
        """
        self.server = server
        self.method = method
        self.path = path
        self.args = args or {}
        self.headers = MiniHeaders(headers)
        self._post_data = post_data
        self._session_cookie_name = session_cookie_name or "session"
        # query string
        self.query_string = query_string or ''
        # requested host, not including port
        self.host = self.headers.get("Host", "").split(":")[0]
        # underlying socket
        self.connection = None
        # check for url-encoded arguments
        content_type = self.headers.get("Content-Type") or ""
        if post_data and "form-urlencoded" in content_type:
            try:
                post_str = self.post_data.decode("utf-8")
                self.args.update(parse_post_data(post_str))
            except:
                # ignore failure here, just don't collect posted args
                pass
        # client IP
        self.client_address = client_address
        # session ID
        if session_id:
            # caller-supplied override
            self.session_id = session_id
        else:
            # session ID from cookie
            self.session_id = self.cookie(self._session_cookie_name)
            # must be a valid UUID
            if self.session_id and not is_uuid(self.session_id):
                self.session_id = None
        # session variables are here
        if session:
            # caller-provided override
            self.session = session
        elif server:
            # fetch old session; will be None if no session exists with this ID
            ssn = server.session_handler.load_session(self.session_id)
            # if supplied session ID doesn't match a real session we ignore it
            # - if this is an expired session this gives us distinct IDs for each 'time-bounded-sequence' of
            #   user interactions, which is a good thing
            # - this blocks forged session IDs
            # - see DSW-3533
            if not ssn:
                self.session_id = None
            self.session = SessionDict(ssn)
            # changes to session data get written immediately
            # NOTE: sessions only get written when and if something changes, so merely pinging the site
            #  will not store a new session
            if server.session_handler:
                def update_session(upd):
                    if not self.session_id:
                        self.session_id = str(uuid.uuid4())
                    server.session_handler.save_session(self.session_id, upd)

                self.session._writer = update_session
        else:
            # blank session - no server
            self.session = SessionDict()
        # time request was received
        self.start_time = time.time()
        # custom properties for application use
        self.state = {}

    @property
    def post_data(self):
        """
        Access to POSTed data in its entirety.  Usually bytes, may sometimes be a str.
        """
        if isinstance(self._post_data, tuple):
            self._post_data = self._post_data[0].read(self._post_data[1])
        return self._post_data

    @property
    def post_stream(self):
        """
        Access to POSTed data as a stream.  A tuple with the stream, and the length of the data.
        """
        if isinstance(self._post_data, tuple):
            return self._post_data
        if isinstance(self._post_data, bytes) or not self._post_data:
            return io.BytesIO(self._post_data or b''), len(self._post_data or b'')
        if hasattr(self._post_data, "read"):
            return self._post_data, None
        return io.StringIO(self._post_data), len(self._post_data)

    def cookie(self, name):
        """ Get the value of a named cookie. """
        for kv in self.headers.get("cookie", self.headers.get("Cookie", "")).split('; '):
            if kv:
                k, v = kv.split('=', 1)
                if k == name:
                    return v

    def accepts_content_type(self, content_type: str):
        """
        Check a proposed response content type against this request's 'Accept' header.
        """
        if not content_type:
            return True
        accept = self.headers.get("Accept", self.headers.get("accept"))
        if not accept:
            return True
        if ";" in content_type:
            content_type = content_type.split(";")[0]
        accept = accept.lower()
        content_type = content_type.lower()
        for accept_part in re.split(r'\s*,\s*', accept):
            if ";" in accept_part:
                accept_part = accept_part.split(";")[0]
            if accept_part == "*/*":
                return True
            if accept_part.startswith("*/"):
                if "/" not in content_type:
                    return False
                return content_type.split("/")[1] == accept_part[2:]
            if accept_part.endswith("/*"):
                return content_type.split("/")[0] == accept_part[:-2]
            if content_type == accept_part:
                return True
        return False


class Response(object):
    """
    Use this object (or the object of the same name from http.server) for control over details of the
    response.
    """

    def __init__(self, status_code=200, headers=None, content=""):
        self.status_code = status_code
        self.headers = headers or {}
        self.content = content

    @staticmethod
    def file_head_response(size: int = None, modified: int = None, **kwargs):
        """
        Generate a response for a HEAD request seeking a file's properties.
        """
        headers = {}
        if size is not None:
            headers["Content-Length"] = str(size)
        if modified:
            headers["Last-Modified"] = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(modified))
        return Response(status_code=200, headers=headers)


def parse_post_data(post_data):
    """
    Extract arguments from url-encoded form POST data.
    :param post_data:
    :return:   A {} of named arguments.
    """
    return urllib.parse.parse_qs(post_data)


class MiniHeaders(object):
    """
    Storage of HTTP headers, with case-insensitive lookup.
    """

    def __init__(self, initial=None):
        self._values = {k: v for k, v in initial.items()} if initial else {}

    def __getitem__(self, key: str):
        v = self.get(key)
        if v is None:
            return ""
        return v

    def __setitem__(self, key, value):
        if key:
            self._values[key] = value

    def keys(self):
        return self._values.keys()

    def get(self, key: str, dflt=None):
        if not key:
            return dflt
        k_l = key.lower()
        for k, v in self._values.items():
            if k.lower() == k_l:
                return v
        return dflt

    def items(self):
        return self._values.items()

    def pop(self, key, dflt=None):
        self._values.pop(key, dflt)

    def __contains__(self, key):
        if not key:
            return False
        k_l = key.lower()
        for k, v in self._values.items():
            if k.lower() == k_l:
                return True
        return False
