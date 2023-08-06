"""
Everything related to being a client of Shibboleth, i.e. support for SSO for applications behind Shibboleth.
"""
import threading
import json
import sys
import uuid
import time

from miniapp.errs import AccessDenied403
from miniapp.utils.misc import is_uuid


class SSOSupport(object):
    def __init__(self, api):
        """
        Create a support instance for a given API.  Call setup() to install the support.
        """
        self.api = api
        self.sso_cfg = None
        cfg = api.get_config()
        if cfg and hasattr(cfg, "get_sso_config"):
            self.sso_cfg = cfg.get_sso_config()

    def setup(self):
        """
        Run this once to set up SSO.  This is not part of the __init__() because it should only be called
        once when the application starts, and it needs to be tied to only one copy of the API object.
        """
        if not self.sso_cfg:
            return
        sso_wrapper = self.create_sso_wrapper()
        self.api.get_server().wrap_requests(sso_wrapper)

    def create_sso_wrapper(self):
        """
        Create a wrapper for REST handlers that implements SSO.
        """
        if not self.sso_cfg:
            return
        api = self.api
        sso_exceptions = api._sso_exceptions
        sso_cfg = self.sso_cfg
        dump_headers = sso_cfg.get("dump_headers")
        hdr_pfx = sso_cfg.get("header_prefix")
        developer_mode = sso_cfg.get("developer_mode")
        username_header = sso_cfg.get("username_header")
        email_header = sso_cfg.get("email_header")
        groups_header = sso_cfg.get("groups_header")
        mock_mode = sso_cfg.get("mock")
        role_overrides = sso_cfg.get("role_overrides", {})
        super_role = sso_cfg.get("super_role")
        sso_field_collector = _gen_sso_field_collector(hdr_pfx)
        lock = threading.Lock()
        fallback_role = api._role_names[0] if api._role_names else "ADMIN"

        def is_exception(path):
            return any(ptn.match(path) is not None for ptn in (sso_exceptions or []))

        def sso_wrapper(orig_handler):
            def handler2(method, request):
                if username_header and "{" in username_header:
                    sso_username = username_header.format(**request.headers)
                else:
                    sso_username = request.headers.get(username_header or "")
                # debugging feature: print all headers to find appropriate SAML claims
                if dump_headers:
                    api.log(json.dumps(dict(request.headers.items())), caller_detail="SSO_DEBUG")
                    sys.stdout.flush()
                # collect additional user information from SSO-supplied headers
                sso_more = sso_field_collector(request.headers)

                # mock mode
                if mock_mode:
                    self.ensure_sso_user(mock_mode, role="ADMIN")
                # analyze username and groups
                elif sso_username:
                    if email_header and "{" in email_header:
                        sso_email = email_header.format(**request.headers)
                    else:
                        sso_email = request.headers.get(email_header or "")
                    role, for_group = _look_up_role(
                        role_mapping=sso_cfg.get("roles", fallback_role),
                        sso_groups=request.headers.get(groups_header or "", ""),
                        default_role=fallback_role
                    )
                    # role_overrides can supply a minimum role for a given user
                    min_role = role_overrides.get(sso_username)
                    if min_role:
                        role = min_role
                    with lock:
                        self.ensure_sso_user(
                            sso_username, role=role, sso_more=sso_more, sso_email=sso_email
                        )
                # check for SSO exceptions
                # In developer_mode when ui is mounted no username was transmitted errors can randomly happen
                # But turning these errors off so far hasn't caused any issues for developing
                elif not (is_exception(request.path) or developer_mode):
                    raise AccessDenied403(
                        message="no username was transmitted",
                        private_details={"url": request.path, "expected-header": sso_cfg["username_header"]}
                    )
                resp = orig_handler(method, request)
                return resp

            return handler2

        return sso_wrapper

    def ensure_sso_user(
            self, sso_username: str, role: str, sso_more: dict = None, sso_email: str = None
    ):
        """
        Make sure a user is logged in with the given username and permission groups.
        :param sso_username:    Username/EID.
        :param role:            Role for the user, from SSO.
        :param sso_more:        Additional user information supplied by SSO.
        :param sso_email:       Real email address provided by SSO.
        """
        api = self.api
        # already logged in?
        # NOTE: SSO may have changed email/etc. -- these will only be updated once per session
        if api.current_username() == sso_username:
            return
        # make sure user support exists
        if not hasattr(api, "user"):
            return
        user_mod = getattr(api, "user")
        sso_email = sso_email or self._email_for_sso_user(sso_username)
        # adjust role based on supplied overrides
        sso_config = self.sso_cfg
        # TODO duplicated code for role_overrides
        role_overrides = sso_config.get("role_overrides")
        if role_overrides:
            role = role_overrides.get(sso_username) or role_overrides.get(sso_email) or role
        # dump user information into session variables
        self._set_sso_session_vars(sso_more)
        # find existing user record based on username
        matching_user_records = user_mod._query({"username": sso_username}, {"password": 0})
        correct_username = None
        if not matching_user_records and sso_email:
            # match on email if username doesn't work
            # NOTE: in this case, the username will be updated in the user record
            matching_user_records = user_mod._query({"email": sso_email}, {"password": 0})
            if matching_user_records:
                correct_username = sso_username or matching_user_records[0]["username"]
        if matching_user_records:
            user_record = matching_user_records[0]
            # work out changes to user record
            updates = _prepare_sso_updates(user_record, role, sso_email, correct_username=correct_username)
            self._apply_sso_arrival_timestamp(updates, user_record)
            if updates:
                # make changes to user record using low level method which skips permission checks
                user_mod._update(user_record["_id"], updates)
                user_record._extend(updates)
            api.log(f"sso_returning_user username={sso_username} updates={updates}", caller_detail="SSO")
        else:
            updates = {"role": role, "email": sso_email}
            self._apply_sso_arrival_timestamp(updates)
            # create new user
            updates.update({
                "username": sso_username,
                "password": str(uuid.uuid4()).replace("-", "")[:16],
            })
            user_id = user_mod._create(updates)
            user_record = user_mod._lookup(user_id, {"password": 0})
            api.log(f"sso_new_user username={sso_username} role={role}", caller_detail="SSO")
        # make sure user is logged in
        user_mod._do_login(user_record)

    def sso_headers(self, generic_names: bool = True):
        """
        Collect all HTTP headers related to SSO-provided identity and attributes, i.e. for the current user.

        The headers can be returned as-is
        (generic_names=False) to collect HTTP headers that could be passed to an identically configured SSO-enabled
        application, or with a standard set of names (generic_names=True) in order to obtain a set of SSO values
        with known names.

        The 'known names' are 'username', 'email', 'groups', and 'sso_*' for add-on headers

        :param api:             API for configuration and current user information.
        :param generic_names:  True: use a standard set of names, False: use original HTTP header names
        """
        sso_cfg = self.api.get_config().get_sso_config()
        if not sso_cfg or not self.api.current_request():
            # when not in SSO mode we can still report basic user information, if it is available
            if generic_names:
                return self._sso_headers_no_sso()
            return {}
        headers_in = self.api.current_request().headers or {}
        # add all headers with the given prefix
        headers_out = _process_header_prefix(sso_cfg, generic_names, headers_in)
        # add the specifically named headers
        for hdr in ["username", "email", "groups", "name", "surname"]:
            hdr_v = sso_cfg.get("%s_header" % hdr)
            if hdr_v and hdr_v in headers_in:
                if generic_names:
                    headers_out[hdr] = headers_in[hdr_v]
                else:
                    headers_out[hdr_v] = headers_in[hdr_v]
        return headers_out

    def _email_for_sso_user(self, sso_user: str):
        """
        SSO gives us a username.  Here we turn that into an email address.  The point here is to create an
        anonymize email-like identifier to store in the user record which can be used for git commit, etc..
        """
        if is_uuid(sso_user):
            sso_user = sso_user[-12:]
        # sometimes the username is already in the form of an email
        if not "@" in sso_user:
            return sso_user + "@sso.user"
        return sso_user

    def _set_sso_session_vars(self, sso_more: dict):
        """
        Transfer SSO-provided user information into session variables.  For example, "firstname" would be stored
        as "sso_firstname".  This allows secure management of personal information by only storing it ephemerally.
        Properly configured, all the personally identifying information will only be stored this way, and the values
        that get stored in the user record will not be personally identifying.

        In a high security configuration:
            username - do not use the person's full name here
            email - do not provide a real email address
            actual name - store this in sso_name, sso_firstname, sso_username, or similar
            actual email - store in sso_email
        """
        ssn = self.api.current_session()
        for more_n, more_v in (sso_more or {}).items():
            setattr(ssn, "sso_%s" % more_n, more_v)

    def _apply_sso_arrival_timestamp(self, updates: dict, user_record=None):
        """
        We track the time a user first arrives from SSO.
        """
        if updates is None:
            return
        field_name = self.api._sso_arrival_timestamp
        if field_name:
            if not user_record or not user_record[field_name]:
                updates[field_name] = time.time()

    def _sso_headers_no_sso(self):
        """
        Special case.  In non-SSO mode we still return basic user information.
        """
        out = {}
        v = self.api.current_username()
        if v:
            out["username"] = v
        v = self.api.current_user_email()
        if v:
            out["email"] = v
        v = self.api.get_config().tenant_id
        if v:
            out["tenant"] = v
        return out




