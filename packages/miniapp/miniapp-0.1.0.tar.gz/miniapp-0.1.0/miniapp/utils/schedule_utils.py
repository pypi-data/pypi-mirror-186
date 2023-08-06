"""
Scheduling basics.
"""
# TODO support cron format - https://www.ibm.com/docs/en/db2oc?topic=task-unix-cron-format
from datetime import datetime, timezone, timedelta
import dateutil.parser
import pytz
import re
import tzlocal

from miniapp.utils.lru_cache import LruCache

GMT = datetime.strptime("+00:00", "%z").tzinfo
PTN_DATE_ONLY = re.compile(r'^\s*(\d+|[a-zA-Z]+)[-/., ]+(\d+|[a-zA-Z]+)([-/., ]+\d+)?\s*$')


class Schedule(object):
    def __init__(
            self, start_time: (str, float)=None, end_time: (str, float)=None, interval: (str, float)=None,
            time_ranges: list=None, time_zone=None, priority: int=None
    ):
        """
        Defines a schedule for an event or condition.

        An event is something which is supposed to happen at a particular point in time, like running a job.  An
        instance of this class could represent 6am every morning.
        * Schedule(interval="day", time_ranges=[(6*3600, None)])
        * occurs(t0, t1) - if I am a job executor I can test a series of time ranges to know whether I should run this
          event.

        A condition is true at some times and false at other times.  For example an instance of this class could
        represent "normal working hours".
        * Schedule(interval="week", time_ranges=[(86400*dow+9*3600, 86400*dow+17*3600) for dow in range(1, 6)
        * on(t) - determine whether a given time is within working hours.

        This logic only does time computations, it does nothing related to job execution itself.

        Important methods:
        * from_json(), to_json() - persist a schedule as JSON.
        * description() - give a verbal description of a schedule.
        * occurs(t0, t1) - does the event (or the start time of a condition) occur within this time range?
        * on(t) - is the condition true at this time?
        * find_transitions() - find times within a range that the event occurs or the condition changes
        * intervals_in_range() - find the days, weeks, months, etc. for a schedule

        :param start_time:          Overall start time.
        :param end_time:            Overall end time.  We consider this an 'inclusive date' when a date is specified.
        :param interval:            Repeats from start time on this interval (days, 0=no repeat, or see constants in code).
        :param time_ranges:         Start/stop offsets within each interval (if given) or in absolute terms.
        :param time_zone:           Time zone for interpreting interval.  Name of a timezone, a timezone object, or None for system default.
        :param priority:            Used to resolve conflicts when more than one schedule is in effect at once.
        """
        if isinstance(time_zone, str):
            if time_zone[0] in {"+", "-"}:
                self.time_zone = datetime.strptime(time_zone, "%z").tzinfo
            elif time_zone.lower() == "system":
                self.time_zone = system_timezone()
            else:
                self.time_zone = pytz.timezone(time_zone)
        elif isinstance(time_zone, timezone):
            self.time_zone = time_zone
        else:
            # GMT as default
            self.time_zone = pytz.timezone("GMT")
        self.start_time = self._parse(start_time)
        self.end_time = self._parse(end_time, inclusive_date=True)
        if isinstance(interval, str):
            interval = interval.lower()
            if interval in {"hour", "hours", "hr", "hrs", "hourly"}:
                interval = 3600
            elif interval in {"day", "days", "daily"}:
                interval = 86400
            elif interval in {"week", "weeks", "weekly"}:
                interval = 7 * 86400
            elif interval in {"month", "months", "monthly"}:
                interval = 30*86400
            else:
                raise ValueError("unrecognized interval: %s" % interval)
        self.interval = interval
        if time_ranges:
            time_ranges = [(self._parse(start), self._parse(end)) for start, end in time_ranges]
        self.time_ranges = time_ranges
        self.priority = priority

    @staticmethod
    def from_json(json_data: dict):
        return Schedule(**json_data)

    def _parse(self, time_value, inclusive_date: bool=False):
        if isinstance(time_value, str):
            now = datetime.now()
            out = cached_date_parse(now.year, time_value, self.time_zone)
            if inclusive_date and PTN_DATE_ONLY.match(time_value):
                out += 86400
            return out
        if isinstance(time_value, float):
            return int(round(time_value))
        return time_value

    def _format(self, time_number: float, date_only: bool=False):
        dt = datetime.fromtimestamp(time_number, tz=self.time_zone)
        out = dt.strftime("%Y/%m/%d %H:%M")
        if out.endswith(" 00:00") or date_only:
            out = out.split(" ")[0]
        return out

    @staticmethod
    def _format_delta(delta):
        if delta.seconds == 0:
            return "%dd" % delta.days
        if delta.days == 0:
            return str(delta)
        return "%dd %s" % (delta.days, timedelta(seconds=delta.total_seconds() % 86400))

    def _is_null(self):
        return not self.start_time and not self.end_time and not self.time_ranges

    def to_json(self):
        out = {
        }
        for f in ["start_time", "end_time", "interval", "time_ranges"]:
            if getattr(self, f):
                out[f] = getattr(self, f)
        if self.time_zone:
            tz = str(self.time_zone)
            if tz.startswith("UTC") and len(tz) > 3:
                tz = tz[3:]
            out["time_zone"] = tz
        return out

    def t_interval(self, t: float):
        """
        Find time relative to the selected interval.
        """
        t_rel = t
        if self.interval:
            if self.interval == 7*86400:
                # for weeks, adjust t_rel to start on a Sunday
                t_rel -= 3*86400
            if self.interval % 86400 == 0:
                tz = self.time_zone
                offset = tz.utcoffset(datetime.fromtimestamp(t)).total_seconds()
                t_rel += offset
            if self.interval == 86400 * 30:
                # months
                tz = self.time_zone
                dt0 = datetime.fromtimestamp(t, tz).replace(day=1)
                t_rel = t - dt0.timestamp()
            else:
                # all other intervals
                t_rel %= self.interval
        return t_rel

    def next_interval(self, t: float):
        """
        Find the next interval time after a given starting time.
        """
        if self.interval == 86400 * 30:
            tz = self.time_zone
            dt0 = datetime.fromtimestamp(t, tz)
            dt1 = dt0.replace(year=dt0.year if dt0.month < 12 else dt0.year+1, month=dt0.month+1 if dt0.month < 12 else 1, day=1)
            return dt1.timestamp()
        elif self.interval:
            return t + self.interval

    def intervals_in_range(self, start_time: (int, float), end_time: (int, float), limit=100):
        """
        Break a time range into intervals, rounding up to cover the whole range.
        """
        t0 = start_time - self.t_interval(start_time)
        if not self.interval:
            return
        i = 0
        while i < limit:
            t1 = self.next_interval(t0)
            yield (t0, t1)
            if t1 >= end_time:
                break
            t0 = t1
            i += 1

    def description(self):
        """ Describe a schedule. """
        if self._is_null():
            return "no schedule"
        parts = []
        if self.start_time:
            parts.append("Start: " + self._format(self.start_time))
        if self.end_time:
            parts.append("End: " + self._format(self.end_time))
        if self.interval and self.time_ranges:
            i = {86400: "Daily", 7*86400: "Weekly", 30*86400: "Monthly", 3600: "Hourly"}.get(self.interval, "%.1fd" % (self.interval/86400))
            tr_parts = []
            for start, end in self.time_ranges:
                # TODO special cases for weekly, monthly
                tr_parts.append("%s-%s" % (self._format_delta(timedelta(seconds=start)), self._format_delta(timedelta(seconds=end))))
            parts.append("%s (%s)" % (i, ", ".join(tr_parts)))
        if not self.interval and self.time_ranges:
            tr_parts = []
            for start, end in self.time_ranges:
                tr_parts.append("%s-%s".format(self._format(start), self._format(end)))
            parts.append(" + ".join(tr_parts))
        return ", ".join(parts)

    def on(self, t: float):
        """
        Determine whether the condition is supposed to be true at this time.
        """
        if self._is_null():
            return False
        # time must be within overall bounds
        if self.start_time and t < self.start_time:
            return False
        if self.end_time and t >= self.end_time:
            return False
        # no interval: just check the time ranges
        if not self.interval and self.time_ranges:
            return self._on_ranges(t)
        # interval with time ranges
        if self.interval and self.time_ranges:
            return self._on_interval(t)
        # no further restrictions
        return True

    def _on_ranges(self, t: float):
        for range_start, range_end in self.time_ranges:
            if range_start <= t < range_end:
                return True
        return False

    def _on_interval(self, t: float):
        t_rel = self.t_interval(t)
        for range_start, range_end in self.time_ranges:
            if range_start <= t_rel < range_end:
                return True
        return False

    def occurs(self, t0: float, t1: float):
        """
        Determine whether an event occurs within the given time range.
        """
        if not self.start_time and not self.end_time and not self.interval and not self.time_ranges:
            return False
        # time must be within overall bounds
        if self.start_time and t1 < self.start_time:
            return False
        if self.end_time and t0 >= self.end_time:
            return False
        # no interval: just check the time ranges
        if not self.interval and self.time_ranges:
            return self._occurs_time_ranges(t0, t1)
        # interval with no time ranges
        if self.interval and not self.time_ranges:
            return self._occurs_interval_only(t0, t1)
        # interval with time ranges
        if self.interval and self.time_ranges:
            return self._occurs_interval_ranges(t0, t1)
        # with no interval or time ranges there is only one occurrence
        if not self.start_time or t0 > self.start_time:
            return False
        # no further restrictions
        return True

    def _occurs_time_ranges(self, t0: float, t1: float):
        for range_start, range_end in self.time_ranges:
            if t0 <= range_start <= t1:
                return True
        return False

    def _occurs_interval_only(self, t0: float, t1: float):
        # if more than one interval is crossed, we trigger
        if t1 - t0 >= self.interval:
            return True
        # trigger when t0 and t1 are in different intervals
        r = self.t_interval(t0), self.t_interval(t1)
        return r[1] < r[0]

    def _occurs_interval_ranges(self, t0: float, t1: float):
        # find all interpretations of t0-t1 in this interval
        r = [(self.t_interval(t0), self.t_interval(t1))]
        if r[0][1] < r[0][0]:
            # t0-t1 crosses an interval boundary
            r = [(r[0][0], self.interval), (0, r[0][1])]
        # check time ranges
        for range_start, range_end in self.time_ranges:
            for span_start, span_end in r:
                if span_start <= range_start <= span_end:
                    return True
        return False

    def find_transitions(self, begin: (str, float), end: (str, float), include_bounds: bool=True, limit=100):
        """
        Find all transition times in the given time range.  Returns a list of times that the schedule turns on or off.
        The boundary times themselves are included if they are within the overall time range and 'include_bounds' is
        True.
        """
        begin = self._parse(begin)
        end = self._parse(end)
        begin0, end0 = begin, end
        if not self._trans_valid(begin, end):
            return
        # truncate to start and end times
        begin, end = self._trans_trunc(begin, end)
        # check for backwards request
        if begin > end:
            return
        # time ranges only
        if not self.interval and self.time_ranges:
            for t in self._trans_time_ranges(begin, end, begin0, end0, include_bounds=include_bounds):
                yield t
            return
        # interval with time ranges
        if self.interval and self.time_ranges:
            for t in self._trans_intervals(begin, end, limit, include_bounds=include_bounds):
                yield t
            return
        # start and end times only
        if include_bounds:
            yield begin
            yield end
            return
        if self.start_time and begin0 <= self.start_time < end0:
            yield self.start_time
        if self.end_time and begin0 <= self.end_time <= end0:
            yield self.end_time

    def _trans_trunc(self, begin, end):
        if self.start_time and begin < self.start_time:
            begin = self.start_time
        if self.end_time and end > self.end_time:
            end = self.end_time
        return begin, end

    def _trans_valid(self, begin, end):
        if self._is_null():
            return False
        # truncate to start and end times
        if self.end_time and begin >= self.end_time:
            return False
        if self.start_time and end <= self.start_time:
            return False
        return True

    def _trans_time_ranges(self, begin, end, begin0, end0, include_bounds):
        for r_start, r_end in self.time_ranges:
            if begin >= r_end or end <= r_start:
                continue
            r_start0, r_end0 = r_start, r_end
            if r_start < begin:
                r_start = begin
            if include_bounds or (begin0 <= r_start0 < end0):
                yield r_start
            if r_end > end:
                r_end = end
            if include_bounds or (begin0 <= r_end0 <= end0):
                yield r_end

    def _trans_intervals(self, begin, end, limit, include_bounds):
        """
        Find transition times for recurring intervals.
        """
        offset = self.t_interval(begin)
        t = begin - offset
        cycles = 0
        while t < end and cycles < limit:
            for r_start, r_end in self.time_ranges:
                for t1 in self._trans_intervals_cycle(r_start, r_end, t=t, offset=offset, end=end, include_bounds=include_bounds):
                    yield t1
            t = self.next_interval(t)
            offset = 0
            cycles += 1

    def _trans_intervals_cycle(self, r_start, r_end, t, offset, end, include_bounds):
        if offset >= r_end:
            return
        start_offs, end_offs = False, False
        if offset > r_start:
            r_start = offset
            start_offs = True
        r_start += t
        r_end += t
        if r_start > end:
            return
        if r_end > end:
            r_end = end
            end_offs = True
        if include_bounds or not start_offs:
            yield r_start
        if include_bounds or not end_offs:
            yield r_end

    @staticmethod
    def find_transition_times(schedules, projection_range):
        """
        Generate a sorted list of every time that something changes in any schedule.

        :param schedules:               An iterable of (settings, schedule).
        :param projection_range:        Time range: (start, end)
        :return:            A sorted list of times.
        """
        if not projection_range:
            return []
        ref = schedules[0][1] if schedules else Schedule()
        trans = {ref._parse(projection_range[0]), ref._parse(projection_range[1])}
        for _, schedule in schedules:
            trans |= set(map(int, schedule.find_transitions(*projection_range)))
            trans.add(int(schedule._parse(projection_range[0])))
            trans.add(int(schedule._parse(projection_range[1])))
        return list(sorted(trans))

    def widen_time_range(self, start_time, end_time):
        """
        Cause a time range to start and end on interval boundaries.
        """
        if self.interval:
            intervals = list(Schedule(interval=self.interval, time_zone=self.time_zone).intervals_in_range(start_time, end_time))
            if intervals[0][0] < start_time:
                start_time = intervals[0][0]
            if intervals[-1][1] > end_time:
                end_time = intervals[-1][1]
        return start_time, end_time


def system_timezone():
    """
    Get default timezone.

    NOTE:
        datetime(y,m,d,h,m,s, tzinfo=zone) <- DO NOT USE tzinfo!!!
        Instead use zone.localize(datetime(y,m,d,h,m,s))

        The first case seems to fall back to local mean time, ignoring the specified timezone.

        See: test_bug_in_pytz()
    """
    return tzlocal.get_localzone()


DATE_PARSE_CACHE = LruCache(max_size=1000)


def cached_date_parse(default_year, time_str, time_zone):
    """
    Date parsing is a bit slow, and the dates we parse tend to be the same ones over and over.
    """
    key = "%d:%s:%s" % (default_year, time_str, time_zone)
    out = DATE_PARSE_CACHE.get(key)
    if out:
        return out
    default = datetime(default_year, 1, 1)
    naive = dateutil.parser.parse(time_str, ignoretz=True, default=default)
    if not hasattr(time_zone, "localize"):
        # compensate for input timezone
        naive = naive.replace(tzinfo=GMT)
        offs = time_zone.utcoffset(naive).total_seconds()
        out = naive.timestamp() - offs
    else:
        out = time_zone.localize(naive).timestamp()
    DATE_PARSE_CACHE[key] = out
    return out
