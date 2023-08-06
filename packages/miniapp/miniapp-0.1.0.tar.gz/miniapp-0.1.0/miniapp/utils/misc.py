import base64
import hashlib
import re
import io
import sys
import time
import json
import datetime
from collections import namedtuple, OrderedDict
import dateutil.parser
import string
import secrets
from urllib.parse import urlparse, unquote, quote, urlunparse

PTN_QUOTE = re.compile(r'%[0-9a-fA-F][0-9a-fA-F]')
PTN_EMAIL = re.compile(r'[a-zA-Z0-9_\-.!]{1,100}@[a-zA-Z0-9_\-.]{1,100}')
PTN_UUID = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
PTN_URL_PARTS = re.compile(r'^(.*://)?([^:/]+)(:(\d+))?(/.*)?$')

ISO_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
ISO_DATE_FORMAT = "%Y-%m-%d"

# ssh-based source control URI
# NOTE: gitlab also allows emojis in project names
PTN_SSH = re.compile(r'^(ssh://)?([a-z0-9]+)@([A-Za-z0-9\-.]+(:\d+)?):([A-Za-z0-9\-./_]+)$')
# url with no protocol, and where host is the default
PTN_HOST_ONLY = re.compile(r'^(?![a-z]+://)([^/]+?(:\d+)?)(/([^:@]*))?$')
# for split_url()
T_URL = namedtuple("UrlParts", "scheme user pwd host path", rename=True)


def _md5(s):
    """
    MD5 can no longer be considered secure for passwords but it IS a good general purpose hashing mechanism
    for many other uses.  Please call fast_informal_hash() instead to make it clear that the usage does not
    violate security policies.
    """
    if isinstance(s, str):
        s = s.encode("UTF-8")
    return hashlib.md5(s).hexdigest()


def fast_informal_hash(s):
    """
    Use this method to quickly obtain a reasonably unique and random hash value.

    DO NOT USE FOR CIPHERS, PASSWORDS, ETC..
    """
    return _md5(s)


def split_url(url: str, omit_password: bool=False, host_default: bool=False):
    """
    Similar to urllib.parse.urlparse(), only with username and password support, and some special logic for ssh URLs.
    """
    url = url or ""
    # ssh protocol
    m = PTN_SSH.match(url)
    if m is not None:
        return T_URL(scheme="ssh", user=m.group(2), pwd="", host=m.group(3), path=m.group(5))
    # special case that assumes simple strings like 'abc' are a hostname, not a path
    elif host_default and PTN_HOST_ONLY.match(url) is not None:
        m = PTN_HOST_ONLY.match(url)
        parts = T_URL(scheme="", user="", pwd="", host=m.group(1), path=m.group(4))
        scheme = ""
        host = parts.host
        path = parts.path or ""
    else:
        # full URL split
        parts = urlparse(url)
        scheme = parts.scheme
        host = parts.netloc
        path = parts.path
    # split out username & password
    user = pwd = ""
    if "@" in host:
        # NOTE: '@' can occur in 'user'
        u_p, host = re.split(r'@(?!.*@)', host)
        if ":" in u_p:
            user, pwd = u_p.split(":")
        else:
            user, pwd = u_p, ""
    if omit_password:
        pwd = "****"
    return T_URL(scheme, unquote(user), unquote(pwd), host, path)


def join_url(parts: T_URL) -> str:
    """
    Similar to urllib.parse.urlunparse(), only with support for username and password field.
    """
    if parts.user and parts.pwd:
        netloc = "%s:%s@%s" % (quote(parts.user).replace("%40", "@"), quote(parts.pwd), parts.host)
    elif parts.user:
        netloc = "%s@%s" % (quote(parts.user).replace("%40", "@"), parts.host)
    else:
        netloc = parts.host
    return urlunparse((parts.scheme, netloc, parts.path, '', '', ''))


def hostname_from_url(uri: str, incl_creds: bool=False, incl_port: bool=False) -> str:
    """
    Parse the hostname only out of various URIs.
    """
    parts = split_url(uri, host_default=True)
    host = parts.host
    if not incl_port and ":" in host:
        host = host.split(":")[0]
    if incl_creds and (parts.user or parts.pwd):
        creds = quote(parts.user or '').replace("%40", "@")
        if parts.pwd and creds:
            creds += ":"
        creds += quote(parts.pwd or '')
        host = creds + "@" + host
    return host


def is_valid_email(email):
    if not email:
        return False
    return PTN_EMAIL.match(email) is not None


def is_uuid(s: str) -> bool:
    """
    Check for a UUID.
    """
    if not s or not isinstance(s, str):
        return False
    return PTN_UUID.match(s) is not None