def _look_up_role(role_mapping: str, sso_groups: str, default_role: str = "ADMIN"):
    """
    Look up a user's role based on their SSO group memberships.

    Example role mapping:
        dsw-admin-group=ADMIN, dsw-author-group=AUTHOR, USER

    :param role_mapping:        group=role, group=role, default-role
    :param sso_groups:          CN=group1,XX=yy,...;CN=group2,...
    :param default_role:        Role used in the absence of a default.
    :return:        Determined role, and associated group.
    """
    # find all group memberships
    groups = list(_parse_sso_groups(sso_groups, match_part="CN"))
    # look up role
    role = default_role
    for_group = None
    for group, group_role in _iter_role_map(role_mapping):
        if not group or group in groups:
            role = group_role.strip()
            for_group = group
            break
    return role, for_group


def _iter_role_map(role_mapping):
    """
    Parse a 'groups' value, which maps LDAP group names to DSW role names.

    Iterates pairs of (group_name, associated_role).  If group_name is blank, it indicates a default/fallback role.
    """
    role_mapping = (role_mapping or "").strip()
    for role_map in role_mapping.split(","):
        role_map = role_map.strip()
        if not role_map:
            continue
        if '=' in role_map:
            group, group_role = role_map.split('=')
            yield group.strip(), group_role.strip()
        else:
            yield "", role_map


