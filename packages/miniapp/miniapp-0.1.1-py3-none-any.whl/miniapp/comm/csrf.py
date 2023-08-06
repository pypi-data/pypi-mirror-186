"""
CSRF support
"""
import uuid
import json
import time
import re

from miniapp.errs import AccessDenied403


class CSRF(object):
    def __init__(self, ignore_urls: (re.Pattern, str)=None):
        if isinstance(ignore_urls, str):
            ignore_urls = re.compile(ignore_urls)
        self.ignore_urls = ignore_urls

    def generate_token(self):
        """
        Generate a new, random token.
        """
        return str(uuid.uuid4()).replace("-", "")

    def post_param_name(self):
        """
        Name for POST/PUT parameter containing token.
        """
        return "csrf_token"

    def expiration_time(self):
        """
        Tokens expire after this long.
        """
        return 86400

    def refresh_margin(self):
        """
        We generate a token a little before the previous token expires.
        """
        return self.expiration_time()/3

    def keep_tokens(self):
        """
        We preserve several historical tokens to verify 'good faith'.
        """
        return 7

    def _get_session_tokens(self, request):
        """
        Get the list of tokens from the session.
        """
        try:
            raw = request.session.csrf_tokens
            if not raw:
                return
            tokens = json.loads(raw)
            if not isinstance(tokens, list):
                return
            return tokens
        except ValueError:
            return

    def _token_from_request(self, request):
        token = request.args.pop(self.post_param_name(), None) or ""
        if isinstance(token, list):
            return token[0]
        return token

    def _debug(self, message):
        # print(f"CSRF_DEBUG {message}")
        pass

    def establish_in_session(self, request):
        """
        Ensure that a request has a valid token, and return that token.
        """
        token = self._token_from_request(request)
        registered_tokens = self._get_session_tokens(request)
        t_now = time.time()
        # we can continue to use the current token up until it is about to expire
        for registered_token in (registered_tokens or []):
            if token == registered_token.get("token") and t_now < registered_token.get("expires") - self.refresh_margin():
                self._debug(f"s={request.session_id} re-using client token {token}, which expires in {registered_token.get('expires', 0) - t_now}s")
                return token
        # return current token if it is not just about to expire
        if registered_tokens and t_now < registered_tokens[-1].get("expires") - self.refresh_margin():
            self._debug(f"s={request.session_id} no client token, sending latest registered token {registered_tokens[-1]['token']}, which expires in {registered_tokens[-1].get('expires', 0) - t_now}s")
            return registered_tokens[-1]["token"]
        # generate a new token
        new_token = self.generate_token()
        if not registered_tokens:
            registered_tokens = request.session.csrf_tokens = []
        registered_tokens.append({"token": new_token, "expires": t_now + self.expiration_time()})
        registered_tokens = registered_tokens[-self.keep_tokens():]
        request.session.csrf_tokens = json.dumps(registered_tokens)
        self._debug(f"s={request.session_id} issuing new token {new_token}")
        return new_token

    def verify_request(self, request):
        """
        Verify that a request has a valid token.
        """
        if self.ignore_urls and self.ignore_urls.match(request.path):
            return
        token = self._token_from_request(request)
        registered_tokens = self._get_session_tokens(request)
        if not token or not registered_tokens:
            raise AccessDenied403(private_details={
                "csrf_missing": True, "token": token, "session": request.session_id
            })
        t_now = time.time()
        # if token does not match any historical token, log a violation
        if token not in {t["token"] for t in registered_tokens}:
            raise AccessDenied403(private_details={
                "csrf_violation": True, "token": token, "session": request.session_id
            })
        # check for a valid, non-expired token
        for registered_token in registered_tokens:
            if token == registered_token.get("token") and t_now < registered_token.get("expires"):
                return
        raise AccessDenied403(private_details={
                "csrf_expired": True, "token": token, "session": request.session_id
            })