def scrub_passwords(s):
    """
    Detect and scrub possible passwords from a string.  Cases:
      * URI containing a password
    """
    if not s:
        return s
    if isinstance(s, list):
        return [scrub_passwords(s_n) for s_n in s]
    if isinstance(s, tuple):
        return tuple(scrub_passwords(s_n) for s_n in s)
    if s.startswith("--from-literal="):
        return '='.join(s.split("=")[:2]) + "=..."
    s = re.sub(r'([a-z]+://)([^@/:\s]+:)([^@/:]+)(@)', r'\1\2****\4', s, flags=re.DOTALL)
    return s


def _to_time_tuple(dt):
    if not dt:
        return
    if isinstance(dt, (int, float)):
        return time.gmtime(dt)
    elif isinstance(dt, tuple):
        return dt
    elif isinstance(dt, (datetime.datetime, datetime.date)):
        return dt.timetuple()
    elif isinstance(dt, str):
        return time.gmtime(parse_iso_datetime(dt))
    else:
        return


def _to_time_number(dt):
    if isinstance(dt, (int, float)):
        return dt
    elif isinstance(dt, tuple):
        return time.mktime(dt)
    elif isinstance(dt, (datetime.datetime, datetime.date)):
        return dt.timestamp()
    else:
        return


def format_iso_datetime(dt) -> (str, None):
    t_tuple = _to_time_tuple(dt)
    if t_tuple:
        return time.strftime(ISO_DATETIME_FORMAT, t_tuple)


def format_iso_date(dt) -> (str, None):
    t_tuple = _to_time_tuple(dt)
    if t_tuple:
        return time.strftime(ISO_DATE_FORMAT, t_tuple)


def parse_iso_datetime(v: (str, float, datetime.datetime), ignore_error: bool=False):
    """
    Parse date/time formats and produce a date number in time.time() format (seconds past 1970).
    """
    if not isinstance(v, str):
        return _to_time_number(v)
    try:
        dt = dateutil.parser.parse(v.upper(), ignoretz=True)
        return (dt - datetime.datetime(1970, 1, 1)).total_seconds()
    except Exception:
        if ignore_error:
            return
        raise


def capture_io(to_run, *args, capture_exception: bool=False, **kwargs):
    """
    Run a function and capture stdout/stderr.
    :param to_run:      Function to execute.
    :param args:        Positional arguments.
    :param capture_exception: True to capture exceptions, False to raise exceptions.
    :param kwargs:      Named arguments.
    :return:   A namedtuple with 'return_value', 'stdout', 'stderr', 'exception'.
    """
    RET = namedtuple("Captured", "return_value stdout stderr exception")
    t_o, t_e = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = io.StringIO(), io.StringIO()
    ret = exc = None
    try:
        ret = to_run(*args, **kwargs)
    except Exception as err:
        exc = err
        if not capture_exception:
            raise
    finally:
        r_o, r_e = sys.stdout.getvalue(), sys.stderr.getvalue()
        sys.stdout, sys.stderr = t_o, t_e
    return RET(ret, r_o, r_e, exc)


def apply_cache(getter: callable, key, cache):
    """
    Very simple shorthand for applying caching.
    :param getter:      The expensive method to cache.
    :param key:         Key for storage in cache.
    :param cache:       Cache, with get() and __setitem__() methods.
    :return:            Value, either from cache or from getter.
    """
    from_cache = cache.get(key)
    if from_cache is not None:
        return from_cache
    fresh = getter()
    cache[key] = fresh
    return fresh


def random_password(allowed_punct: str=None):
    """
    Random gibberish-laden password.
    """
    rand_gen = secrets.SystemRandom()
    chars = string.digits + string.ascii_letters + (allowed_punct if allowed_punct is not None else "._-!@#$^&*|/:;+=?")
    return "".join(rand_gen.choice(chars) for _ in range(10))


def binary_search(indexable, value, key: callable=None):
    """
    Find the index of a given value amidst sorted values.
    :param indexable:       A sorted list of values that supports len() and [].
    :param value:           Value to find within the list.
    :param key:             A lambda that extracts the sort value.
    :return:    A tuple with the index of a less or equal match, and a boolean: True=exact match, False=lower item found
    """
    key = key or (lambda x: x)
    lo = 0
    hi = len(indexable)
    if not hi:
        return -1, False
    while True:
        mid = (lo + hi) // 2
        v_mid = key(indexable[mid])
        if value == v_mid:
            return mid, True
        if value > v_mid:
            lo = mid + (lo == mid)
            if lo >= hi:
                return mid, False
        else:
            hi = mid
            if hi <= lo:
                return hi-1, False


def dedup_ordered_list(values):
    """
    Remove duplicates from a list without changing its order.
    """
    return list(OrderedDict((u, None) for u in values if u))