def _parse_sso_groups(sso_groups: str, match_part: str):
    """
    Find all instances of (match_part) in the SSO groups listed by (sso_groups).

    Example LDAP style groups header value:
       CN=AIPDS_MMUI_modelengineer,OU=1234567890,DC=mobility,DC=digital,DC=com;CN=AIPDS_MMUI_modeloperationsengineer,OU=1234567890,DC=mobility,DC=digital,DC=com

    Groups can also be specified as a ";" delimited list
    """
    match_part = match_part.lower()
    sso_groups = sso_groups or ""
    for group in sso_groups.split(";"):
        group = group.strip()
        if not group:
            continue
        if "," not in group and "=" not in group and " " not in group:
            # bare group name
            yield group
            continue
        for part in group.split(","):
            if "=" not in part:
                continue
            part_name, part_value = part.split("=", 1)
            if part_name.lower() == match_part:
                yield part_value


def _gen_sso_field_collector(hdr_pfx):
    """
    Generate a collector for sso fields which match a given prefix.
    """

    def collector(headers):
        out = {}
        if hdr_pfx:
            for hn, hv in headers.items():
                if hn.startswith(hdr_pfx):
                    out[hn[len(hdr_pfx):]] = hv
        return out

    return collector


def synthesize_sso_headers(user_record, sso_config):
    """
    Generate HTTP headers that would cause a given user to be logged in.

    Purpose: simulate HTTP requests on behalf of a given user.

    :param user_record:     Information about the user to simulate.
    :param sso_config:      SSO configuration, see ConfigBase.get_sso_config()
    """
    headers = {}
    if sso_config:
        for hdr, prop in {"email_header": "email", "username_header": "username"}.items():
            hdr_name = sso_config.get(hdr)
            if hdr_name:
                headers[hdr_name] = user_record[prop]
        # set up a group to match the user's role
        user_role = user_record["role"]
        grp_hdr = sso_config.get("groups_header")
        grp_for_role = {v: k for k, v in _iter_role_map(sso_config.get("roles"))}
        if grp_hdr and grp_for_role:
            group = grp_for_role.get(user_role)
            if group:
                headers[grp_hdr] = f"CN={group}"
    return headers


def _process_header_prefix(sso_cfg, generic_names: bool, headers_in: dict):
    hdr_pfx = sso_cfg.get("header_prefix")
    if not hdr_pfx:
        return {}
    if generic_names:
        return {"sso_%s" % k[len(hdr_pfx):]: v for k, v in headers_in.items() if k.startswith(hdr_pfx)}
    else:
        return {k: v for k, v in headers_in.items() if k and k.startswith(hdr_pfx)}


def _prepare_sso_updates(user_record, sso_role: str, sso_email: str, correct_username: str=None):
    """
    Work out what values to change in a user record, given a supplied role and email.

    :param user_record:     Current user record.
    :param sso_role:        Detected role for SSO.
    :param sso_email:       Detected email for SSO.
    :return:    A {} with updates to make, or None.
    """
    updates = {"role": sso_role, "email": sso_email}
    if correct_username:
        updates["username"] = correct_username
    # system administrators can store values in certain fields and block SSO from modifying them
    blocked = user_record["sso_overrides"] or []
    update_fields = [f for f in ["role", "email"] if f not in blocked]
    # make sure user properties align with requested properties
    old_values = {f: user_record[f] for f in update_fields}
    for f in list(updates):
        if f in blocked:
            del updates[f]
    if old_values != updates:
        return updates

