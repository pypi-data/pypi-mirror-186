import uuid
import time
import sys
import threading

from miniapp.data.impl import InMemoryDb
from miniapp.errs import GeneralError, ReportedException
from miniapp.utils.cmdline import CommandLine

_current_job_info = threading.local()


class JobManager(object):
    """
    Tracking of background jobs.
    """
    def __init__(self, job_id_prefix: str="", db=None, collection_name="jobs", keep_completed_s=60*60):
        """
        Create a job manager instance.
        :param job_id_prefix:   All job IDs will be given this prefix so that they can be distinguished between
                                services.
        :param db:              A MongoishDb instance where job data will be persisted.
        :param collection_name: Which collection in 'db' to store job data.
        """
        self.db = db or InMemoryDb()
        self.collection_name = collection_name
        # how long to keep a record of completed jobs
        self.keep_jobs_s = keep_completed_s
        # how long to keep jobs that have been cancelled
        self.keep_cancelled_s = 30
        # how long to let a job go without a heartbeat before assuming its process has crashed
        self.assume_abandoned_s = 55
        # predictable prefix for all job IDs
        self.job_id_prefix = job_id_prefix
        # last summary of overall status
        self._prev_status = {}
        # for running commands
        self._commands = CommandLine()

    def log(self, message):
        """
        Default logging.
        """
        print(message)
        sys.stdout.flush()

    def query(self, filters: dict=None, limit=None):
        """
        Scan active and recently completed jobs.
        :param filters:             Filters to restrict which records are returned.
        :param limit:               Maximum number of job records to return.
        """
        return self.db.query(self.collection_name, query=filters, fields={"progress": 0, "spec": 0}, limit=limit)

    def status(self, job_id) -> dict:
        """
        Get the status of a specific job.
        """
        if not job_id:
            raise Exception("call query() instead")
        job_rec = self.db.lookup(self.collection_name, job_id)
        if job_rec and "spec" in job_rec:
            job_rec = dict(job_rec)
            job_rec.pop("spec", None)
        return job_rec

    def current_job_id(self) -> (str, None):
        """
        Get the ID of the currently executing job for the current thread.
        """
        try:
            return _current_job_info.job_id
        except AttributeError:
            return

    def maintenance(self):
        """
        Do all maintenance of the job system.  Call this method occasionally.
        """
        self._prune()
        self._update_heartbeats()
        self._detect_abandoned_jobs()

    def _prune(self):
        """
        Remove old, finished jobs, and cancelled jobs whose threads have exited.
        """
        q_expired = {"ended": {"$lt": time.time() - self.keep_jobs_s}}
        self.db.delete(self.collection_name, q_expired)
        q_cancelled = {"ended": {"$lt": time.time() - self.keep_cancelled_s}, "cancel": True}
        self.db.delete(self.collection_name, q_cancelled)

    def _update_heartbeats(self):
        """
        For all jobs running in local threads, store a heartbeat time so that we can detect when a job has been
        abandoned, i.e. by the application being restarted.
        """
        thread_names = set()
        for t in threading.enumerate():
            if t.name.startswith(self.job_id_prefix):
                thread_names.add(f"{t.name}")
        heartbeats = []
        for job_rec in self.db.query(self.collection_name, query={"ended": None}, fields=["_id", "ended"]):
            job_id = job_rec["_id"]
            if job_id in thread_names:
                heartbeats.append(job_id)
        t_now = time.time()
        for job_id in heartbeats:
            self.db.update(self.collection_name, job_id, {"$set": {"heartbeat": t_now}})

    def _detect_abandoned_jobs(self):
        """
        When a system is restarted all the threads handling them go away.  Detect this via old heartbeats.
        """
        t_now = time.time()
        threshold = t_now - self.assume_abandoned_s
        abandoned = []
        # - no recent heartbeat
        for job_rec in self.db.query(self.collection_name, query={"heartbeat": {"$lt": threshold}, "ended": None}):
            abandoned.append(job_rec)
        # - no heartbeat recorded at all
        for job_rec in self.db.query(self.collection_name, query={"heartbeat": None, "ended": None, "started": {"$lt": threshold}}):
            abandoned.append(job_rec)
        for job_rec in abandoned:
            if self._consider_resuming_job(job_rec):
                continue
            self.db.update(self.collection_name, job_rec["_id"], {"$set": {"ended": time.time(), "error": {"code": "server-restart"}}})

    def _consider_resuming_job(self, job_rec):
        """
        Determine whether a job can be resumed, and if it is possible, cause this to happen.
        """
        job_id = job_rec["_id"]
        job = JobAccessor(job_mgr=self, job_id=job_id, name=job_id)
        # work out the function to call for this job
        if "spec" not in job_rec:
            return False
        spec = JobSpec.from_json(job_rec["spec"])
        # limit number of restarts
        n_restarts = job_rec.get("n_restarts", 0)
        if n_restarts >= 3:
            return False
        job._write_job_rec("n_restarts", n_restarts + 1)
        # set heartbeat to prevents redundant restarts
        job._write_job_rec("heartbeat", time.time())
        # TODO we should try harder to prevent redundant restart
        #  - at the moment we are protected only by the unlikelihood of different processes running
        #    _detect_abandoned_jobs() at exactly the same time.
        # re-launch the job
        self.start_code(spec, name=job_rec["name"], _restart_as=job_id)
        self.log(f"RESTARTING JOB {job_rec['name']}, id={job_id}")
        return True

    def _start(self, name: str="", user=None, job_title: str=None, **kwargs):
        """
        Create a job description and mark a job as started.
        """
        job_id = self.job_id_prefix + str(uuid.uuid4()).replace("-", "")[:24]
        name = name or job_id
        job = {
            "_id": job_id,
            "user": user,
            "name": name,
            "started": time.time(),
            "ended": None,
            "progress": [],
            "n_msgs": 0,
            **kwargs
        }
        if job_title:
            job["title"] = job_title
        self.db.insert(self.collection_name, job)
        self._prune()
        return JobAccessor(job_mgr=self, job_id=job_id, name=name)

    def _run_code(self, code, job, code_kwargs: dict=None):
        """
        Execute code within a job.
        :param code:          Code to run.  A callable which is passed a job accessor.
        :param job:           Job accessor, from _start().
        :param code_kwargs:   Named arguments to pass to 'code'.
        :return:   False on exception.
        """
        ok = True
        try:
            if isinstance(code, JobSpec):
                code_kwargs = code.kwargs
                code = code.lookup_callable()
            if code:
                _current_job_info.job_id = job.job_id
                code(job, **(code_kwargs or {}))
        except Exception as err:
            if not isinstance(err, GeneralError):
                err = ReportedException(err)
            if err.has_private_details():
                err.private_details["job_id"] = job.job_id
                self.log("JOB_ERROR %s" % err.to_log())
            else:
                err.remove_tracking_code()
            job._write_job_rec("error", err.to_json(include_private_details=False))
            ok = False
        _current_job_info.job_id = None
        job._write_job_rec("ended", time.time())
        return ok

    def start_code(self, code, name: str, code_kwargs: dict=None, _restart_as: str=None, background: bool=True, user: str=None, job_title: str=None, parent_job: str=None, more_props: dict=None):
        """
        Start some code running in the background.

        :param code:            A callable, or a JobSpec.
        :param name:            Name for the job.
        :param code_kwargs:     Named arguments to pass to code().
        :param user:            Specify owner of job.
        :return:   ID of started job.
        :param _restart_as:     For internal use when restarting a crashed job.
        :return:   ID of started job.
        """
        props = dict(more_props) if more_props else {}
        if parent_job:
            props["parent_job"] = parent_job
        if isinstance(code, JobSpec):
            if _restart_as:
                job = JobAccessor(job_mgr=self, job_id=_restart_as, name=name)
            else:
                job = self._start(name, spec=code.to_json(), user=user, job_title=job_title, **props)
        else:
            job = self._start(name, user=user, job_title=job_title, **props)
        if background:
            threading.Thread(target=self._run_code, args=(code, job, code_kwargs), name=job.job_id).start()
        else:
            self._run_code(code, job, code_kwargs)
        return job.job_id

    def start_cmdline(self, cmd, cwd=None, on_exit: callable=None, name: str="", env: dict=None, shell: bool=False,
                      stdin=None, interpret_error: callable=None, metrics: bool=False, stream_stdout: bool=True,
                      user: str=None):
        """
        Run a command line task in the background.

        :param cmd:      An [] of command line elements.
        :param cwd:      Initial/working directory.
        :param on_exit:  Run after exit.  Passes job record as sole argument.
        :param name:     Name for job.
        :param env:      Environment variables.
        :param stdin:    Content to send to stdin of process.
        :param interpret_error:  Method to produce an exception from exit code and stderr.
        :param metrics:  True to capture 'cpu' and 'memory' peak values.
        :param user:     Specify owner.
        :return:   ID of started job.
        """
        job = self._start(name=name, user=user)
        def run():
            err = None
            try:
                logger = None
                if stream_stdout:
                    logger = lambda chunk: job.progress({"stdout": chunk})
                metrics_out = {}
                def store_pid(pid):
                    job["pid"] = pid
                exit_code, stdout, stderr = self._commands.command(
                    cmd, log_stdout=logger, cwd=cwd, env=env, shell=shell, stdin=stdin,
                    metrics=metrics_out if metrics else None, store_pid=store_pid
                )
                if metrics_out:
                    job["metrics"] = metrics_out
                job["stderr"] = stderr
                if not stream_stdout:
                    job["stdout"] = stdout
                job["pid"] = None
                if exit_code and interpret_error:
                    err = interpret_error(exit_code, stderr)
                elif exit_code and not interpret_error:
                    err = GeneralError(
                        code="exec-error", message="Code execution error",
                        private_details={
                            "cmd": cmd, "cwd": cwd
                        },
                        public_details={
                            "stderr": stderr, "stdout": stdout, "exit_code": exit_code
                        }
                    )
            except Exception as exc:
                err = ReportedException(exc)
                err.private_details["cmd"] = cmd
            if err:
                if err.has_private_details():
                    self.log("JOB_ERROR %s" % err.to_log())
                sys.stdout.flush()
                job["error"] = err.to_json(include_private_details=False, include_tracking_code=err.has_private_details())
            self._run_code(on_exit, job)
        threading.Thread(target=run, name=job.job_id).start()
        return job.job_id

    def cancel_job(self, job_id: str):
        """
        Request cancellation.
        """
        job_rec = self.status(job_id)
        if job_rec:
            if job_rec.get("ended"):
                # completed jobs just get deleted
                self.db.delete(self.collection_name, job_id)
            else:
                self.db.update(self.collection_name, job_id, {"$set": {"cancel": True}})
                # if the job is running in a subprocess, kill it
                pid = job_rec.get("pid")
                if pid:
                    self.db.update(self.collection_name, job_id, {"$set": {"ended": time.time()}, "$unset": {"pid": 1}})
                    self._commands.kill_process(pid)

    def is_cancelled(self, job_id: str):
        """
        Check for cancellation.
        """
        if not job_id:
            return
        job_rec = self.status(job_id)
        if job_rec:
            return bool(job_rec.get("cancel"))

    def sleep_w_check_for_cancel(self, s: float, interval: float=0.25, job_id: str=None):
        """
        Delay for a while, checking for cancellation all the while.

        :returns:   False if cancelled.
        """
        job_id = job_id or self.current_job_id()
        t_end = time.time() + s
        while time.time() < t_end:
            time.sleep(interval)
            if self.is_cancelled(job_id):
                return False
        return True

    def wait_for_job(self, job_id: str, max_wait: (int, float)=1, check_interval: (int, float)=0.1):
        """
        Wait for a job to end, but no longer than 'max_wait' seconds.
        :param job_id:          Which job.
        :param max_wait:        Maximum wait.
        :param check_interval:  How often to check.
        :return:    Job record if job completed, None if it was still busy after the timeout or if job
                did not exist.
        """
        t_timeout = time.time() + max_wait
        while True:
            job_rec = self.status(job_id)
            if not job_rec:
                return
            if job_rec["ended"] or "error" in job_rec:
                return job_rec
            if time.time() > t_timeout:
                return
            time.sleep(check_interval)

    def detect_status_changes(self):
        """
        Detect changes in state of jobs since the last call to this method.  Each change (job started, ended or emitted
        messages) yields a {} describing the change.
        """
        job_status = {}
        # detect new/updated jobs
        for job in self.query():
            job_id = job["_id"]
            state = {
                "user": job.get("user"),
                "started": job["started"],
                "ended": job["ended"],
                "n_msgs": job.get("n_msgs") or 0,
                "name": job.get("name")
            }
            job_status[job_id] = state
            if job_id not in self._prev_status:
                change = dict(state)
            elif state != self._prev_status[job_id]:
                change = dict(state)
                change["n_msgs"] -= self._prev_status[job_id]["n_msgs"]
            else:
                continue
            change["job_id"] = job_id
            yield change
        # detect expired/deleted jobs
        for del_id in set(self._prev_status) - set(job_status):
            job = self._prev_status[del_id]
            yield {
                "job_id": del_id,
                "user": job.get("user"),
                "started": job["started"],
                "ended": job["ended"],
                "name": job.get("name"),
                "n_msgs": 0,
                "deleted": True
            }
        self._prev_status = job_status


