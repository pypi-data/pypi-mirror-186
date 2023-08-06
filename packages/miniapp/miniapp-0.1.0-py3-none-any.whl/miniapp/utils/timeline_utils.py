"""
Utilities related to timelines, histograms, etc..
"""
import time
from collections import defaultdict


class HistogramEventCounter(object):
    """
    Track multiple events or measures over time, organizing them into 'time bins' of a given size.

    The name 'event' is used, implying an integer value indicating the number of times something has occurred, but
    you can also track 'measures' using floating point values.

    events = HistogramEventCount(...options...)
    ... time passes ...
    events.add_event("calls")
    events.add_event("leakage", 3.251)
    ...
    print(events.summary())

    """
    def __init__(self, time_bin_size: float=60, max_bins: int=60):
        """
        :param time_bin_size:   How wide the time bins should be, in seconds.
        :param max_bins:        Number of bins to include in the timeline.
        """
        self.time_bin_size = time_bin_size
        self.max_bins = max_bins
        if self.max_bins <= 1 or self.time_bin_size <= 0:
            raise ValueError()
        self.t0 = time.time()
        self.bins = defaultdict(lambda: defaultdict(int))

    def _bin_for_time(self, t: float=None) -> int:
        """
        Calculate an integer value representing a given time bin, given a time.
        """
        if not t:
            t = time.time()
        dt = max(t - self.t0, 0)
        return int(dt // self.time_bin_size)

    def _time_for_bin(self, bin_no: int) -> float:
        """
        Calculate the starting time for a given bin number.
        """
        return self.t0 + bin_no * self.time_bin_size

    def _trim_bins(self):
        """
        Get rid of bins that are too far in the past.
        """
        threshold = self._bin_for_time() - self.max_bins
        for bin_no in list(self.bins):
            if bin_no < threshold:
                self.bins.pop(bin_no, None)

    def add_event(self, event, count: (int, float)=1):
        """
        Place an event on the timeline, adding it to a histogram bin.
        """
        self.bins[self._bin_for_time()][event] += count

    def summary(self, include_current_bin: bool=True) -> list:
        """
        Produce a clean timeline of events.  An array of {}s is returned, mapping event names to event counts.
        The returned list will only include time bins from when the histogram was created, and will never contain
        more than self.max_bins.  The very last time bin contains partial data, so you can choose to omit it.
        """
        self._trim_bins()
        bin1 = self._bin_for_time()
        bin0 = max(bin1 - self.max_bins + 1, 0)
        results = [{} for _ in range(bin0, bin1+1)]
        for bin_no, events in sorted(self.bins.items()):
            results[bin_no - bin0] = events
        if not include_current_bin:
            results = results[:-1]
        return results
