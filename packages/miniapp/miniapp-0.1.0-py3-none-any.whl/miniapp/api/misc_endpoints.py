from miniapp.data.impl import compile_query
from miniapp.errs import GeneralError
from miniapp.utils.generic_obj import make_object
from miniapp.utils.message_queue import MessageQueue


"""
Generate a message checking method.
"""
def check_for_messages(api, message_queue: MessageQueue, require_login: bool=True, message_trimmer: callable=None,
                       last_marker: (int, str) = None, wait: float = None, query: dict = None, limit: int = 0):
    """
    Check for, or wait for messages.  Note that only messages targeting the current user (or all users)
    will be considered, along with whatever restrictions are given in 'query', so 'wait' will wait
    until a message matching those criteria is generated.

    :param last_marker:     ID of most recently received message.  No messages before or equal will be returned.
                            If omitted, no messages from the past are included.  Specify an integer to return
                            all messages in the last (n) seconds.  Note that only a few minutes worth of messages
                            are retained.
    :param wait:            How long to wait for a new message.
    :param query:           Filters to apply.
    :param limit:           If specified, only the most (n) recent matching messages are returned (most recent
                            first).  Normally messages are returned in time ascending order.  Specifying a limit
                            reverses this.
    :return:    results = list of (id, message)  List is blank on timeout.
                last_marker = ID of last known message.
    """
    user_ids = (api.current_username(), api.current_user_id())
    session_id = api.current_session_id()
    compiled_query = compile_query(query)

    def filt(msg):
        """ restrict which messages to include """
        if not compiled_query(msg[1]):
            return False
        for_sid = msg[1].get("session_id")
        if for_sid and for_sid != session_id:
            return False
        return msg[1].get("user", user_ids[0]) in user_ids

    def poll():
        """ method called while waiting - detects logout """
        user_id = api.current_user_id()
        if not user_id and require_login:
            raise GeneralError(code="logged-out", message="Logout occurred")

    msgs = message_queue.read(
        from_marker=last_marker,
        wait=wait,
        message_filter=filt,
        poll=poll,
        reverse_order=bool(limit),
        limit=limit
    )
    if message_trimmer:
        msgs = list(map(message_trimmer, msgs))
    if msgs and not limit:
        last_marker = msgs[-1][0]
    else:
        last_marker = message_queue.last_marker()
    return make_object(results=msgs, last_marker=last_marker)
