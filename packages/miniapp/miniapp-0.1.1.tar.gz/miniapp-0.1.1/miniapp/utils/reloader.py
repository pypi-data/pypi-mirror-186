"""
Common bits for a typical service.
"""
import os
import sys
import time
import subprocess

from miniapp.utils.file_utils import detect_file_changes


def default_logger(msg):
    print(msg)
    sys.stdout.flush()


class HotReloader(object):
    """
    Watches for code changes and restarts a process.
    """
    def __init__(self, code_folder_to_monitor, run_args, interval=3, runner=("python",), logger=default_logger):
        """
        Set up hot reloading.
        :param code_folder_to_monitor:  If any code in this folder changes, the process is restarted.  You can also
            supply a list.
        :param run_args:                Arguments to runner.
        :param interval:                How often to check for changes.
        :param runner:                  Alternative to the default Python command.
        """
        self.code_folders_to_monitor = code_folder_to_monitor if isinstance(code_folder_to_monitor, (list, tuple))\
            else [code_folder_to_monitor]
        # entry_point can be a string, a list or a tuple
        # it defaults to 'main.py' in the folder being monitored
        self.run_args = tuple(run_args)
        self.current_server_process = None
        self.runner = (runner,) if isinstance(runner, str) else tuple(runner)
        self.interval = interval
        self.running = False
        self.logger = logger

    def get_source_mod_time(self, prior=None, retries: int=None):
        """
        Find modification time for source files.
        :param prior:   Time of prior modification, used to gather list of changed files.
        :return:        Time of most recent modification and a list of changed files.
        """
        if retries:
            for _ in range(retries):
                try:
                    return self.get_source_mod_time(prior)
                except Exception:
                    if _ == retries-1:
                        raise
                    time.sleep(3)
        ignored_names = [
            '__pycache__',
            '.coverage',
            'htmlcov'
        ]
        def _file_filter(f):
            # Return True if the file should be watched
            if f.basename in ignored_names:
                return False
            return f.is_dir() or f.name.endswith(".py")

        return detect_file_changes(
            self.code_folders_to_monitor, prior, file_filter=_file_filter
        )

    def monitor_for_changes(self):
        """
        Run forever, looking for changes and restarting the process.
        """
        t0, _ = self.get_source_mod_time(retries=3)
        self.running = True
        while self.running:
            time.sleep(self.interval)
            t1, details = self.get_source_mod_time(t0, retries=3)
            if t1 > t0:
                self.on_change(details)
            t0 = t1

    def launch_server(self):
        """
        Runs the thing we're monitoring.
        """
        cmd = self.runner + self.run_args
        #print("RUNNING %s" % str(cmd))
        return subprocess.Popen(cmd)

    def on_change(self, details):
        """
        Called when changes are detected.
        """
        self.logger("\nSOURCE CHANGED %s, restarting" % details)
        self.current_server_process.kill()
        self.current_server_process = self.launch_server()

    def run(self):
        """
        Launch the process and begin monitoring.
        """
        self.current_server_process = self.launch_server()
        self.monitor_for_changes()


def run_with_reloader(code_folder, run_args, alt_runner=None):
    """
    Run an application with hot reload.  Runs forever.
    :param code_folder:   Folder to monitor, or a list of folders.
    :param main_file:     Filename for main entry point, assumed to be at the root of the source tree.
    :param alt_runner:    Alternative runner to ["python"].
    """
    HotReloader(code_folder, run_args=run_args, runner=alt_runner or (sys.executable,)).run()


def is_hot_reload_requested():
    """
    Test the environment flag for hot reloading.
    """
    return os.environ.get("HOT_RELOAD", "").lower() in {"1", "on", "true", "yes"}
