"""
Client access to DSW service APIs.
"""
import requests
import json
import urllib.parse
import re
import time
import traceback

from miniapp.comm.utils import StreamFromChunks


def build_api(base_url: str, use_session: bool=False, timeout: float=None, csrf: bool=False, login: tuple=None, error_class=None, response_wrapper=None, bearer_token: str=None, conn_args: dict=None):
    """
    Generate an API class to handle the methods at the given URL.

    :param base_url:        URL, or host name where the REST endpoints are to be found.  If you specify a hostname,
                            "http://" will be prefixed because the assumption is that Kubernetes is protecting the
                            communication.  Prefix with "https://" when this is not the case.
    :param use_session:     True to maintain a dedicated HTTP session using requests.session().METHODS, False to use
                            requests.METHODS.
    :param timeout:         Timeout value (connection timeout) for communicating with the endpoints.
    :param csrf:            Whether CSRF is required by the API.
    :param login:           A set of credentials to apply when access to a full API requires a prior login.
    :param error_class:     Alternate exception class.
    :param response_wrapper: Library responses of type 'dict' can be wrapped with this method, i.e. to create synthetic
                            objects, etc..
    """
    error_class = error_class or _DefaultError
    if "://" not in base_url:
        base_url = "http://" + base_url
    if base_url.endswith("/"):
        base_url = base_url[:-1]
    api_url = base_url+"/api/v1"
    session = requests.session() if use_session else requests
    headers = {}
    conn_args = conn_args or {}
    def session_get(url, headers=None):
        try:
            resp = session.get(url, headers=headers, **conn_args)
            resp.raise_for_status()
            return resp
        except Exception as err:
            raise error_class(
                code="api-comm-failure", message="Communication error with microservice API", public_details={
                    "system": base_url
                }, private_details={
                    "method": "get",
                    "url": base_url,
                    "error": str(err),
                    "trace": traceback.format_stack()
                }
            )
    if bearer_token:
        headers["Authorization"] = f"Bearer {bearer_token}"
    resp = session_get(api_url, headers)
    spec = resp.json()
    intf_options = dict(
        session=session, timeout=timeout, csrf=csrf, error_class=error_class, response_wrapper=response_wrapper,
        conn_args=conn_args
    )
    api = ApiClient(spec, base_url, **intf_options)
    api._add_headers.update(headers)
    # credentials provided > log in
    if login:
        if not hasattr(api, "user") or not hasattr(api.user, "login"):
            raise error_class(code="invalid-api-spec", message="Invalid API spec, no user.login() method")
        api.user.login(*login)
        # logging in enables more endpoints so we have to fetch the spec again
        spec = session_get(api_url).json()
        api = ApiClient(spec, base_url, **intf_options)
    return api


