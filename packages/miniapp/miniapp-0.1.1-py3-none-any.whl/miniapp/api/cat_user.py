import base64
import uuid
import time
import re
import jsonschema
import hashlib
import json

from miniapp.api.auth import alt_authenticate
from miniapp.api.base import endpoint
from miniapp.api.cat_base import ApiCategoryBaseCRUD
from miniapp.data.const import ROW_ID
from miniapp.data.impl import prepend_update, compile_query
from miniapp.errs import BadRequest, GeneralError, AccessDenied403, InternalError
from miniapp.utils.generic_obj import make_object
from miniapp.utils.misc import random_password

PTN_HASHED_PASSWORD = re.compile(r'^[0-9a-f]{32}$')
PTN_VALID_USERNAME = re.compile(r'^[a-zA-Z0-9.\-%_@]+$')

LOGIN_FAILED_CODE = "login-failed"
LOGIN_FAILED_MSG = "login failed"


class UserBase(ApiCategoryBaseCRUD):
    DESCRIPTION = "User management."

    """
    User management, login.
    """
    def __init__(self, api, on_login: callable=None, audit: callable=None, perm_manage_users=None, perm_super_user=None, validator=None, sequence=0):
        """
        Base class for user information, including basic login functionality.

        :param api:         API for which this instance will become a new category.
        :param on_login:    Method to call on every login.
        :param audit:       Reporting of major auditable events in user lifecycle.
        :param perm_manage_users:  Permission required to modify user information (other than restricted access to 'self')
        :param perm_super_user:    Permission required for highly restricted operations.
        :param validator:   Path to schema JSON for user record, relative to API's schema root.
        """
        super(UserBase, self).__init__(api, sequence=sequence, collection_name="users", validator=validator)
        self._alt_lookup_field = "username"
        self._on_login = on_login
        self._audit = audit
        self._perm_manage_users = perm_manage_users
        self._perm_super_user = perm_super_user
        self._visible_fields = {"password": 0}
        self._username_cache = api.setup_cache("user_username", expiration_time=30)
        self.LIST_USERS_FIELDS = {"username", "role", "email", ROW_ID}
        self.LIST_USERS_FIELDS_NON_ADMIN = {"username", ROW_ID}

    def normalize_user_id_and_name(self, user_id_or_name: str):
        """
        A user can be specified either by name or ID.  This method lets us turn one of those into both.

        :returns:       A tuple with user ID and user name.
        """
        out = self._username_cache.get(user_id_or_name)
        if not out:
            urec = self._lookup(user_id_or_name, fields=["username"], not_found_error=False)
            if not urec:
                out = (None, None)
                self._username_cache[user_id_or_name] = out
            else:
                out = urec._id, urec.username
                self._username_cache[urec._id] = out
                self._username_cache[urec.username] = out
        return out

    def _apply_alt_authentication(self, username, password):
        """
        Apply alternate authentication.  (This is only a placeholder.)
        """
        found_user_props = alt_authenticate(self.api, username, password)
        if found_user_props is not None:
            # find existing record
            found = self._query({"username": username}, self._visible_fields)
            if not found:
                # create new user record
                # create new user record
                new_rec = found[0]._to_json() if found else make_object(username=username)
                new_rec._extend(found_user_props)
                user_id = self._create(new_rec._to_json())
                new_rec._extend({ROW_ID: user_id})
                return [new_rec]
            elif found_user_props:
                # update user record with remote authenticator's changes
                user_id = found[0]._id
                self._update(user_id, found_user_props)
                found = [self._lookup(user_id)]
            return found

    def _setup_default_user(self, username, password=None, email=None, role="ADMIN"):
        """
        Ensure that a configured user exists.  The account will only be created if the given username does not yet
        exist.
        :returns: True if a new user record was created.
        """
        placeholder_email = False
        if username:
            if not email:
                placeholder_email = True
                email = username + "@dsw.accenture.com"
            admin_users = self.list_users({"username": username}).results
            if not admin_users:
                pwd = password or random_password()
                self.create_user(record={
                    "username": username, "password": pwd, "role": role,
                    "email": email
                })
                # send password reminder in non-SSO mode
                sso_cfg = self._get_sso_config()
                if not placeholder_email and not sso_cfg:
                    self.start_recovery(email)
                return True

    def _pwd_hashes(self, pwd: str):
        """
        Do password hashing.  First result is the proper one to store.  All others are for backward compatibility.

        TODO customize 'salt' value
        """
        pwd_salt = self.api.get_config().password_salt.encode("utf-8")
        if isinstance(pwd, str):
            pwd = pwd.encode("UTF-8")
        pwd_hash = hashlib.pbkdf2_hmac("sha256", pwd, salt=pwd_salt, iterations=400000).hex()
        return [
            pwd_hash,
            # NOTE: if you have a very old local development environment and want your ancient MD5-encoded passwords
            #   to work, un-comment this line, but PLEASE DO NOT CHECK IT IN
            # wbcommon.misc._md5(pwd)
        ]

    def login(self, username: str='', password: str=''):
        """
        Sign in a user based on a username and password.
        """
        username = username or ""
        # prevent unreasonable requests
        if username and (len(username) > 100 or not PTN_VALID_USERNAME.match(username)):
            raise GeneralError(code=LOGIN_FAILED_CODE, message=LOGIN_FAILED_MSG, private_details={"username": username})
        if len(password) > 256:
            raise GeneralError(code=LOGIN_FAILED_CODE, message=LOGIN_FAILED_MSG, private_details={"username": username})
        sso_cfg = self._get_sso_config()
        if sso_cfg and not sso_cfg.get("enable_login"):
            raise GeneralError(
                code="login-disabled", message="login disabled, use SSO instead"
            )
        fields = {"password": 0, "auth_token": 0}
        found = None
        if not username:
            found = self._query({"auth_token": password}, fields, all_visible=True)
        else:
            pwd_hashes = self._pwd_hashes(password)
            for pwd_hash in pwd_hashes:
                found = self._query({"username": username, "password": pwd_hash}, fields, all_visible=True)
                if found:
                    break
        if not found:
            found = self._apply_alt_authentication(username, password)
        if found:
            self._do_login(found[0])
            self.api.log(f"user={username}, success=1", caller_detail="LOGIN")
            return make_object(user=found[0], ok=True)
        else:
            self.api.log(f"user={username}, success=0", caller_detail="LOGIN")
            raise GeneralError(
                code=LOGIN_FAILED_CODE, message=LOGIN_FAILED_MSG,
                private_details={"username": username}
            )

    def _do_login(self, user_record):
        session = self.api.current_session()
        if session is None:
            raise InternalError("no session")
        self._set_session_from_user_record(session, user_record)
        if self._on_login:
            self._on_login()

    def _set_session_from_user_record(self, session, user_record):
        """
        Fill in a session object from values in a user record.  This happens at login.
        """
        if user_record:
            session.user_id = getattr(user_record, ROW_ID)
            session.user_role = user_record.role
            session.user_name = user_record.username
            session.user_email = user_record.email
        else:
            session.user_id = None
            session.user_role = None
            session.user_name = None
            session.user_email = None

    def logout(self, session_ids: list=None, all: bool=False):
        """
        Log out the user's current session, or optionally log out multiple sessions belonging to the currently
        logged in user.
        """
        # TODO explain this
        session = self.api.current_session()
        if session is not None:
            self._set_session_from_user_record(session, None)
        # log out specific sessions
        if session_ids or all:
            current_user_id = self.api.current_user_id()
            if current_user_id:
                ssn_filter = {"user_id": current_user_id()}
                if session_ids and not all:
                    ssn_filter["_id"] = {"$in": list(session_ids)}
                purge_filter = compile_query(ssn_filter)
                self.api.get_server().session_handler.purge(filter=purge_filter)
        # inform SSO provider of logout
        sso_cfg = self.api.get_config().get_sso_config()
        if sso_cfg:
            # Web Client needs to be routed to below URL to log out of Shibboleth
            return make_object(logout_url=sso_cfg.get("logout_url"))
        return make_object()

    def start_recovery(self, email: str, recovery_time_limit: int=None):
        """ Generate a recovery code for a user record.  Returns the recovery code if account is found. """
        rr = self._query({"email": email}, self._visible_fields)
        if not rr:
            return
        recovery_code = generate_recovery_code()
        recovery_time_limit = recovery_time_limit or 3 * 3600
        t_now = int(time.time())
        recovery_code_expires = t_now + recovery_time_limit
        # don't allow rapidly repeated requests
        prev_request_expires = rr[0]["recovery_code_expires"]
        if prev_request_expires and t_now - prev_request_expires[0] < 30:
            return
        # store the recovery code
        self.update_user(rr[0]["_id"], {"recovery_code": recovery_code, "recovery_code_expires": [t_now, recovery_code_expires]})
        return recovery_code, recovery_code_expires

    def recover_account(self, email: str, recovery_code: str):
        """ Log in using a recovery code. Returns user record. """
        rr = self._query({"email": email, "recovery_code": recovery_code}, self._visible_fields)
        if not rr or rr[0]["recovery_code_expires"][1] < time.time():
            return
        self._do_login(rr[0])
        return rr[0]

    def _clean_new_record(self, record: dict):
        store = dict(record)
        # extract username from email
        if "username" not in store and "email" in store:
            store["username"] = store["email"].split("@")[0]
        store = self._clean_changes(store, record)
        return store

    def _clean_changes(self, changes, old_rec: dict):
        # always store hashed password
        if "password" in changes and PTN_HASHED_PASSWORD.match(changes["password"]) is None:
            changes = dict(changes)
            changes["password"] = self._pwd_hashes(changes["password"])[0]
        # only super-user can change this field
        if "sso_overrides" in changes and (not self._perm_super_user or not self.api.has_permission(self._perm_super_user)):
            changes.pop("sso_overrides")
        return changes

    def _extra_validation(self, record, exclude_id=None):
        self._enforce_unique(record, exclude_id, "username")

    def _add_sso_info(self, out: dict):
        """
        Add SSO-supplied information
        """
        ssn = self.api.current_session()
        if not ssn or not ssn.ALL:
            return
        for vx in ["sso_email", "sso_username"]:
            if vx in ssn.ALL:
                out[vx] = ssn[vx]

    def whoami(self):
        vals = {}
        rqst = self.api.current_request()
        user_id = self.api.current_user_id()
        vals["session_id"] = rqst.session_id if rqst else None
        vals["user_id"] = user_id
        if user_id:
            user_rec = self.get_user("self")
            vals["user_name"] = user_rec.username
            vals["user_role"] = self.api.current_user_role()
        # add SSO-supplied information
        self._add_sso_info(vals)
        return make_object(**vals)

    def query_sessions(self, query: dict):
        """
        Search session information.
        """
        return list(self.api.get_server().session_handler.query(query))

    def list_users(self, query: dict=None):
        admin = self.api.has_permission(self._perm_manage_users)
        results = self._query(query, self.LIST_USERS_FIELDS if admin else self.LIST_USERS_FIELDS_NON_ADMIN)
        if not admin:
            # show nothing but username to non-admins
            results = [{"username": r.username} for r in results]
        return make_object(results=results)

    def get_user(self, user_id, _not_found_error: bool=True):
        current_uid = self.api.current_user_id()
        add_fields = {}
        if user_id in {"self", current_uid}:
            user_id = current_uid
            # add in SSO values
            self._add_sso_info(add_fields)
        elif not self.api.has_permission(self._perm_manage_users):
            raise AccessDenied403(message="You can only see yourself.", private_details={
                "method": "get_user", "user": current_uid, "access_user": user_id
            })
        rec = self._lookup(user_id, fields=self._visible_fields, not_found_error=_not_found_error)
        if rec:
            rec._extend(add_fields)
        return rec

    def _get_user_password_hash(self, user_id):
        """
        Look up hashed password.  Obviously, this method is for internal, not public use.
        """
        return self._lookup(user_id, fields={"password": 1}).password

    def create_user(self, record: dict):
        # default to lowest role
        requested_role = record.get("role")
        if requested_role not in (self.api._role_names or []):
            if requested_role:
                raise BadRequest(message=f"Unrecognized role: '{requested_role}'")
            record = dict(record)
            record["role"] = self.api._role_names[0] if self.api._role_names else ""
            requested_role = None
        if requested_role and not self.api._disable_permissions:
            # no access to roles higher than one's own role
            cmp_role = self.api._cmp_role_names(requested_role, self.api.current_user_role())
            if cmp_role not in {0, -1}:
                raise AccessDenied403(
                    message="no access to role",
                    public_details={},
                    private_details={"method": "create_user", "user": self.api.current_user_id(), "role": requested_role}
                )
        user_id = self._create(record)
        if self._audit:
            self._audit(self.api, "create", user_id, record)
        return make_object(user_id=user_id)

    def mimic_role(self, role: str):
        """
        Temporarily change the current user's role to the same or a lesser role than what is assigned.
        """
        # get real role and ordered list of groups
        user_rec = self.get_user("self", _not_found_error=False)
        if not user_rec:
            return False
        real_role = user_rec.role
        roles = self.api._role_names
        if not roles or real_role not in roles or role not in roles:
            return False
        # verify role is lower than current role
        n_real = roles.index(real_role)
        n_req = roles.index(role)
        if n_req > n_real:
            return False
        # make the change to the session
        self.api.current_session().user_role = role
        return True

    def _check_user_id_access(self, user_id: str):
        """
        Verify the supplied user_id can be accessed by the currently logged in user.

        :returns:  A tuple of:
                        0) translated user_id
                        1) whether advanced permissions are available
        """
        if not user_id:
            raise BadRequest(message="invalid user_id")
        current_user_id = self.api.current_user_id()
        if user_id == "self":
            if not current_user_id:
                raise BadRequest(message="user_id='self' only works when logged in")
            user_id = current_user_id
        if not self.api.has_permission(self._perm_manage_users):
            if user_id != self.api.current_user_id():
                # no access to modify other user data
                raise AccessDenied403(private_details={"method": "update_user", "user": self.api.current_user_id()})
            return user_id, False
        return user_id, True

    def update_user(self, user_id: str, changes: dict):
        user_id, advanced_perms = self._check_user_id_access(user_id)
        if not advanced_perms:
            banned = set(changes) - {"email", "metadata", "password"}
            if banned:
                raise AccessDenied403(
                    message="no access to fields",
                    public_details={"fields": banned},
                    private_details={"method": "update_user", "user": self.api.current_user_id()}
                )
        if "role" in changes:
            if changes["role"] not in self.api._role_names:
                raise BadRequest(message=f"invalid role: {changes['role']}")
            requestor_role = self.api.current_user_role()
            cmp_role = self.api._cmp_role_names(changes["role"], requestor_role)
            if cmp_role not in {0, -1} and not self.api._disable_permissions:
                raise AccessDenied403(
                    message="no access to role",
                    public_details={},
                    private_details={"method": "update_user", "user": self.api.current_user_id(), "role": changes["role"]}
                )
        r = self._update(user_id, changes)
        if user_id == self.api.current_user_id():
            self._update_api_with_user_updates(changes)
        if self._audit:
            self._audit(self.api, "update", user_id, changes)
        return r

    def update_user_metadata(self, user_id: str, metadata: (dict, str)):
        """
        Update only metadata for a user, usually 'self'.
        """
        user_id, advanced_perms = self._check_user_id_access(user_id)
        if not isinstance(metadata, dict):
            # may be base64 encoded
            if metadata.startswith("enc:"):
                metadata = metadata[4:]
            metadata = json.loads(base64.b64decode(metadata.encode("utf-8")))
        changes = prepend_update(metadata, "metadata")
        r = self._update(user_id, changes)
        # TODO I think metadata changes do not merit auditing - delete if you agree
        #if self._audit:
        #    self._audit(self.api, "update", user_id, changes)
        return r

    def _update_api_with_user_updates(self, changes: dict):
        """
        Changes to certain fields need to be kept up to date in the current session.
        """
        if "email" in changes:
            self.api.current_session().user_email = changes["email"]
        if "username" in changes:
            self.api.current_session().user_name = changes["username"]
        if "role" in changes:
            self.api.current_session().user_role = changes["role"]

    def delete_user(self, user_id: str):
        old_rec = self.get_user(user_id)._to_json()
        if self._audit:
            self._audit(self.api, "delete", user_id, old_rec)
        resp = self._delete(user_id)
        # delete all associated sessions
        old_user_id = old_rec[ROW_ID]
        server = self.api.get_server()
        if server:
            server.session_handler.purge_old(filter=lambda rec: True if "user_id" not in rec else rec["user_id"] != old_user_id)
        return resp

    def _get_sso_config(self):
        cfg = self.api.get_config()
        return cfg.get_sso_config()

    def get_config(self):
        sso = self._get_sso_config()
        if sso:
            return make_object(
                sso_enabled=True,
                invitations=bool(sso.get("by_invitation"))
            )
        else:
            return make_object(sso_enabled=False)

    def get_sso_invited_users(self):
        """
        Get the list of invited users.
        """
        cfg = self.get_config()
        if cfg.sso_enabled and cfg.invitations:
            return make_object(invited=self._get_sso_invited_users(), enabled=True)
        else:
            return make_object(invited=[], enabled=False)

    def _get_sso_invited_users(self):
        out = {}
        # fetch from database
        db = self.api.get_config().get_db()
        invitees = list(db.query("config", {"_id": "invited"}))
        if invitees:
            from_db = invitees[0].get("value") or {}
            if isinstance(from_db, list):
                from_db = {v: {} for v in from_db}
            out.update(from_db)
        # add owner's sso username
        owner = self.api.get_config().owner_sso_username
        if owner:
            out[owner] = {"role": "ADMIN"}
        return out

    def set_sso_invited_users(self, invited: (list, dict)):
        """
        Store a list of invited users.
        """
        if not invited:
            invited = {}
        if isinstance(invited, list):
            invited = {v: {} for v in invited}
        jsonschema.validate(invited, USER_INVITE_SCHEMA)
        cfg = self.get_config()
        if cfg.sso_enabled and cfg.invitations:
            owner = self.api.get_config().owner_sso_username
            if owner:
                invited.pop(owner, None)
            db = self.api.get_config().get_db()
            db.replace("config", "invited", {"value": invited})
        else:
            raise BadRequest(message="SSO invitation is not enabled")
        return make_object()


