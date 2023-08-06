"""
Common bits for building entry points for our services.
"""
import os
import sys
import signal
import re
import typing

from miniapp.api.base import ApiBase
from miniapp.api.configbase import ConfigBase
from miniapp.api.sso_utils import SSOSupport
from miniapp.comm.csrf import CSRF
from miniapp.comm.http import HandlerConfig
from miniapp.comm.rest import MiniREST
from miniapp.comm.session import DbSessionHandler
from miniapp.errs import GeneralError, ReportedException
from miniapp.utils.reloader import is_hot_reload_requested, run_with_reloader
from miniapp.utils.task_runner import TaskRunner


# default value for entry_point()'s add_http_headers__api parameter
HTTP_HEADERS_NO_CACHING = {"Cache-control": "no-store", "Pragma": "no-cache"}

ON_STOPPED = []


def on_stopped(handler: callable):
    """
    Add a method to call when the application is stopped.
    """
    ON_STOPPED.append(handler)


def call_on_stopped_handlers(logger: callable):
    """
    Call all the on_stop handlers.
    """
    for handler in ON_STOPPED:
        try:
            handler()
        except Exception as err:
            if not isinstance(err, GeneralError):
                err = ReportedException(err)
            logger(err.to_log())


def startup_logger(msg):
    """
    This logger is only used until an API object can be constructed.  Thereafter, the API is used for logging.
    """
    print(msg)
    sys.stdout.flush()


def generate_secure_http_headers(server_name: str=None, app_domains: (str, list)=None, script_domains: (str, list)=None, iframe_domains: (str, list)=None, dev_mode: bool=False):
    """
    Put together a set of HTTP headers which enforce some best practice security settings.

    :param server_name:  Name to send in 'Server' header, instead of 'miniapp/version'.
    :param app_domains:  One or more hostnames (wildcards allowed), where the application and its related services are
                         hosted.  All permissions are granted to these domains.  Ex: "*.mydomain.com".
    :param script_domains: Hostnames for all sources of javascript files, not including app_domains, which are included
                        automatically.
    :param iframe_domains: All domains that host iframes which are allowed to be embedded in the application.
    :param dev_mode:        In developer mode, certain settings are omitted which are very unlikely to work in local
                        development environments.
    """
    def domain_list(dl: (str, list)) -> str:
        """ stringify a list of allowed domains """
        if not dl:
            return ""
        if isinstance(dl, str):
            return dl
        return " ".join(str(d or '') for d in dl)

    headers = {
        "X-Frame-Options": "sameorigin",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "X-Content-Type-Options": "nosniff",
        "X-XSS-Protection": "1, mode=block",
    }
    if server_name:
        headers["Server"] = server_name
    if app_domains:
        csp = [
            f"default-src 'self' 'unsafe-eval' 'unsafe-inline' {domain_list(app_domains)}",
            f"object-src 'self'",
            f"script-src 'self' 'unsafe-inline' 'unsafe-eval' {domain_list(app_domains + script_domains)}",
            f"img-src 'self' {domain_list(app_domains + ['data:'])}",
            f"connect-src 'self' {domain_list(app_domains)}"
        ]
        if iframe_domains:
            csp.append(f"frame-src {iframe_domains}")
        if not dev_mode:
            csp.append(f"upgrade-insecure-requests")
            csp.append(f"block-all-mixed-content")
        headers["Content-Security-Policy"] = "; ".join(csp)
    return headers


def web_root_contains_file(web_root, filename):
    """
    Check whether a given file is available in the web root.
    """
    if not web_root:
        return
    folders = [web_root] if isinstance(web_root, str) else web_root
    for folder in folders:
        if os.path.exists(os.path.join(folder, filename)):
            return True


