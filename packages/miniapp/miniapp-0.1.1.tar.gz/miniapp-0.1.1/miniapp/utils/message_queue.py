"""
Extremely simple message queue, or abstraction for same.
"""
import time
import threading
import uuid

from miniapp.data.const import ROW_ID


class MessageQueue(object):
    """
    A simple in-memory or persistent message queue.

    You can back this with a database but when the messages have a very short lifespan this may not be important.

    Uses include:
      - a background process wants to inform the user of something as it is running
      - an admin wants to send a message to all the users
      - system asynchronously detects the need for a user to enter some credentials or permission or whatever:
        + message is sent to user requesting the missing data
        + user replies with needed information
        + the waiting system process receives the message and continues
    """
    def __init__(self, db=None, collection="messages", max_age: float=3*60):
        """
        :param db:              Store messages in this database, if provided.
        :param collection:      Name of collection to use.
        :param max_age:         How long to let the messages live.  This only needs to be as long as the slowest
                                observer, i.e. if all listeners pick up their messages within 10 seconds the messages
                                do not have to live longer than that.
        """
        self._db = db
        self._collection = collection
        self._messages = []
        self.max_age = max_age
        self.prev_t = None
        self.MARKER_OFFSET = 1_600_000_000
        self.MARKER_SCALE = 1000000
        self.lock = threading.RLock()
        self._cleaning_thread = None
        self._auto_clean_tick = 5
        self._auto_clean_interval = 20
        self._shutdown = False
        # markers we produce are suffixed with a unique value to tell message generators apart
        self._my_id = hex(0x10000 + uuid.uuid4().int % 0xF0000)[2:]

    def stop(self):
        """
        Request shutdown of background threads.
        """
        self._shutdown = True

    def _marker(self) -> str:
        """
        Generate an always-ascending marker to identify each message.  We can't guarantee the ascendingness across
        servers but it's nice to have them in approximate order.
        """
        t = int(time.time() * self.MARKER_SCALE) / self.MARKER_SCALE
        if self.prev_t and t <= self.prev_t:
            t = self.prev_t + 1/self.MARKER_SCALE
        self.prev_t = t
        return self._marker_for_time(t)

    def _marker_for_time(self, t):
        return hex(int((t - self.MARKER_OFFSET)*self.MARKER_SCALE))[2:] + self._my_id

    def _current_marker(self):
        """
        A default marker that excludes prior messages.
        """
        t = self.prev_t or time.time()
        return self._marker_for_time(t + 1/self.MARKER_SCALE)

    def _get_messages(self, limit: int=None):
        if self._db:
            return [(rec.get(ROW_ID), rec) for rec in self._db.query(self._collection, limit=limit)]
        return self._messages

    def _add_message(self, marker, message):
        if self._db:
            msg_record = {ROW_ID: marker, **message}
            self._db.insert(self._collection, msg_record)
            return
        self._messages.append((marker, message))

    def last_marker(self):
        """
        Very last known marker / message ID.
        """
        if self._db:
            msgs = list(self._db.query(self._collection, fields=[], sort=((ROW_ID, -1),), limit=1))
            return msgs[0][ROW_ID] if msgs else None
        return self._messages[-1][0] if self._messages else None

    def clear(self):
        """
        Erase all messages.
        """
        if self._db:
            self._db.delete(self._collection, {})
        else:
            self._messages.clear()

    def clean(self):
        """
        Delete expired messages.
        """
        threshold = self._marker_for_time(time.time() - self.max_age)
        with self.lock:
            if self._db:
                self._db.delete(self._collection, {"id": {"$lt": threshold}})
            else:
                self._messages = self._recent(threshold)

    def is_empty(self):
        """
        Check for an empty queue.
        """
        return not self._get_messages(limit=1)

    def _recent(self, from_marker: str, message_filter: callable=None, reverse_order: bool=False, limit: int=0):
        """
        Gather all messages after a given marker.
        """
        with self.lock:
            msgs = self._get_messages()
            if reverse_order:
                msgs = reversed(msgs)
            msgs = filter(lambda msg: msg[0] > from_marker, msgs)
            if message_filter:
                msgs = filter(message_filter, msgs)
            return list(msgs) if not limit else list(msgs)[:limit]

    def read(self, from_marker: (str, int, float)=None, wait: float=None, message_filter: callable=None, check_interval: float=0.1, poll: callable=None, reverse_order: bool=False, limit: int=0):
        """
        Read recent messages.

        :param from_marker:     (str) > Marker for last message received.
                                None > don't include any old messages, return only new messages.
                                (int, float) > Return messages younger than this number of seconds.
        :param wait:            How long to wait for a new message.
        :param message_filter:  Limits messages to those of interest.
        :param check_interval:  How long to wait between checks for new messages.
        :param poll:            Method called while waiting.
        :param reverse_order:   Returns results most recent first.
        :param limit:           Maximum number of messages to return.
        :return:        A list of tuples: message ID and message content.
        """
        if not from_marker:
            from_marker = self._current_marker()
        if isinstance(from_marker, (int, float)):
            from_marker = self._marker_for_time(time.time() - from_marker)
        while wait and wait > 0:
            found = self._recent(from_marker, message_filter=message_filter, reverse_order=reverse_order, limit=limit)
            if found:
                return found
            if poll:
                poll()
            time.sleep(check_interval)
            wait -= check_interval
        return self._recent(from_marker, message_filter=message_filter, reverse_order=reverse_order, limit=limit)

    def add(self, message: dict):
        """
        Add a message to the queue.
        """
        with self.lock:
            self._add_message(self._marker(), message)
        self._auto_clean()

    def _auto_clean(self):
        """
        Delete expired messages in the background until the message queue is empty.
        """
        if self._auto_clean_interval <= 0:
            return
        delay_ticks = int(self._auto_clean_interval / self._auto_clean_tick)
        def checker():
            n = 0
            while True:
                time.sleep(self._auto_clean_tick)
                if self.is_empty() or self._shutdown:
                    break
                n += 1
                if n % delay_ticks:
                    self.clean()
            self._cleaning_thread = None
        # start the thread
        if self._cleaning_thread:
            return
        self._cleaning_thread = threading.Thread(target=checker, daemon=True, name="message_queue.auto_clean")
        self._cleaning_thread.start()
