"""
Configuration.
"""
import os
import json
import sys
import typing
import re

from miniapp.api.decorators import apply_class_cache
from miniapp.comm.coerce import coerce_param_to_annotation
from miniapp.data import connect_to_db
from miniapp.utils.smtp_emailer import MockMailer, SMTP_EMailer


_LOCALHOST = "127.0.0.1"


class ConfigBase(object):
    """
    Base class for configurations.  Only very generic values shared across all applications are defined here.
    See derived classes for important configuration specific to each application.

    Note that almost all applications use a database, so get_db() is defined, but they each define their own lower
    level configuration parameters (usually 'db_uri') and their own implementation of get_db().

    Member variables (self.*) are the configurable values.  Any value can be configured through an
    environment variable named USE_(name), where (name) is the name of the variable, in upper case.

      export USE_DB_URI="memory"
      export USE_ENABLE_CSRF=true
    """
    _cache = {}

    # port to bind to
    port: int = 8888
    # the public URL through which this application can be reached - if no protocol is given, https is assumed
    external_url: str = None
    # the internal URL that other parts of the application will use to reach this service - if no protocol is given,
    #   http is assumed; if no port is given, self.port is assumed.
    internal_url: str = None
    # database - 'memory' to run in memory, 'disk:(folder)' for a very simple implementation, or a MongoDB URI
    db_uri: str = 'memory'
    # a JSON list of strings, or comma-delimited list - 'disable' disables all logging, 'disable_LEVEL' disables a level
    logging_flags: list = None
    # you can keep track of multiple installations with this value - emitted in logs
    tenant_id: str = None
    # enables CSRF protection, for user-facing services
    enable_csrf: bool = False
    # session expires after this much idle time - in SSO mode we usually don't have control of session expiration,
    #    but we still use this to predict when it will expire
    session_idle_expiration: int = 3600
    # use this flag for local development, for QA servers, etc.
    development_features: bool = False
    # email configuration - a JSON string which defines fields such as host, port, user, pwd, sender.
    emailer = None
    # This value, if given, contains JSON details with SSO configuration.  When SSO is disabled,
    # users authenticate against an internal database.  With SSO, it is assumed that Shibboleth or
    # an equivalent service has already authenticated the users and we are receiving a proxied HTTP
    # request with certain HTTP headers defined with authenticated user information.  See api.base
    # for more information about the fields defined here.
    enable_sso: (str, dict) = None
    # default password salt - used only for build-in authentication -- if using built-in encryption, please
    #   remember to configure something properly random and unique
    password_salt: str = "x8asld6fas76dfa"

    def __init__(self, **kwargs):
        """
        You can set values in the constructor.
        :param kwargs:
        """
        self.set_values(**kwargs)

    def default_logger(self, msg):
        """
        Fallback target for log streams.
        """
        print(msg)
        sys.stdout.flush()

    def set_value(self, name: str, value):
        """
        Change one value.
        """
        if name.startswith("_") or not hasattr(self, name):
            raise ValueError(f"Invalid configuration property '{name}'")
        prev_value = getattr(self, name)
        if hasattr(prev_value, "__call__"):
            raise ValueError(f"Invalid configuration property '{name}'")
        self._cache.pop(name, None)
        type_hint = typing.get_type_hints(self.__class__).get(name)
        if not type_hint and isinstance(prev_value, (int, float, bool, str, dict, list)):
            type_hint = type(prev_value)
        if type_hint:
            if type_hint in (tuple, list) and isinstance(value, str) and not value.startswith("[") and "," in value:
                # special case: comma-delimited string
                value = [v.strip() for v in value.split(",")]
            else:
                value = coerce_param_to_annotation({name: value}, name, type_hint)
        elif isinstance(value, str):
            # no hints, make only obvious adjustments
            if value.isdigit():
                value = int(value)
            elif value in ("true", "True"):
                value = True
            elif value in ("false", "False"):
                value = False
            elif value in ("null", "None"):
                value = None
            else:
                try:
                    value = float(value)
                except:
                    pass
        setattr(self, name, value)

    def set_values(self, **kwargs):
        """
        Set multiple values.
        """
        for k, v in kwargs.items():
            self.set_value(k, v)

    def apply_environment(self):
        """
        Update the configuration from the environment.
        """
        for attr in dir(self):
            if attr.startswith("_") or hasattr(getattr(self, attr), "__call__"):
                continue
            env_name = self.ENV_OVERRIDE_PREFIX + attr.upper()
            if env_name in os.environ:
                env_value = os.environ[env_name]
                self.set_value(attr, env_value)

    def apply_command_line(self, argv=None) -> list:
        """
        Set values from the command line.

        Any parameter

        :param argv:    Alternate command line.  Omit to use the command line from the current process.
        :return:        A list of all the unused parameters, i.e. everything not starting with '-'.
        """
        argv = argv if argv is not None else sys.argv
        unused = []
        for arg in argv[1:]:
            if arg.startswith("--"):
                # named value
                if "=" in arg:
                    prop_name, prop_value = arg[2:].split("=", maxsplit=1)
                else:
                    prop_name, prop_value = arg[2:], ""
                self.set_value(prop_name, prop_value)
            elif arg.startswith("-"):
                # boolean flag
                flag_name = arg[1:]
                self.set_value(flag_name, True)
            else:
                unused.append(arg)
        return unused

    @apply_class_cache(key='db')
    def get_db(self):
        """
        Get configured database.
        """
        return connect_to_db(self.db_uri, logger=self.default_logger)

    def get_external_url(self) -> (str, None):
        """
        The public/externally reachable URL of this application - a host name, and a protocol,
        i.e. https://HOST.  Not to be confused with an internal URL that may only be reachable from inside the
        cluster or VPN.
        """
        url = self.external_url
        if not url and self.development_features:
            return f"http://{_LOCALHOST}:{self.port}"
        if not url:
            return
        url = url.strip('/')
        if "://" not in url:
            url = "https://" + url
        return url

    def get_internal_url(self) -> (str, None):
        """
        The internally reachable URL for this application which other parts of the application and behind-the-scenes
        utilities can use to reach us.
        """
        url = self.internal_url or self.external_url
        if not url and self.development_features:
            return f"http://{_LOCALHOST}:{self.port}"
        if not url:
            return
        if "://" not in url:
            url = "http://" + url
        url = url.strip('/')
        if not re.search(r':\d+$', url):
            url += f":{self.port}"
        return url

    @apply_class_cache(key="logging_flags")
    def get_logging_flags(self) -> tuple:
        """
        Returns a set of flags indicating which logs should be produced.

        disable:       disable all logging
        disable_LEVEL: disable all messages for a particular level.
        """
        return tuple(self.logging_flags or [])

    def get_emailer(self):
        """
        If an emailer is configured, get an instance.

        "emailer" is a JSON string which can include the following (see SMTP_EMailer):
            host, port, user, pwd, sender
        """
        if hasattr(self, "emailer"):
            s_email = getattr(self, "emailer")
            if not s_email:
                return
            if s_email == "mock":
                return MockMailer("from_addr")
            if isinstance(s_email, str):
                emailer = json.loads(s_email)
            else:
                emailer = s_email
            return SMTP_EMailer(**emailer, logger=self.default_logger)

    def get_sso_config(self):
        """
        SSO configuration is a block of JSON which defines the following fields:
          username_header - name of HTTP header with username - MANDATORY
          header_prefix - all HTTP headers with this prefix will be captured and made available as session variables
          groups_header - name of HTTP header with group membership - format of header is "CN=group,XX=yy,...;CN=group2,..."
          email_header - name of HTTP header with email address
          tenant_header - name of HTTP header with tenant ID
          roles - mapping from group name to role name (group=role,group=role,...)
          super_role - name of a role which can enter without an invitation
          by_invitation - true: only SSO users on a list will be allowed in (list is managed by each application)
          dump_headers - true: dumps all received header values to the logs, for debugging
          mock - name of a user who will always be logged in - bypasses most other SSO logic, for debugging
          attributes - definitions of saml attributes to shibboleth to use, see Helm values file for more info
          idp - identity provider information for shibboleth, see Helm valaues file for more info
          sp - service provider information for shibboleth - see Helm valaues file for more info
          role_overrides - a mapping from sso username to the role to grant that person - overrides SSO but not user-record-level overrides
          enable_login - allow users to log in with a username and password -- ordinarily, enabling SSO means disabling login
          logout_url - URL to redirect to on logout, i.e. URL which tells SSO to log the user out

        NOTES:
          'username_header' and 'email_header' can contain format strings and be composed from multiple SSO headers.
          For example, "{first}.{last}" will assemble a username from the SSO headers 'first' and 'last'.
        """
        if self.enable_sso:
            try:
                if isinstance(self.enable_sso, str):
                    spec = json.loads(self.enable_sso)
                else:
                    spec = dict(self.enable_sso)
            except TypeError:
                spec = {}
            if "username_header" not in spec:
                spec["username_header"] = "username"
            if "groups_header" not in spec:
                spec["groups_header"] = "groups"
            if spec.get("enable") is False:
                return
            return spec

    ENV_OVERRIDE_PREFIX = "USE_"