def entry_point(api_class: type, config_class: type=None, config_defaults: dict=None,
                main_py: str="main.py", api_base_url: str="/api/v1", web_root: (str, dict)=None,
                api_setup: typing.Callable[[ApiBase.__class__], None]=None,
                bg_task_setup: typing.Callable[[ApiBase.__class__, TaskRunner.__class__], None]=None,
                redirects: (dict, list)=None, rewrites: (dict, list)=None,
                reload_source_root: (str, list)=None,
                call_when_stopped: callable=None,
                csrf_ignore_urls: (re.Pattern, str)=None, logged_in_paths: list=None, secure_cookies: bool=True,
                add_http_headers: dict=None, add_http_headers__api: dict=None,
                enable_api_test_page: str=None, use_subprocesses: bool=False, daemon_threads: bool=True):
    """
    Entry point helper for microservices and application back-ends.

    :param api_class:       API - class to instantiate.
    :param config_class:    Configuration - class to instantiate, values will be filled in from environment variables.
    :param config_defaults: Changes to default values for configuration.  Environment variables override these.
    :param main_py:         Relative path to entry point.  Used for HOT_RELOAD.  Default is 'main.py'.
    :param api_base_url:    Where the API will be hosted.  Default is /api/v1.
    :param web_root:        Path to web content, or a {} mapping URLs to web roots.
    :param reload_source_root: Location of source folder(s) that should trigger 'hot reload'.
    :param api_setup:       Additional setup of API after it is instantiated.
    :param bg_task_setup:   Set up background tasks - supply a method that takes (api, task_runner) which calls
                            task_runner.add_task().  See TaskRunner.
    :param redirects:       Redirection rules.  A {src: dst, ...} or a [(src, dst), ...].  See MiniREST.add_redirect().
    :param rewrites:        Rewrite rules.  A {src: dst, ...} or a [(src, dst), ...].  See MiniREST.add_rewrite().
    :param call_when_stopped: Method to call when server shuts down.
    :param csrf_ignore_urls: A regex for URLs to omit from CSRF protection.
    :param logged_in_paths: Experimental.  A separate session cookie will be set for each listed path.
                            Default is ["/"].
    :param secure_cookies:  True to require HTTPS for session cookies.  This should be True for
                            user-facing services and False for internal services.  Will be changed to False if
                            config.development_features is set.
    :param add_http_headers: HTTP headers added to all responses.  You can use generate_secure_http_headers() to build
                            this value or omit it to not add any headers, or to allow the application or a proxy be in
                            charge of adding headers.
    :param add_http_headers__api: HTTP headers added to REST responses.  A default value that disables caching is used.
                            To inhibit this default, pass {}.
    :param enable_api_test_page: To enable the built-in API test page, supply a path.
    :param use_subprocesses: True to handle all requests in subprocesses (experimental),
                            False to handle them in threads.
    :param daemon_threads:  True - all requests terminate when the server is stopped (i.e. with SIGTERM),
                            False - requests are allowed to terminate when server is stopped.
    :return:   Does not return.
    """
    # defaults
    if not config_class:
        config_class = ConfigBase
    if add_http_headers__api is None:
        add_http_headers__api = HTTP_HEADERS_NO_CACHING
    # register supplied clean-up function
    if call_when_stopped:
        on_stopped(call_when_stopped)
    # hot reload requested?
    if reload_source_root and is_hot_reload_requested() and "--no-reload" not in sys.argv:
        startup_logger("RUNNING WITH HOT_RELOAD=1")
        run_with_reloader(reload_source_root, [main_py, "--no-reload"], "python")
        sys.exit(0)
    # get configuration - note the precedence, from lowest to highest (higher overrides lower):
    #   1) config_class's defaults
    #   2) supplied 'config_defaults'
    #   3) environment variables
    #   4) command line
    config = config_class(**(config_defaults or {}))
    config.apply_environment()
    config.apply_command_line()
    dev_mode = hasattr(config, "development_features") and config.development_features
    if dev_mode:
        secure_cookies = False
    # set up web server and API
    logger = config.default_logger
    the_db = config.get_db()
    session_handler = DbSessionHandler(the_db) if the_db else None
    handler_config = HandlerConfig(logged_in_paths=logged_in_paths, https_only=secure_cookies)
    max_session_expire = 24*3600 if config.get_sso_config() else config.session_idle_expiration + 1
    server = MiniREST(
        config.port, logger=logger, session_handler=session_handler, handler_config=handler_config,
        max_session_expire=max_session_expire
    )
    # custom http headers
    if add_http_headers:
        server.add_custom_headers(".*", add_http_headers)
    if add_http_headers__api:
        server.add_custom_headers(f"^{api_base_url}($|/.*)", add_http_headers__api)
    # more server setup
    if config.enable_csrf:
        server.csrf = CSRF(csrf_ignore_urls)
    server.track_session_activity()
    # exit elegantly
    def signal_handler(sig, frame):
        call_on_stopped_handlers(logger)
        server.shutdown(1)      # haven't found a way to shut down connection threads yet, so using a short timeout
        sys.exit(0)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    # instantiate and configure the API
    api = api_class(config, server)
    server.logger = lambda message, level, caller_detail=None: api.log(message, level, caller_detail or "WEB")
    # - connect endpoints to server
    api.configure_server(base_url=api_base_url)
    if config.get_sso_config():
        SSOSupport(api).setup()
    # serve static content
    if web_root:
        if isinstance(web_root, str):
            server.add_static_folder("/", web_root)
        else:
            for url, root in web_root.items():
                server.add_static_folder(url, root)
        if redirects is None and web_root_contains_file(web_root, "index.html"):
            server.add_redirect("/", "/index.html")
    # API test page
    if enable_api_test_page:
        if not enable_api_test_page.startswith("/"):
            enable_api_test_page = "/" + enable_api_test_page
        if not enable_api_test_page.endswith("/"):
            enable_api_test_page += "/"
        api_test_content = os.path.join(os.path.dirname(__file__), "../web/api_test")
        server.add_static_folder(enable_api_test_page, api_test_content)
        server.add_redirect(enable_api_test_page, enable_api_test_page + f"index.html?url={api_base_url}")
    # redirects & rewrites
    for src, dst in (redirects.items() if isinstance(redirects, dict) else redirects or []):
        server.add_redirect(src, dst)
    for src, dst in (rewrites.items() if isinstance(rewrites, dict) else rewrites or []):
        server.add_rewrite(src, dst)
    # more api setup
    if api_setup:
        # general setup
        api_setup(api)
    if bg_task_setup:
        # set up background tasks
        task_runner = TaskRunner()
        bg_task_setup(api, task_runner)
        task_runner.start()
        on_stopped(task_runner.stop)
    # ready to start up
    version_info = ", ".join("%s=%s" % kv for kv in api.version().items())
    api.log("starting on port %d, %s" % (config.port, version_info), caller_detail="STARTUP")
    ext_url = config.get_external_url()
    if ext_url:
        api.log(f"url: {ext_url}", caller_detail="STARTUP")
    if dev_mode:
        api.log("RUNNING IN DEVELOPMENT MODE", caller_detail="STARTUP")
    # start the server
    server.start(
        mode="subprocesses" if use_subprocesses else "threads",
        wait_for_shutdown=True,
        daemon_threads=daemon_threads
    )
    # shut down
    call_on_stopped_handlers(logger)
    sys.exit(0)