def generate_user_category_class(perm_logged_in=None, perm_manage_users=None, perm_super_user=None, on_login: callable=None, audit: callable=None, validator=None, sequence=0):
    """
    Put together a standard user management and login module to add to an API.
    :param perm_logged_in:     Permission allowing access to any logged in user.  This should be a permission
                               associated with the lowest level role.
    :param perm_manage_users:  Permission to allow user management.
    :param on_login:           Method called when a new user logs in.
    :param audit:              Method called to audit user changes.
    :param validator:          JSON schema validation name - a filename appended to the schema folder for the API.
    :return:    User module to add to API.
    """
    class User(UserBase):
        """
        User management, login.
        """
        def __init__(self, api):
            super(User, self).__init__(
                api, on_login=on_login, audit=audit, perm_manage_users=perm_manage_users,
                perm_super_user=perm_super_user, validator=validator, sequence=sequence
            )

        @endpoint("post", "login", sequence=1, activity_analysis=_analyze_login)
        def login(self, username: str='', password: str=''):
            """
            Log in.
            :param username: User name, or None to verify an authorization token.
            :param password: Password, or authorization token.
            :param password: Password, or authorization token.
            :return:  "user" = user record
            """
            return super(User, self).login(username, password)

        @endpoint("post", "logout", sequence=2)
        def logout(self, session_ids: list=None, all: bool=False):
            """
            Log out the current session, or optionally log out other sessions owned by the currently logged in user.
            This only clears internal session information, which will not cause an SSO log out.
            When integrated with SSO, a URL is returned which can be used to log out the SSO session.  That session
            may cause all sessions belonging to the user to be logged out, so the usefulness of the 'session_ids'
            and 'all' parameters may be limited in some cases.

            :param session_ids: A list of session IDs to log out.
            :param all:         True to log out all sessions owned by the current user.
            """
            return super(User, self).logout(session_ids=session_ids, all=all)

        @endpoint("post", "recovery/start", sequence=5, activity_analysis=["email"])
        def start_recovery(self, email: str, recovery_time_limit: int=None):
            """
            Begin account recovery process.  If email is valid, user record is given a recovery code,
            and that code can be used to log in using recover_account().  Send the recovery code via email
            or another private channel.
            :param email:                   Email for account.
            :param recovery_time_limit:     How long to give them.  Reserved for future admin use, not implemented.
            """
            # TODO ADMIN could change recovery_time_limit, or this could be set by configuration
            found = super(User, self).start_recovery(email)
            if found:
                recovery_code, recovery_code_expires = found
                params = {
                    "url": self.api.get_config().get_external_url(),
                    "email": email,
                    "recovery_code": recovery_code,
                    "recovery_code_expires": recovery_code_expires
                }
                body_t = self.api.apply_template("email_account_recovery.body.txt", params)
                body_h = self.api.apply_template("email_account_recovery.body.html", params)
                subject = self.api.apply_template("email_account_recovery.subject.txt", params)
                emailer = self.api.emailer
                if not emailer:
                    raise GeneralError(code="email-not-configured", message="email not configured")
                msg = emailer.create_message(to=email, subject=subject, body=(body_t, body_h))
                emailer.send(msg)
            return make_object()

        @endpoint("post", "recovery/login", sequence=6, activity_analysis=["email"])
        def recover_account(self, email: str, recovery_code: str):
            """
            Log in using a recovery code.
            :param email:           Email for account.
            :param recovery_code:   Recovery code from start_recovery().
            :return:   recovered=whether recovered, user=user record
            """
            user_rec = super(User, self).recover_account(email, recovery_code)
            if user_rec:
                return make_object(recovered=True, user=user_rec)
            else:
                return make_object(recovered=False)

        @endpoint("get", "whoami", sequence=11, activity_analysis=False)
        def whoami(self):
            """
            Information about the current user and session.
            """
            return super(User, self).whoami()

        @endpoint("get", "sessions", permission_required=perm_logged_in, sequence=12, activity_analysis=False, update_session_timer=False)
        def my_sessions(self):
            """
            Information about the current user's sessions.
            """
            current_user_id = self.api.current_user_id()
            if current_user_id:
                sessions = super(User, self).query_sessions({"user_id": current_user_id})
                sessions = [{f: ssn.get(f) for f in INCLUDE_SESSION_FIELDS} for ssn in sessions]
                self._add_session_expiration_info(sessions)
                return make_object(results=sessions)

        @endpoint("get", "sessions/query", permission_required=perm_manage_users, sequence=13)
        def query_sessions(self, query: dict=None):
            """
            Examine current sessions.  This endpoint allows an administrator to see details about which users are
            logged in.
            """
            sessions = super(User, self).query_sessions(query)
            sessions = [{f: ssn.get(f) for f in INCLUDE_SESSION_FIELDS} for ssn in sessions]
            self._add_session_expiration_info(sessions)
            return make_object(results=sessions)

        def _add_session_expiration_info(self, sessions):
            t_now = time.time()
            for ssn in sessions:
                if "timestamp" in ssn and ssn.get("user_name"):
                    ssn["expires_in"] = self.api.get_config().session_idle_expiration - (t_now - ssn["timestamp"])

        @endpoint("get", "users", permission_required=perm_logged_in, sequence=14)
        def list_users(self, query: dict=None):
            """
            List all users.
            """
            return super(User, self).list_users(query)

        @endpoint("get", "users/{user_id}", permission_required=perm_logged_in, sequence=15, activity_analysis=_analyze_get_user)
        def get_user(self, user_id: str, _not_found_error: bool=True):
            """
            Get a particular user record, or 'self'.
            """
            return super(User, self).get_user(user_id, _not_found_error=_not_found_error)

        @endpoint("post", "users", permission_required=perm_manage_users, sequence=20, activity_analysis=_analyze_create_user)
        def create_user(self, record: dict):
            """
            Create a new user.
            """
            return super(User, self).create_user(record)

        @endpoint("put", "users/{user_id}", permission_required=perm_logged_in, sequence=21, activity_analysis=_analyze_update_user)
        def update_user(self, user_id: str, changes: dict):
            """
            Make changes to a user record.
            """
            return super(User, self).update_user(user_id, changes)

        @endpoint("put", "users/{user_id}/metadata", permission_required=perm_logged_in, sequence=21, activity_analysis=_analyze_update_user)
        def update_user_metadata(self, user_id: str, metadata: (dict, str)):
            """
            Make changes to user metadata only.
            """
            return super(User, self).update_user_metadata(user_id, metadata)

        @endpoint("delete", "users/{user_id}", permission_required=perm_manage_users, sequence=22, activity_analysis=["user_id"])
        def delete_user(self, user_id: str):
            """
            Delete a user record.
            """
            return super(User, self).delete_user(user_id)

        @endpoint("put", "users/self/mimic_role", permission_required=perm_logged_in, sequence=30, activity_analysis=["role"])
        def mimic_role(self, role: str):
            """
            Request a temporary change of role to something less or equal to one's assigned role.
            :param role:   New role which will stay in effect until the next login, or until the user record is
                updated.
            """
            ok = super(User, self).mimic_role(role)
            if not ok:
                raise BadRequest(message="invalid request")
            return make_object()

        @endpoint("get", "config", permission_required=perm_logged_in, sequence=101, activity_analysis=False)
        def get_sso_config(self):
            """
            SSO configuration.
            """
            return super(User, self).get_config()

        @endpoint("get", "sso_users", permission_required=perm_manage_users, sequence=102, activity_analysis=False)
        def get_sso_invited_users(self):
            """
            Get the list of usernames/emails that will be allowed in through SSO.
            @deprecated  - invitations are managed by the provisioner
            """
            return super(User, self).get_sso_invited_users()

        @endpoint("post", "sso_users", permission_required=perm_manage_users, sequence=103, activity_analysis=["invited"])
        def set_sso_invited_users(self, invited: (list, dict)):
            """
            Change the list of usernames/emails that can come in through SSO.

            @deprecated

            There is no longer any local storage of invitation information.
            """
            return super(User, self).set_sso_invited_users(invited)

    return User


