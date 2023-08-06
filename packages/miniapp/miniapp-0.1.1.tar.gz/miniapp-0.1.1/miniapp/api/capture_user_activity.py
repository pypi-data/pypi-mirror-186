"""
This module governs capture of all user activity through REST endpoints.  Details about each action are recorded in
a configurable location: database or logs.  Note that internal API calls are not recorded, only calls that come through
REST.

Every endpoint is responsible for choosing what should be logged here, and this is done through the "activity_analysis"
endpoint decorator parameter.

See Config.user_activity_* for configuration.
See api_user_activity for retrieval endpoint.
"""
from miniapp.errs import InternalError
from miniapp.utils.json_utils import gen_json_size_limiter
from miniapp.utils.misc import unobfuscate


def intercept_endpoints(server, api):
    """
    Dig all the useful information out of calls to the REST endpoints, toward the end of tracking what users
    do in potentially great detail.

    :param server:      The REST HTTP server receiving the calls.
    :param api:         The API to which the calls are delegated.
    """
    limit_size = gen_json_size_limiter()
    api_admin = api.admin_instance()
    user_activity = api_admin.find_category(has_methods=["record_activity", "aggregate_sessions"])
    if not user_activity:
        raise InternalError("Could not find 'user_activity' API category")

    def mon(method, request, function, kwargs=None, output=None):
        """ this is the function we plug in to track all activity """
        # 'analyzer' tells us what specifically to log for user activity
        analyzer = function.endpoint.activity_analysis if hasattr(function, "endpoint") else False
        # "False" means no logging at all
        if analyzer is False:
            return
        uid, sid = _get_override_uid_sid(request)
        if not analyzer:
            # None / default - no details
            analysis = {}
        elif analyzer == "*":
            # "*" means capture all arguments
            analysis = kwargs
        elif isinstance(analyzer, (list, tuple)):
            # 'analyzer' can be an iterable, which just captures input arguments
            analysis = {f: kwargs[f] for f in analyzer if f in kwargs}
        elif hasattr(analyzer, "__call__"):
            # custom method that can do whatever analysis it wants
            analysis = analyzer(
                request=request, function=function, params=kwargs, output=output, api=api
            )
        else:
            return
        # we want non-obfuscated values in our analyses
        # FIXME it would be better to request obfuscation in the endpoint than to test hardcoded parameter names
        #  - and it is too late here - should be done prior to calling analyzer()
        if "sql" in analysis:
            analysis["sql"] = unobfuscate(analysis["sql"])
        analysis = limit_size(analysis)
        user_activity.record_activity(username=uid, session_id=sid, endpoint=function.__name__, detail=analysis)
    server.monitor = mon


def _get_override_uid_sid(request):
    # FIXME clean this up
    """ checks for session/user information - for cases when an access token is being used """
    uid = sid = None
    rq_state = request.state
    # The data_access methods can be invoked without a session from a notebook, in which case
    # the token and context they pass are turned into comparable values for sid and uid.
    if "monitor.s" in rq_state:
        sid = rq_state["monitor.s"]
    if "monitor.u" in rq_state:
        uid = rq_state["monitor.u"]
    return uid, sid