def consistent_hash_key(value):
    """
    Make a complex value consistent for use as a key in a cache, then turn it into a string, then take its hash.
    """
    def consistent(value):
        if isinstance(value, dict):
            return {k: consistent(v) for k, v in value.items()}
        if isinstance(value, set):
            return list(sorted(map(consistent, value)))
        if isinstance(value, (list, tuple)):
            return list(map(consistent, value))
        if isinstance(value, (bytes, bytearray)):
            return value.decode("utf-8", errors="ignore")
        return value
    v_str = json.dumps(consistent(value), sort_keys=True)
    return fast_informal_hash(v_str)


class frozendict(dict):
    """
    A {} that cannot be changed.
    """
    def _mod(self):
        raise Exception("Attempted to modify 'frozendict'")

    def __setitem__(self, key, value):
        self._mod()

    def pop(self, k):
        self._mod()

    def popitem(self):
        self._mod()

    def update(self, m, **kwargs):
        self._mod()

    def clear(self):
        self._mod()

    def __delitem__(self, key):
        self._mod()


def detect_xss(s):
    """
    Detect unsafe HTML.
    """
    if not s or "<" not in s:
        return False
    PTN_BAD_TAGS = re.compile(r'</?(script|frameset|iframe|object|applet)\b[^>]*>', re.IGNORECASE)
    PTN_BAD_ATTRS = re.compile(r'<[a-z0-9]+\s[^>]*\b(on[a-z]+)=[^>]*(>|$)', re.IGNORECASE)
    PTN_SCRIPT_INSERTION = re.compile(r'<[a-z0-9]+[^>]*\$\s*\{[^>]*(>|$)')
    if PTN_BAD_TAGS.search(s) or PTN_BAD_ATTRS.search(s) or PTN_SCRIPT_INSERTION.search(s):
        return True
    return False


def wrap_with_retries(runner, n_tries: int=3, delay_s: float=4, delay_backoff: float=2):
    """
    Apply retry with delays.
    """
    n_try = n_tries
    while True:
        try:
            return runner()
        except Exception:
            n_try -= 1
            if n_try < 0:
                raise
            time.sleep(delay_s)
            delay_s *= delay_backoff


def closest_strings(match: str, strings: (list, tuple), limit: int=3):
    """
    Return the most likely matches.
    """
    if len(strings) <= limit:
        return strings
    ptn_norm = re.compile(r'[^a-zA-Z0-9]')
    def normalize(s):
        return ptn_norm.sub('', s).lower()
    def closeness(a, b):
        if a == b:
            return 110
        if a.lower() == b.lower():
            return 109
        n_a = normalize(a)
        n_b = normalize(b)
        if n_a == n_b:
            return 108
        if n_b.startswith(n_a):
            return 50 + len(n_a) * 50 // len(n_b)
        if n_a in n_b:
            return 20 + len(n_a) * 30 // len(n_b)
        if n_b in n_a:
            return 5 + len(n_b) * 15 // len(n_a)
        return 0
    w_v = [(closeness(match, s), s) for s in strings]
    w_v.sort(reverse=True)
    return [w_v[n][1] for n in range(limit)]


def destream(source, close: bool=True, as_type=None):
    """
    Get data, where 'source' may be data, or a stream.
    """
    if hasattr(source, "read"):
        out = source.read()
        if close:
            source.close()
    else:
        out = source
    if as_type == str and not isinstance(out, str):
        out = out.decode("utf-8")
    elif as_type == bytes and not isinstance(out, (bytes, bytearray)):
        out = out.encode("utf-8")
    return out


def quote_once(s: str) -> str:
    """
    Quote a string, but only if it has not already been url-encoded.
    """
    if PTN_QUOTE.search(s):
        # normalize quoting to always be upper case
        while True:
            m = re.search(r'%([a-f][0-9A-F]|[0-9A-F][a-f]|[a-f][a-f])', s)
            if not m:
                break
            s = s[:m.start()] + s[m.start():m.end()].upper() + s[m.end():]
        return s
    return quote(s)


def obfuscate(s):
    """
    Mask data to prevent misinterpretation.

    Pragmatic reason: some firewalls inspect the data submitted by a browser and prevent transfer of such things as
    SQL commands, code snippets, and so on.  This is very undesirable behavior for applications built for developers
    who regularly need to work with such data, or for certain advanced administrative functions.

    Main use: Client (javascript) obfuscates user-entered, code-like fields before posting to REST.  REST endpoint
    calls unobfuscate() to return data to its original state.
    """
    if isinstance(s, str):
        s = s.encode("utf-8")
    return f"enc:{base64.b64encode(s).decode('utf-8')}"


def unobfuscate(s):
    """
    Decode obfuscated data.  Supports the format produced by obfuscate() and also ordinary data URIs.
    """
    if not s:
        return s
    if s.startswith("data:"):
        b = base64.b64decode(s.split(",")[1])
        return b.decode("utf-8")
    if s.startswith("enc:"):
        b = base64.b64decode(s.split(":", maxsplit=1)[1])
        return b.decode("utf-8")
    return s