def generate_user_category(api, **kwargs):
    """
    Goes one step further than generate_user_class() and instantiates the class.
    """
    cls = generate_user_category_class(**kwargs)
    return cls(api)


def generate_recovery_code():
    """
    Recovery codes for account recovery / reset password.
    """
    return str(uuid.uuid4()).replace("-", "")[:16]


def _analyze_login(output, **kwargs):
    out_user = output["user"]
    out = {}
    if "role" in out_user:
        out["role"] = out_user["role"]
    return out


def _analyze_get_user(params, **kwargs):
    if params.get("user_id") == "self":
        return None
    return {}


def _analyze_create_user(params, output, **kwargs):
    rec = params.get("record", {})
    return {
        "username": rec.get("username"),
        "email": rec.get("email"),
        "user_id": output["user_id"]
    }


def _analyze_update_user(params, **kwargs):
    changes = params.get("changes", {})
    changed_fields = list(changes.keys())
    if changed_fields == ["metadata"]:
        return
    out = {
        "user_id": params.get("user_id"),
        "changed_fields": changed_fields,
    }
    for f in ["role", "username", "email"]:
        if f in changes:
            out[f] = changes[f]
    return out


USER_INVITE_SCHEMA = {
    "comment": "invitation of users to a workbench: a mapping from username or email to details of the invitation",
    "type": "object",
    "patternProperties": {
        ".+": {
            "type": "object",
            "properties": {
                "role": {
                    "type": "string"
                }
            },
            "additionalProperties": False
        }
    }
}


# only these fields are listed from user sessions
INCLUDE_SESSION_FIELDS = ["_id", "timestamp", "user_name", "user_role", "user_email"]
