"""
Command line / SSH interface, for running Helm, etc.
"""
import subprocess
import tempfile
import threading
import time
import re
import os
import psutil

from ..errs import GeneralError


class PopenWithMetrics(subprocess.Popen):
    """
    Replacement for Popen which collects resource usage from child before reaping it.
    """
    def _try_wait(self, wait_flags):
        (pid, sts, res) = os.wait4(self.pid, wait_flags)
        self.rusage = res
        self.metrics = {"cpu": res.ru_stime + res.ru_utime, "memory": res.ru_maxrss, "iops": res.ru_inblock + res.ru_oublock}
        return pid, sts

    def poll(self):
        if self.returncode is not None:
            return self.returncode
        try:
            if not self._waitpid_lock.acquire(False):
                return
            try:
                pid, sts = self._try_wait(os.WNOHANG)
                if pid == self.pid:
                    self.returncode = sts
            finally:
                self._waitpid_lock.release()
        except ChildProcessError:
            self.returncode = 0
        return self.returncode


class CommandLine(object):
    """
    Interface to command line, for running commands locally.
    """

    def __init__(self):
        self._active = {}

    def command(self, cmd, log_stdout=None, cancellation_checker=None, shell=False, cwd=None, env=None,
                timeout=None, stdin=None, cat_stdout=None, cat_stderr=None, metrics=None, store_pid=None):
        """
        Run a command.
        :param cmd:  Remote command to execute, a list of strings.
        :param log_stdout:  Method called with chunks of stdout from the process.
        :param cancellation_checker:  Method called to test for cancellation.
        :param shell:   Whether to allow shell commands.
        :param cwd:     Working directory to use.
        :param env:     Environment variables.
        :param timeout: Maximum time to wait for completion.
        :param stdin:   Content to pipe to stdin.
        :param cat_stdout: Concatenates stdout to a given file.
        :param cat_stderr: Concatenates stderr to a given file.
        :param metrics: Returns process statistics (cpu, memory) here if a {} is supplied.
        :param store_pid:  Filename where PID will be stored, or a function to call with the PID.
        :return: A tuple with the exit code, stdout and stderr from the process.  All will be None if the process was
            cancelled by cancellation_checker.  stdout will be None if log_stdout was given.
        """
        if log_stdout and cat_stdout:
            raise Exception("invalid use: 'log_stdout' and 'cat_stdout'")
        if log_stdout:
            return self._command_log_stdout(
                cmd, log_stdout=log_stdout, cancellation_checker=cancellation_checker, stdin=stdin, cwd=cwd, env=env,
                store_pid=store_pid, metrics=metrics
            )
        if cat_stdout or cat_stderr:
            cmd = self._extend_cmd(cmd, cat_stdout, cat_stderr)
            shell = True
        process = PopenWithMetrics(
            cmd, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=shell, cwd=cwd, env=env, stdin=subprocess.PIPE if stdin else None
        )
        self._register_proc(process.pid, process.kill)
        if store_pid:
            if hasattr(store_pid, "__call__"):
                store_pid(process.pid)
            else:
                with open(store_pid, 'w') as f:
                    f.write(str(process.pid))
        self._send_stdin(stdin, process)
        # separate thread to check for cancellation
        if cancellation_checker:
            self._cancellation_check(process, cancellation_checker)
        try:
            stdout, stderr = process.communicate(timeout=timeout)
            stdout = stdout.decode("utf-8")
            stderr = stderr.decode("utf-8")
            # monitor process and collect peak usage
            if metrics is not None:
                metrics.update(process.metrics)
            # unlock pid file
            if store_pid and isinstance(store_pid, str) and os.path.exists(store_pid):
                os.remove(store_pid)
            # no longer active
            self._register_proc(process.pid, None)
        except subprocess.TimeoutExpired:
            # clean up - otherwise file handles linger
            self._register_proc(process.pid, None)
            process.kill()
            if store_pid and isinstance(store_pid, str):
                os.remove(store_pid)
            try:
                _ = process.communicate(timeout=timeout)
            except Exception:
                # ignore error encountered while cleaning up
                pass
            raise GeneralError(code="timeout", message="internal timeout", private_details={
                "command": cmd, "timeout": timeout
            })
        return process.returncode, stdout, stderr

    def kill_process(self, pid: int):
        """
        Use this method to kill a process that has been started.
        """
        killer = self._active.get(pid)
        if killer:
            killer()

    def _register_proc(self, pid: int, killer: callable=None):
        if not killer:
            self._active.pop(pid)
        else:
            self._active[pid] = killer

    @staticmethod
    def _extend_cmd(cmd, cat_stdout=None, cat_stderr=None):
        """
        Extend a shell command to include stream redirection.
        """
        cmd = CommandLine.args_to_str(cmd)
        if cat_stdout:
            cmd += " >> %s" % cat_stdout
        if cat_stderr:
            cmd += " 2>&1" if cat_stderr == cat_stdout else " 2>> %s" % cat_stderr
        return cmd

    @staticmethod
    def _send_stdin(stdin, process):
        """
        Write content to stdin of a process.
        """
        if stdin:
            if isinstance(stdin, str):
                stdin = stdin.encode("utf-8")
            process.stdin.write(stdin)

    def _command_log_stdout(self, cmd, log_stdout=None, cancellation_checker=None, stdin=None, store_pid=None, metrics=None, **kwargs):
        """
        Runs a command and streams its stdout to a given method.
        :param cmd:             Command to run.
        :param log_stdout:      Method to receive chunks of stdout.
        :param cancellation_checker: Checks for cancellation.
        :param stdin:           Content to send to stdin of process.
        """
        tmp_f = tempfile.NamedTemporaryFile(delete=False)
        pid = None
        try:
            cmd = "exec " + self.args_to_str(cmd) + " > %s" % tmp_f.name
            process = PopenWithMetrics(
                cmd, stderr=subprocess.PIPE, shell=True, stdin=subprocess.PIPE if stdin else None, **kwargs
            )
            pid = process.pid
            self._register_proc(pid, process.kill)
            if store_pid:
                if hasattr(store_pid, "__call__"):
                    store_pid(pid)
                else:
                    with open(store_pid, 'w') as f:
                        f.write(str(pid))
            self._send_stdin(stdin, process)
            if cancellation_checker:
                self._cancellation_check(process, cancellation_checker)
            if stdin:
                process.stdin.close()
            for line in read_file_til_process_done(process, tmp_f.name):
                log_stdout(line)
            if metrics is not None:
                metrics.update(process.metrics)
        finally:
            if pid:
                self._register_proc(pid, None)
            os.unlink(tmp_f.name)
        stderr = process.stderr.read().decode("utf-8") if process.returncode is not None else None
        if store_pid and isinstance(store_pid, str):
            os.remove(store_pid)
        process.stderr.close()
        return process.returncode, None, stderr

    @staticmethod
    def _cancellation_check(process, cancellation_checker):
        """
        Runs a thread alongside a process and kills the process if requested by a supplied monitor.
        :param process:                 Process to watch.
        :param cancellation_checker:    Monitor to call, returns True to kill the process.
        """
        def runner():
            while True:
                time.sleep(0.25)
                if not process_is_running(process):
                    return
                if cancellation_checker():
                    process.kill()
                    return
        threading.Thread(target=runner, name="cmdline.cancellation_check").start()

    @staticmethod
    def args_to_str(args):
        """
        Convert a Popen() style argument list to a properly escaped bash command string fragment.
        """
        if not args:
            return ""
        if isinstance(args, str):
            return args
        out = []
        for arg in args:
            if re.match(r'^[a-zA-Z0-9_\-./:$]+$', arg, re.DOTALL) is None:
                cleaned = re.sub(r'([!"\\])', r'\\\1', arg) \
                    .replace("\n", "\\n") \
                    .replace("\r", "").replace("\t", "\\t")
                out.append('"%s"' % cleaned)
            else:
                out.append(arg)
        return " ".join(out)


