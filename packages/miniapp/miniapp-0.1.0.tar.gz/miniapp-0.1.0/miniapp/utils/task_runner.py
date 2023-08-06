from collections import namedtuple
import time
import threading
import random

from miniapp.errs import GeneralError, ReportedException


class TaskRunner(object):
    """
    Scheduled background tasks.  Manages the execution of any number of tasks that should run at regular intervals.
    """
    TASK = namedtuple("Task", "runner interval initial_delay name use_thread enabler")

    def __init__(self, interval=1, logger: callable = None):
        self.tasks = []
        self.interval = interval
        self.request_stop = False
        self.lock = threading.Lock()
        self.logger = logger
        self.threads_running = set()

    def add_task(self, runner: callable, interval, initial_delay=None, name: str=None, use_thread: bool=False, extra_random: float=0.1, enabler: callable=None):
        """
        Add a task to be executed.
        :param runner:          Method that will be called.
        :param interval:        How often to call it.  0 to run back-to-back.  Specify a number to
                                indicate the interval in seconds, or a method to have the interval computed.  A negative
                                value means the same as a positive value only the 'stuck' warning is inhibited.
        :param initial_delay:   How long to wait before calling it.
        :param name:
        :param use_thread:      Whether to run in a separate thread to avoid delaying other tasks.
        :param enabler:         A method to call to determine whether the task should be executed.  The task is paused
                                (and its timer does not change) when this method returns False.
        """
        if isinstance(interval, (int, float)) and interval > 0:
            # lots of tasks will be at 15s, 30s, etc. intervals
            # - by adding a small random amount they will spread out and distribute the load more evenly
            interval += random.uniform(0, extra_random)
        with self.lock:
            # first value is amount of time before task should run
            self.tasks.append([
                initial_delay or 0,
                self.TASK(runner, interval, initial_delay or 0, name=name or runner.__name__, use_thread=use_thread, enabler=enabler)
            ])

    def start(self):
        threading.Thread(target=self.run, name="TaskRunner").start()

    def stop(self):
        self.request_stop = True

    def log(self, message, **kwargs):
        if self.logger:
            self.logger(message, **kwargs)
        else:
            print(message)

    def _get_interval(self, task):
        i = task.interval
        if hasattr(i, "__call__"):
            return i()
        return i

    def next_tasks(self, dt: float):
        """
        Find tasks that are ready to run.

        :param dt:   Amount of elapsed time since last check.  This amount is subtracted from all enabled tasks' timers.
        """
        with self.lock:
            out = []
            for task in self.tasks:
                # check whether task is enabled to run
                enabler = task[1].enabler
                enabled = enabler() if enabler else True
                if not enabled:
                    continue
                # decrease timer
                task[0] -= dt
                # timer reached 0?
                if task[0] < 0:
                    # add to list of 'ready' tasks, reset timer
                    out.append(task[1])
                    task[0] = abs(self._get_interval(task[1]))
            return out

    def run_task(self, task, enable_thread: bool=True):
        if task.use_thread and enable_thread:
            def runner():
                self.threads_running.add(task.name)
                self.run_task(task, enable_thread=False)
                self.threads_running.remove(task.name)
            # we never allow 2 threads to run for the same task
            if task.name in self.threads_running:
                # task is already running - if interval is 0 we don't show the warning
                i = self._get_interval(task)
                if i > 0:
                    self.log(f"task stuck, interval={i}", level="WARN", caller_detail=f"BACKGROUND_TASK.{task.name}")
            else:
                threading.Thread(target=runner, name=f"TaskRunner.{task.name}").start()
            return
        try:
            # a long-running task will delay other tasks
            task.runner()
        except Exception as err:
            if not isinstance(err, GeneralError):
                err = ReportedException(err)
            self.log(err.to_log(), level="ERROR", caller_detail=f"BACKGROUND_TASK.{task.name}")

    def run(self):
        t0 = time.time()
        while not self.request_stop:
            t1 = time.time()
            dt = t1 - t0
            for task in self.next_tasks(dt):
                self.run_task(task)
            time.sleep(self.interval)
            t0 = t1
