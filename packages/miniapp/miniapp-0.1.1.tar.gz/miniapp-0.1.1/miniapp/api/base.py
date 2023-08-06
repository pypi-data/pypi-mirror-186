from jsonschema import ValidationError
import os
import sys
import json
import jsonschema
import time

from miniapp.api.capture_user_activity import intercept_endpoints
from miniapp.api.cat_base import ApiCategoryBase
from miniapp.comm.binding import create_endpoint_decorator
from miniapp.comm.session import SessionDict
from miniapp.errs import InternalError, GeneralHttpError, GeneralError
from miniapp.utils.file_utils import load_file, normalize_path
from miniapp.utils.json_utils import repair_to_schema
from miniapp.utils.lru_cache import LruCache
from miniapp.utils.template_utils import Templates

endpoint = create_endpoint_decorator(
    permission_checker=lambda instance, perm_requested: instance.api.has_permission(perm_requested)
)
LOGGING_LEVEL_NAMES = ("FATAL", "ERROR", "WARN", "INFO", "DEBUG")


class ApiBase(object):
    """
    Base class for APIs.
    """
    def __init__(
            self, config=None, server=None, disable_permissions=False,
            schema_path=None, template_path=None, version_path=None,
            helpdoc_path=None, visible_schemas=None,
            sso_exceptions: list=None,
            role_names: list=None, role_permissions: dict=None,
            caches: dict=None
        ):
        """
        Get an instance of the API, with the given configuration and permission mechanism.
        :param config:   Configuration, with such things as the database.
        :param server:   The server.  If not given, permission checking will be disabled.
        :param disable_permissions:  True to disable all permission checking.
        :param schema_path:  Root folder where schema JSON is kept.
        :param visible_schemas:  A callable which indicates whether the current user should be allowed to see a given
            schema (see ApiCommonBase.fetch_schema()).
        :param template_path: Where templates are kept.
        :param version_path: Application version file path.
        :param helpdoc_path: Where help files are kept.
        :param sso_exceptions:  A list of regexes for URLs that do not require SSO authentication.
        :param role_names: Ordered list of roles, least to most privileged.
        :param role_permissions: A {} with a list of permissions available to each role.
        :param caches:      A place to store all caches throughout the whole system.
        """
        self._config = config
        self._server = server
        self._serverless_session = None
        self._disable_permissions = disable_permissions
        self._schema_path = schema_path
        self._visible_schemas = visible_schemas
        self._template_path = template_path
        self._templates = None
        self._helpdoc_path = helpdoc_path
        self._override_session = None
        self._version_path = version_path
        self._version_info = None
        self._sso_config = None
        self._sso_arrival_timestamp = None
        self._sso_exceptions = sso_exceptions
        self._emailer = None
        self._last_ping = None
        self._ping_count = 0
        self._caches = caches if caches is not None else {}
        self._mode = None
        self._role_names = role_names if role_names is not None else list(role_permissions) if role_permissions else []
        self._default_role = self._role_names[0] if self._role_names else None
        self._role_permissions = self._compile_permissions(role_permissions, self._role_names)

    def _do_ping(self, level: str=None, count: int=None):
        """
        Implement health check here.  Raise an exception if anything is wrong.
        """

    def _clone_args(self):
        """
        When an API instance is cloned (see admin_instance() and instance_for_user()), this method will supply
        additional initialization arguments so that the state of the original API will be preserved in the copy.
        """
        return {}

    def setup_cache(self, name: str, expiration_time: int=None, max_size: int=0, refresh_expiration_on_read=False):
        """
        Set up or re-use a cache.
        """
        if name in self._caches:
            return self._caches[name]
        if not expiration_time and not max_size:
            cache = {}
        else:
            cache = LruCache(max_size=max_size, expiration_time=expiration_time, refresh_expiration_on_read=refresh_expiration_on_read)
        self._caches[name] = cache
        return cache
        # TODO we should follow this pattern (of calling setup_cache() to get a universal instance of something) for
        #   threading.Lock() as well - there are some locks being enforced which
        #   will not be enforced when copies are made of the API

    def start_up(self, startup_complete: bool=False):
        """
        Check whether it is appropriate to do API start-up activities.  Call with startup_complete=True to end API start-up.
        """
        if startup_complete:
            self._caches["startup_complete"] = True
        return self._caches.get("_startup_complete_", True)

    def _cmp_role_names(self, a, b):
        """
        Test which role is higher (mor privileged).
        """
        if not self._role_names or a not in self._role_names or b not in self._role_names:
            return None
        n_a = self._role_names.index(a)
        n_b = self._role_names.index(b)
        if n_a == n_b:
            return 0
        if n_a < n_b:
            return -1
        return 1

    def _compile_permissions(self, role_perms: dict, role_names: list):
        """
        Permissions are cumulative - higher roles have all permissions of lower roles.  We are supplied with the
        permissions unique to each role, but we need to store a complete list of permissions available to each role.
        """
        out = {}
        accum = set()
        role_perms = role_perms or {}
        for role in role_names:
            perms = role_perms.get(role, [])
            accum |= set(perms)
            out[role] = list(sorted(accum))
        return out

    @property
    def emailer(self):
        """
        Get the class which can send email.
        """
        if not self._emailer:
            cfg = self.get_config()
            if cfg:
                self._emailer = cfg.get_emailer()
        return self._emailer

    def log(self, message="", level="INFO", caller_detail=None):
        """
        Logging...
          TIMESTAMP|LEVEL|TENANT|CONTEXT|MESSAGE
        """
        if level not in LOGGING_LEVEL_NAMES:
            raise Exception("invalid log level %s" % level)
        # you can disable logging entirely, or by level
        cfg = self.get_config()
        if "disable" in cfg.get_logging_flags():
            return
        if "disable_%s" % level.lower() in cfg.get_logging_flags():
            return
        # ensure messages all fit on one line, escape delimiter
        message = message.replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r").replace("|", "[[BAR]]")
        msg = [
            # timestamp, level, tenant
            _log_timestamp(), level, cfg.tenant_id or "",
            # contextual detail
            caller_detail or "",
            # message
            message
        ]
        # config class defines logging stream
        cfg.default_logger("|".join(msg))

    def admin_instance(self):
        """
        Returns an instance of the API with no permission checking.
        """
        if self._disable_permissions:
            return self
        out = self.__class__(
            config=self._config, server=self._server, disable_permissions=True, **self._clone_args(),
            caches=self._caches
        )
        out._serverless_session = self._serverless_session
        return out

    def instance_for_user(self, user_name: str=None, user_email: str=None, user_id: str=None,
                          user_role: str=None, disable_permissions: bool=None, use_session_id: str=None):
        """
        Returns an instance of the API which is authenticated as a given user.
        """
        if self._mode and self._mode == user_name:
            return self
        session = SessionDict()
        session.user_name = user_name
        session.user_id = user_id
        session.user_email = user_email
        session.user_role = user_role
        if not user_email or not user_name or not user_id:
            inst = self.admin_instance()
            user_cat_name = [
                fn for fn in dir(inst)
                if not fn.startswith("_")
                    and hasattr(getattr(inst, fn), "get_user")
                    and hasattr(getattr(inst, fn), "_set_session_from_user_record")
            ]
            if user_cat_name:
                user_cat = getattr(inst, user_cat_name[0])
                urec = user_cat.get_user(user_id or user_name)
                user_cat._set_session_from_user_record(session, urec)
            else:
                raise InternalError("instance_for_user() - missing fields and could not look up user")
        inst = self.__class__(
            config=self._config, server=self._server,
            disable_permissions=disable_permissions if disable_permissions is not None else self._disable_permissions,
            ** self._clone_args(),
            caches=self._caches
        )
        inst._override_session = session
        use_session_id = use_session_id or self.current_session_id()
        inst.current_session_id = lambda: use_session_id
        inst._mode = inst.current_username()
        return inst

    def multithread_instance(self):
        """
        Normally the API uses thread-locals to track authentication.  This method creates an API instance that
        works across threads.
        """
        if self._mode:
            return self
        if not self._server:
            return self
        session = self._server.current_session()
        session_id = self.current_session_id()
        request = self._server.current_request()
        ssn_activity = self._server.session_activity
        orig = self
        class ServerPlaceholder(object):
            def __init__(self):
                class RequestHolder(object):
                    def __init__(self):
                        self.request = request
                self.current = RequestHolder()
                self.session_activity = ssn_activity
            def current_request(self):
                return request
            def current_session(self):
                return session
            def wrap_requests(self, wrapper: callable):
                """ disable wrapping """
            def active_users(self):
                return orig._server.active_users()
        out = self.__class__(
            config=self._config, server=ServerPlaceholder(), disable_permissions=self._disable_permissions,
            ** self._clone_args(),
            caches=self._caches
        )
        out.current_session_id = lambda: session_id
        out._serverless_session = self._serverless_session
        out._mode = "_MT_"
        return out

    def version(self) -> dict:
        """
        System version.
        """
        if self._version_info is None:
            self._version_info = self.load_version_info(self._version_path)
        return self._version_info

    @staticmethod
    def load_version_info(path: str) -> dict:
        """
        Get version & release information.
        """
        v, r = None, None
        if path:
            fn = os.path.join(path, "version")
            v = (load_file(fn, must_exist=False) or '').strip()
            fn = os.path.join(path, "release")
            r = (load_file(fn, must_exist=False) or '').strip()
        return {"version": v, "release": r}

    def ping(self, level: str=None):
        """
        Verify system is operational.
        :returns:  True if ok, raises HTTP error if not.
        """
        last_ping_t, last_ping_err = None, None
        if self._last_ping:
            last_ping_t, last_ping_err = self._last_ping
        t_now = time.time()
        if not last_ping_t or t_now - last_ping_t >= 1:
            err = None
            try:
                self._do_ping(level, self._ping_count)
            except Exception as exc:
                err = exc
            self._last_ping = t_now, err
            last_ping_err = err
        self._ping_count += 1
        if last_ping_err:
            raise GeneralHttpError(http_code=503, message="false", mimetype="application/json", code="ping-failure")
        return True

    def active_usernames(self, in_last_s: int=15*60):
        """
        Get the list of users active in the last (period of time).
        """
        names = []
        if self._server:
            t_threshold = time.time() - in_last_s
            for user_info in self._server.active_users():
                if user_info["last_activity"] < t_threshold:
                    continue
                user_name = user_info["user_name"]
                if user_name:
                    names.append(user_name)
            names.sort()
        return names

    def get_validation_schema(self, schema_name: (str, list, tuple)) -> dict:
        """
        Returns JSON-SCHEMA json describing a given schema.
        :param schema_name:  Name of a JSON-SCHEMA within the designated folder ('_schema_path'),
            or an iterable of names which will be strung together like a path.
        """
        if self._schema_path:
            if isinstance(schema_name, (list, tuple)):
                schema_name = "/".join(schema_name)
            # TODO delete this -- all paths are generated by code, no need to be paranoid here
            #if wbcommon.misc.is_breakout_path_element(schema_name):
            #    raise Exception(f"invalid schema name: {schema_name}")
            if not schema_name.endswith(".json"):
                schema_name += ".json"
            schema_fn = os.path.join(self._schema_path, normalize_path(schema_name, safe=True))
            if os.path.exists(schema_fn):
                with open(schema_fn) as fR:
                    return json.load(fR)
        return {}

    def validate_schema(self, schema_name: (str, list, tuple), data_to_validate, partial_record: bool=False, repair: bool=False, schema_subpath: str=None):
        """
        Validate data against a schema stored in the codebase.
        :param schema_name:   Reference to a particular schema.  See get_validation_schema().
        :param data_to_validate:  What will be checked for errors.
        :param partial_record:   True to ignore 'required' blocks.
        :param repair:      Whether to attempt to repair data in simple cases, rather than fail.
        :param schema_subpath:    Allows a sub-structure to be enforced within a schema.  Specify an XPath-like location
                            consisting of named elements separated by '/'.
        """
        data = _streams_to_strings(data_to_validate)
        schema = self.get_validation_schema(schema_name)
        if schema:
            # extract schema sub-path if requested
            if schema_subpath:
                for part in schema_subpath.strip("/").split("/"):
                    schema = schema.get(part, {})
            if partial_record:
                # at the moment we only ignore 'required' at the top level
                schema = dict(schema)
                schema.pop("required", None)
            if repair and repair_to_schema(data, schema):
                data_to_validate.clear()
                data_to_validate.update(data)
            try:
                jsonschema.validate(data, schema)
            except jsonschema.ValidationError as err:
                schema_name_coded = schema_name if isinstance(schema_name, str) else "-".join(schema_name)
                if schema_subpath:
                    schema_name_coded += "-" + schema_subpath.replace("/", "_")
                raise GeneralError.validation_error(err, schema_name_coded)

    def apply_template(self, template_name: str, template_params: dict=None):
        """
        Templatize some values.
        :param template_name:       Name of template.
        :param template_params:     Parameters.
        :return:        Values rendered through template, if template exists.
        """
        if not self._templates:
            template_params = template_params or {}
            if not self._template_path:
                return "%s: %s" % (template_name, template_params)
            self._templates = Templates(self._template_path)
        return self._templates.render(template_name, template_params)

    def find_category(self, name: (str, list)=None, instance_of: type=None, has_methods: list=None, fail_on_missing: bool=True):
        """
        Find an API category...

        :param name:        Match by name (or a list of names).
        :param instance_of: Match on base class.
        :param has_methods: Match on whether certain methods are available.

        :return:    The category, i.e. "self.category".
        """
        found = []
        names = [name] if isinstance(name, str) else name
        for field_name in dir(self):
            if field_name.startswith("_"):
                continue
            if name and field_name not in names:
                continue
            member = getattr(self, field_name)
            if not isinstance(member, ApiCategoryBase):
                continue
            if instance_of and not isinstance(member, instance_of):
                continue
            if has_methods and not all(list(hasattr(member, method) for method in has_methods)):
                continue
            found.append(member)
        if len(found) == 1:
            return found[0]
        if fail_on_missing:
            msg = []
            if name:
                msg.append(f"name={name}")
            if instance_of:
                msg.append(f"instance_of={instance_of}")
            if has_methods:
                msg.append(f"has_methods={has_methods}")
            if found:
                raise InternalError(f"API category not found matching ({', '.join(msg)}) - {len(found)} matches")
            else:
                raise InternalError(f"API category not found matching ({', '.join(msg)})")

    def configure_server(self, base_url):
        """
        Set up the associated server to handle this API.  All ApiCategoryBase fields in this class are made available
        as sets of endpoints ("categories") to the REST interface.

        :param base_url:   Base URL for all calls.
        """
        if not self._server:
            return
        if not base_url.endswith("/"):
            base_url += "/"
        for category_name in dir(self):
            if category_name.startswith("_"):
                continue
            category = getattr(self, category_name)
            if not isinstance(category, ApiCategoryBase):
                continue
            if hasattr(category, "prefix"):
                prefix = category.prefix
            else:
                prefix = category_name.lower()
            self._server.add_category(base_url + prefix, category)
        # enable activity analysis if that API category is present
        user_activity = self.find_category(has_methods=["record_activity", "aggregate_sessions"], fail_on_missing=False)
        if user_activity:
            intercept_endpoints(self._server, self)

    def get_db(self):
        """
        Get current database.
        """
        return self._config.get_db() if self._config else None

    def get_server(self):
        """
        Associated web server.
        """
        return self._server

    def get_config(self):
        """
        Current configuration.
        """
        return self._config

    def current_request(self):
        """
        Current request.
        """
        if self._server:
            return self._server.current_request()

    def current_session(self):
        """
        Session for current request.
        """
        if self._override_session:
            return self._override_session
        rq = self.current_request()
        if rq:
            return rq.session
        else:
            # tracking a session without a server allows login()/logout() to work
            if self._serverless_session is None:
                self._serverless_session = SessionDict()
            return self._serverless_session

    def current_username(self):
        """
        Username for current user.
        """
        ssn = self.current_session()
        if ssn:
            return ssn.user_name

    def current_user_email(self):
        """
        EMail for current user.
        """
        ssn = self.current_session()
        if ssn:
            return ssn.user_email

    def current_user_id(self):
        """
        ID of current user.
        """
        ssn = self.current_session()
        if ssn:
            return ssn.user_id

    def current_user_role(self):
        """
        Role of current user.
        """
        ssn = self.current_session()
        if ssn:
            if not ssn.user_role:
                if ssn.user_id:
                    # assume lowest role as long as user is logged in
                    return self._default_role
            return ssn.user_role

    def current_session_id(self):
        """
        ID of current session.
        """
        rq = self.current_request()
        if not rq:
            return
        return rq.session_id

    def has_permission(self, permission_required):
        """
        Check whether the current user has a given permission.

        :param permission_required:  The code for a particular permission that the user must have.

        :returns:       True: permission is granted
                        False: permission denied, no details available
                        None: user is not logged in
                        {}: permission is denied, details for error message are provided
        """
        if self._disable_permissions or not permission_required:
            return True
        # not logged in?
        if not self.current_user_id():
            return
        role = self.current_user_role()
        perms_available = self._role_permissions.get(role or self._default_role, [])
        check_perm = permission_required if isinstance(permission_required, str) else permission_required[0]
        return check_perm in perms_available


def _wrap_validation_error(err: ValidationError):
    """
    Turn a ValidationError from "jsonschema" into a {}.
    """
    return dict(message=err.message, path=list(err.path), schema=list(err.schema_path))


def _log_timestamp(t=None):
    """
    Timestamp value for logging.
    """
    t = t or time.time()
    out = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(t))
    out += ".%03dZ" % int((t - int(t)) * 1000)
    return out


def _streams_to_strings(data):
    if isinstance(data, dict):
        return {k: _streams_to_strings(v) for k, v in data.items()}
    if hasattr(data, "read"):
        return ""
    return data
