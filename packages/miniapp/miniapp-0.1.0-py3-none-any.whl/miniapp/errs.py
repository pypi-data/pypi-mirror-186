import traceback
import collections
import uuid
import json
import re

PTN_REGEX_MSG = re.compile(r"^'(.*)' does not match '(.*?)'$")


class GeneralError(Exception):
    """
    Base class for HTTP errors.
    """
    def __init__(self, code: str, message: str=None, http_code: int=500, public_details: dict=None, private_details: dict=None, tracking_code: str=None, **kwargs):
        self.code = code
        self.message = message
        self.public_details = dict(public_details or {})
        self.private_details = dict(private_details or {})
        self.http_code = http_code
        if kwargs:
            self.public_details.update(kwargs)
        # a tracking code which allows private details to be found
        tracking_code = str(uuid.uuid4()).replace("-", "")[:12] if tracking_code is None else tracking_code
        if tracking_code:
            self.private_details["_"] = tracking_code
            self.public_details["_"] = tracking_code

    def remove_tracking_code(self):
        self.public_details.pop("_", None)
        self.private_details.pop("_", None)

    def to_json(self, include_private_details: bool=False, include_tracking_code: bool=True):
        out = collections.OrderedDict()
        out["code"] = self.code
        if self.message:
            out["message"] = self.message
        if self.public_details:
            out.update(self.public_details)
        if include_private_details and self.private_details:
            out.update(self.private_details)
        if not include_tracking_code:
            out.pop("_", None)
        return out

    def has_private_details(self):
        """
        Determine whether there is any private information that needs to be logged and cannot be shown
        to the caller.
        """
        return bool(set(self.private_details.keys()) - {"_"})

    def http_response(self):
        """
        Return content, mime type and http code.
        """
        detail = self.to_json()
        detail["ok"] = False
        try:
            detail_s = json.dumps(detail)
            return (detail_s, "application/json"), self.http_code
        except TypeError as err:
            j_err = GeneralError(code="internal-error", private_details={"message": "Non-json-serializable output", "error": str(err), "detail": repr(detail)})
            print(j_err.to_log())
            return (json.dumps(j_err.to_json(include_tracking_code=True)), "application/json"), 500

    def to_log(self) -> str:
        """
        Render for logging.
        """
        out = self.to_json(include_private_details=True)
        return json.dumps(out)

    def add_public_detail(self, name: str, value):
        self.public_details[name] = value

    @staticmethod
    def validation_error(err, schema_name):
        if not hasattr(err, "schema_path"):
            return err
        schema_path = list(err.schema_path)
        context = list(err.path)
        if err.schema_path[-1] == "pattern":
            msg = PTN_REGEX_MSG.match(err.message)
            if msg:
                value = msg.group(1)
                if len(value) > 50:
                    value = value[:50] + "..."
                return GeneralError(
                    code="validation-error-regex",
                    message=f"Field '{context[-1]}' has invalid characters or is in the wrong format or is too long",
                    public_details={
                        "value": value, "regex": msg.group(2), "schema_name": schema_name,
                        "field": context[-1], "schema_path": schema_path, "context": context
                    }
                )
        return GeneralError(
            code="validation-error_%s" % schema_name,
            message="%s validation failure: %s" % (schema_name, err.message),
            public_details={"schema_path": schema_path, "context": context})

    def __str__(self):
        out = str(self.code)
        if self.message:
            out += ": %s" % self.message
        return out


class Unauthorized401(GeneralError):
    """
    Not logged in.
    """
    def __init__(self, private_details: dict=None, public_details: dict=None):
        private_details = dict(private_details or {})
        private_details["trace"] = traceback.format_stack()
        super(Unauthorized401, self).__init__(
            code="unauthorized", message="Unauthorized", http_code=401,
            private_details=private_details, public_details=public_details
        )


class BadRequest(GeneralError):
    """
    Invalid request to REST endpoint.
    """
    def __init__(self, code: str="invalid-parameters", message: str=None, private_details=None, **kwargs):
        super(BadRequest, self).__init__(
            code=code, message=message, http_code=400,
            private_details=private_details,
            public_details=kwargs
        )


class AccessDenied403(GeneralError):
    """
    No permission.
    """
    def __init__(self, public_details: dict=None, private_details: dict=None, message: str=None, code: str="access-denied"):
        private_details = dict(private_details or {})
        private_details["trace"] = traceback.format_stack()
        super(AccessDenied403, self).__init__(
            code=code, message=message or "Access denied", http_code=403,
            public_details=public_details,
            private_details=private_details
        )


class ReportedException(GeneralError):
    """
    Wrapper for reporting unexpected exceptions.
    """
    def __init__(self, exception: Exception, code: str=None, message: str=None, public_details: dict=None, private_details: dict=None):
        detail = {
            "exception": repr(exception),
            # TODO format this with wbcommon.misc.traceback_to_json(), but beware of recursive module dependencies
            "trace": traceback.format_tb(exception.__traceback__),
            **(private_details or {})
        }
        # dig into exception properties and report as many as we can
        for prop in dir(exception):
            if prop.startswith("_"):
                continue
            try:
                v = getattr(exception, prop)
                if hasattr(v, "__call__"):
                    continue
                # coerce to valid JSON or skip
                detail[prop] = json.loads(json.dumps(v))
            except:
                pass
        super(ReportedException, self).__init__(
            code=code or "internal-error",
            http_code=500,
            message=message,
            private_details=detail,
            public_details=public_details
        )


class InternalError(GeneralError):
    """
    Failures that are probably due to coding problems.
    """
    def __init__(self, message: str=None, public_details=None, private_details=None):
        super(InternalError, self).__init__(
            code="internal-error",
            private_details={
                "message": message,
                "trace": traceback.format_stack()[:-1],
                **(private_details or {})
            },
            public_details=public_details
        )


class GeneralHttpError(GeneralError):
    """
    Transmit general HTTP error information.
    """
    def __init__(self, http_code=500, message="", mimetype="text/plain", code="other", **kwargs):
        super(GeneralHttpError, self).__init__(code=code, message=message, http_code=http_code, **kwargs)
        self.mimetype = mimetype

    def http_response(self):
        return (self.message, self.mimetype), self.http_code


def wrap_exception(exception):
    """
    Coerce exceptions into one of the sort we understand.
    """
    # special case, expose out-of-memory error to user rather than filing away a stack trace
    if isinstance(exception, OSError) and exception.errno == 12:
        return GeneralError(code="out-of-memory", message="Out of memory", private_details={"cause": str(exception)})
    # all other unrecognized exceptions get wrapped like so
    if not hasattr(exception, "to_log") or not hasattr(exception, "http_response"):
        return ReportedException(exception=exception)
    # already a type we understand
    return exception