class JobSpec(object):
    """
    A reference to executable code.
    """
    def __init__(self, function: str, **kwargs):
        self.function = function
        self.kwargs = kwargs

    def lookup_callable(self):
        """
        Look up the dotted package and function name in 'self.function' and return the referenced function.
        """
        def _path_lookup(obj, path, import_path):
            try:
                return getattr(obj, path)
            except AttributeError:
                __import__(import_path)
                return getattr(obj, path)
        components = self.function.split('.')
        import_path = components.pop(0)
        the_object = __import__(import_path)
        for path_elem in components:
            import_path += ".%s" % path_elem
            the_object = _path_lookup(the_object, path_elem, import_path)
        if not hasattr(the_object, "__call__"):
            raise Exception(f"{self.function} is not callable")
        return the_object

    def to_json(self):
        return {
            "function": self.function,
            **self.kwargs
        }

    @staticmethod
    def from_json(data: dict):
        return JobSpec(**data)


class JobAccessor(object):
    """
    Running jobs are given access to an instance of this class and can use it to record progress, store results,
    detect cancellation, etc..
    """
    def __init__(self, job_mgr: JobManager, job_id: str, name: str):
        self._job_mgr = job_mgr
        self._job_id = job_id
        self.name = name

    @property
    def job_id(self):
        return self._job_id

    def is_cancelled(self):
        """
        Test for cancellation.
        """
        return self._job_mgr.is_cancelled(self._job_id)

    def progress(self, message: (str, dict)):
        """
        Report progress.
        """
        self._job_mgr.db.update(self._job_mgr.collection_name, self._job_id, {"$push": {"progress": message}, "$inc": {"n_msgs": 1}})

    def set_restart_param(self, key: str, value):
        """
        Update a start-up parameter in case this job has to be restarted.  On restart, the updated
        parameters will be used instead of the initial values.
        """
        self._job_mgr.db.update(self._job_mgr.collection_name, self._job_id, {"$set": {"spec." + key: value}})

    def _write_job_rec(self, key, value):
        self._job_mgr.db.update(self._job_mgr.collection_name, self._job_id, {"$set": {key: value}})

    def add_child_job(self, child_job_id: str):
        """
        Add a job ID to the list of child jobs.
        This allows the child job to be cancelled if the parent job is cancelled.
        """
        self._job_mgr.db.update(self._job_mgr.collection_name, self._job_id, {"$push": {"child_jobs": child_job_id}})

    def __setitem__(self, key, value):
        """
        Store custom result values in the job record.
        """
        # block changes to core job fields
        for reserved in ["spec", "_id", "user", "id", "name", "started", "ended", "progress", "n_restarts"]:
            if key == reserved or key.startswith(reserved+"."):
                return
        self._write_job_rec(key, value)


def run_in_foreground(runner, raise_exc: bool=False) -> dict:
    """
    Run a job in the foreground.
    :param runner:      Method which expects a JobAccessor() argument.
    :return:    A job description record, with 'started', 'ended' and 'progress' fields.
    """
    jm = JobManager()
    job_id = jm.start_code(runner, name="job", background=False)
    job_rec = jm.status(job_id)
    if raise_exc and job_rec.get("error"):
        err = job_rec["error"]
        raise GeneralError(code="job-error", private_details=err if isinstance(err, dict) else {"detail": err})
    return job_rec