class SSH(CommandLine):
    """
    Interface to ssh, for running commands on remote systems.
    """
    def __init__(self, username, host, private_key):
        self.username = username
        self.host = host
        self.private_key = private_key

    def command(self, cmd, log_stdout=None, cancellation_checker=None, shell=False, cwd=None, env=None, **kwargs):
        """
        Same as CommandLine, only the command is run on a remote system.
        """
        with tempfile.NamedTemporaryFile(delete=True) as identity_file:
            identity_file.write(self.private_key)
            identity_file.flush()
            cmd = ["ssh", "-i", identity_file.name, self.username + "@" + self.host] + cmd
            return super(SSH, self).command(cmd, log_stdout, cancellation_checker)


def read_file_til_process_done(proc, filename):
    """
    Read chunks of a file until a process completes.
    """
    with open(filename, 'r') as f_r:
        p = 0
        ended = False
        while True:
            # read next chunk
            f_r.seek(0, 2)
            len = f_r.tell()
            if len > p:
                f_r.seek(p)
                chunk = f_r.read()
                p = f_r.tell()
                yield chunk
            if ended:
                break
            # check for process still running
            try:
                proc.wait(0.1)
                ended = True
                continue
            except (subprocess.TimeoutExpired, psutil.TimeoutExpired):
                continue


def process_is_running(process):
    """
    Test whether a given process is still running.
    """
    if process.poll() is not None:
        return False
    return pid_is_running(process.pid)


def pid_is_running(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False


def command_exists(command: str) -> bool:
    """
    Check for the existence of a given shell command.
    """
    exitcode, stdout, stderr = CommandLine().command(f"which {command}", shell=True)
    return exitcode == 0