class ApiClient(object):
    """
    This class turns itself into a mirror image of the remote services's API, with all of its endpoints grouped into
    named objects, all the calls filled in, and so on.
    """
    def __init__(self, spec, base_url, session, timeout: float=None, csrf: bool=True, error_class=None, response_wrapper=None, conn_args: dict=None):
        """
        :param spec:        The JSON specification for the API, as retrieved from the API self-description call.
        :param base_url:    Protocol, hostname and port where the remote service can be reached.  Paths to particular
                            endpoints will be appended to this.
        :param session:     A requests.session() instance to use.  If not given, separate sessions are used for each
                            call.
        :param timeout:     Connection timeout.
        :param csrf:        True to enable CSRF.
        """
        if "api" not in spec or "system" not in spec or not isinstance(spec["api"], list):
            raise Exception(f"invalid API spec: {json.dumps(spec)[:120]}...")
        self._extra = {}
        if timeout:
            self._extra["timeout"] = (timeout, 60)
        if conn_args:
            self._extra.update(conn_args)
        self._system = spec.get("system", "")
        self._base_url = base_url
        self._session = session
        self._special_timeouts = {"/api/v1/ping": 15}
        self._error_class = error_class or _DefaultError
        self._response_wrapper = response_wrapper
        self._add_headers = {}
        for call_info in spec["api"]:
            group, calls = call_info[:2]
            grp_calls = {call["title"]: self._build(call) for call in calls}
            setattr(self, group, self._build_group("call_group_%s" % group, grp_calls))
        self._csrf = None
        self._csrf_refresh = None
        if csrf:
            self._csrf = ""

    def _build_group(self, name, calls):
        class Group(object):
            def __init__(self):
                for k, v in calls.items():
                    setattr(self, k, v)
        Group.__name__ = name
        return Group()

    def _get_csrf(self):
        t_now = time.time()
        if self._csrf is None:
            return
        if not self._csrf or t_now > self._csrf_refresh:
            if hasattr(self, "general"):
                csrf_resp = self.general.csrf()
                self._csrf = csrf_resp.get("csrf_token") if isinstance(csrf_resp, dict) else csrf_resp.csrf_token
            self._csrf_refresh = t_now + 3600
        return self._csrf

    @staticmethod
    def _add_post_data(params: dict, post_data):
        """
        Add "post_data" to request parameters.
        """
        if post_data:
            if isinstance(post_data, (dict, list, tuple, set)):
                # json-like data gets transferred as JSON
                params["json"] = post_data
            else:
                # otherwise assume it is raw data
                if "headers" in params:
                    headers = params["headers"]
                else:
                    headers = params["headers"] = {}
                headers["Content-Type"] = "application/octet-stream"
                params["data"] = post_data

    def _normalize_params(self, params: dict, method: str, url: str):
        out = {}
        for k, v in params.items():
            if isinstance(v, set):
                v = list(v)
            if isinstance(v, (dict, list, tuple)):
                v = json.dumps(v)
            out[k] = v
        enable_csrf = method != "get" and not url.endswith("/csrf")
        if self._csrf is not None and enable_csrf:
            out["csrf_token"] = self._get_csrf()
        return out

    def _call(self, method: str, url: str, params: dict, stream: bool=False):
        params = self._normalize_params(params, method, url)
        use_url = self._base_url + self._fill_in_url(params, url)
        extra = dict(self._extra)
        if stream:
            extra["stream"] = True
        if url in self._special_timeouts:
            extra["timeout"] = self._special_timeouts[url]
        headers = params.pop("_headers", None)
        if self._add_headers:
            headers = dict(headers or {})
            headers.update(self._add_headers)
        if headers:
            extra["headers"] = headers
        try:
            if method == "get":
                resp = self._session.get(use_url, params=params, **extra)
            elif method == "post":
                post_data = params.pop("post_data", None)
                self._add_post_data(extra, post_data)
                if post_data is None:
                    extra["data"] = params
                else:
                    extra["params"] = params
                resp = self._session.post(use_url, **extra)
            elif method == "put":
                post_data = params.pop("post_data", None)
                self._add_post_data(extra, post_data)
                resp = self._session.put(use_url, params=params, **extra)
            elif method == "delete":
                resp = self._session.delete(use_url, params=params, **extra)
            else:
                resp = self._session.request(method, use_url, params=params, **extra)
        except Exception as err:
            raise self._error_class(
                code=f"api-comm-failure.{err.__class__.__name__}", message="Communication error with microservice API", public_details={
                    "system": self._system
                }, private_details={
                    "method": method,
                    "url": use_url,
                    "error": str(err),
                    "trace": traceback.format_tb(err.__traceback__)
                }
            )
        return use_url, resp

    def _handle_error(self, resp, title: str, url: str):
        if 500 <= resp.status_code <= 599 or resp.status_code in {400, 401}:
            try:
                out = resp.json()
            except:
                resp.raise_for_status()
                raise
            out.pop("ok", None)
            code = out.pop("code", "")
            msg = out.pop("message", "")
            trk = out.pop("_", "")
            raise self._error_class(
                code=code, message=msg, public_details=out, tracking_code=trk,
                private_details={"method": title, "url": url}
            )

    def _build(self, call):
        def generated_fn(*args, **kwargs):
            # convert positional arguments to named arguments
            params = call["parameters"]
            response_type = call.get("response", "json")
            for n_arg, arg_value in enumerate(args):
                if n_arg < len(params):
                    kwargs[params[n_arg]["name"]] = arg_value
            url, resp = self._call(call["method"], call["url"], params=kwargs)
            if resp.status_code == 403 and self._csrf is not None:
                self._csrf_refresh = time.time() - 1
                url, resp = self._call(call["method"], call["url"], params=kwargs, stream=response_type == "raw")
            if call["title"] == "login" and "session" in resp.cookies:
                self._extra["cookies"] = {"session": resp.cookies["session"]}
            self._handle_error(resp, title=call["title"], url=url)
            if response_type == "json":
                out = self._process_json_response(resp, url, name=call["title"])
            else:
                if resp.status_code == 404:
                    return
                resp.raise_for_status()
                pass_through_headers = {k: v for k, v in resp.headers.items() if k.lower() not in {"set-cookie", "content-type"}}
                if response_type == "raw":
                    # streaming download
                    size_hdr = resp.headers.get("Content-length")
                    if size_hdr and not resp.raw.seekable():
                        # size is known - make stream seekable so that content-length is preserved
                        content = StreamFromChunks(resp.iter_content(chunk_size=400000), size=int(size_hdr))
                    else:
                        # pass through the response's stream
                        content = resp.raw
                else:
                    # immediate download
                    content = resp.content
                out = content, resp.headers['content-type'], pass_through_headers
            return out
        return generated_fn

    @staticmethod
    def _fill_in_url(kwargs, url):
        """
        Fill path arguments into the URL we're going to call.
        :param kwargs:          The full set of arguments we're passing.  On return the path arguments will be removed.
        :param url:             The template for the URL to call.
        :return:                The patched URL.
        """
        for k in list(kwargs.keys()):
            repl = "{%s}" % k
            val = str(ApiClient._arg_val(kwargs[k]) or "")
            if repl in url:
                url = url.replace(repl, urllib.parse.quote_plus(val)).replace("+", "%20")
                del kwargs[k]
            else:
                repl = "{%s:*}" % k
                if repl in url:
                    url = url.replace(repl, urllib.parse.quote(val))
                    del kwargs[k]
        # remove any unused template arguments
        url = PTN_ARG.sub('', url)
        return url

    @staticmethod
    def _arg_val(v):
        if isinstance(v, (list, set, tuple, dict)):
            return json.dumps(v)
        else:
            return v

    def _process_json_response(self, resp, url, name: str=None):
        # parse JSON response
        try:
            json_resp = resp.json()
        except Exception:
            if not(200 <= resp.status_code <= 299):
                raise self._error_class(code="internal-error", message="internal communication error", private_details={"http-code": resp.status_code, "url": url, "name": name})
            # truncate raw response, fall through to error reporting below
            json_resp = resp.text
            if len(json_resp) > 100:
                json_resp = json_resp[:97] + "..."
        # list >> return as-is
        if isinstance(json_resp, list):
            return json_resp
        # dict >> turn into a synthetic object
        if isinstance(json_resp, dict):
            if json_resp.get("ok") is False:
                # error reported
                code = json_resp.get("code")
                msg = json_resp.get("message")
                trk = json_resp.get("_")
                raise self._error_class(code, msg, tracking_code=trk, private_details={"url": url, "name": name})
            # normal response (object), can be wrapped to make
            if self._response_wrapper:
                return self._response_wrapper(**json_resp)
            return json_resp
        else:
            # unexpected response type
            raise self._error_class(code="internal-error", message="unexpected http response", private_details={"response": json_resp, "url": url, "name": name})


class _DefaultError(Exception):
    def __init__(self, code: str, message: str = None, public_details: dict = None, private_details: dict = None, tracking_code = None):
        self.code = code
        self.message = message
        self.public_details = dict(public_details or {})
        self.private_details = dict(private_details or {})
        self.tracking_code = tracking_code

    def __str__(self):
        return self.message + ", " + repr(self.public_details)


PTN_ARG = re.compile(r'{.*?}')
