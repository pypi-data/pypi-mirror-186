import os
import json
import tempfile
import shutil
import re
from collections import namedtuple


def open_file_tweaked(filename, mode='rb', delete_after_use: bool=False, byte_range: (list, tuple)=None):
    """
    Add some features to an open file.
    :param filename:        File to open (only read modes are supported).  Can be a filename or a file object.
    :param mode:            Mode for opening.
    :param delete_after_use: Deletes the file when it is closed.
    :param byte_range:      Range to read from the file.
    :return:            File-like object.
    """
    if "r" not in mode:
        raise ValueError("unsupported mode: %s" % mode)
    if isinstance(filename, str):
        fh = open(filename, mode)
    else:
        fh = filename
    orig_close = fh.close
    orig_read = fh.read
    orig_seek = fh.seek
    orig_tell = fh.tell
    if delete_after_use:
        def do_close():
            orig_close()
            if isinstance(filename, str):
                os.remove(filename)
            elif hasattr(filename, "name"):
                os.remove(filename.name)
        fh.close = do_close
    if byte_range:
        orig_seek(0, 2)
        orig_len = orig_tell()
        orig_seek(byte_range[0])
        byte_range = [min(byte_range[0], orig_len), min(byte_range[1], orig_len)]
        pos = [0]
        lim = byte_range[1] - byte_range[0]
        def do_read(n=None):
            if n is None:
                n = max(lim - pos[0], 0)
            if pos[0] + n > lim:
                n = max(lim - pos[0], 0)
            chunk = orig_read(n)
            pos[0] += len(chunk)
            return chunk
        def do_seek(n, whence=0):
            if whence == 1:
                n += pos[0]
            elif whence == 2:
                n += lim
            n = max(0, min(n, lim))
            orig_seek(byte_range[0] + n)
            pos[0] = n
        def do_tell():
            return pos[0]
        fh.read = do_read
        fh.seek = do_seek
        fh.tell = do_tell
    return fh


def load_file(fn: str, mode='r', must_exist: bool=True):
    """
    Load file content.
    :param fn:      Filename.
    :param mode:    'r' or 'rb'.
    :param must_exist: True to fail if file does not exist, if False and file does not exist, returns None.
    """
    if not must_exist and (not fn or not os.path.exists(fn)):
        return
    with open(fn, mode) as f:
        return f.read()


def store_file(fn: str, content, append: bool=False):
    """
    Atomic file write.  Will write str or bytes, or JSON.
    :param fn:          File to write.
    :param content:     Content to write.
    :param append:      Appends to file.
    """
    mode = "wb" if isinstance(content, (bytes, bytearray)) else "w"
    if isinstance(content, (list, dict, tuple)):
        content = json.dumps(content)
    if append:
        with open(fn, mode.replace("w", "a")) as f_a:
            f_a.write(content)
    else:
        use_dir = os.path.dirname(fn)
        with tempfile.NamedTemporaryFile(dir=use_dir, delete=False, mode=mode, prefix=".~") as f_w:
            f_w.write(content)
        os.rename(f_w.name, fn)


def remove_file(filename):
    """
    Remove a file, with no warning if it does not exist.
    """
    if os.path.exists(filename):
        os.remove(filename)


T_DIR_ENTRY = namedtuple("DIR_ENTRY", "basename name path is_dir stat is_link")
def walk_all(path, file_filter: callable=None, prefix=""):
    """
    Recursive version of os.scandir().  Returns an iteration of:
      basename - just the name of the file with no path information
      name     - the relative path to the file
      path     - the full path to the file
      is_dir   - method to call to test whether this is a directory
      stat     - method to call equivalent to os.stat()
    """
    if not os.path.exists(path):
        return
    def gen_link_fn(fn):
        return lambda: os.path.islink(os.path.join(path, fn))
    for f in os.scandir(path):
        entry = T_DIR_ENTRY(
            f.name, prefix + f.name, f.path, f.is_dir, f.stat, is_link=gen_link_fn(f.name)
        )
        if file_filter and not file_filter(entry):
            continue
        yield entry
        if f.is_dir():
            pfx = entry.name + "/"
            for sub in walk_all(f.path, file_filter=file_filter, prefix=pfx):
                yield sub


def detect_file_changes(folders: list, prior=None, file_filter: callable=None):
    """
    Find modification time for source files.
    :param folders: Which folders to check.
    :param prior:   Time of prior modification, used to gather list of changed files.  None: just determine time
                    of last modification, 0=return all files.
    :param file_filter: Optionally chooses which files to include.
    :return:        Time of most recent modification and a list of changed files.
    """
    latest = 0
    details = []
    def strip_prefix(f, p):
        return f[len(p):] if f.startswith(p) else f
    for check_folder in folders:
        prefix = end_with_slash(check_folder)
        for f in walk_all(check_folder, file_filter):
            try:
                info = f.stat()
            except FileNotFoundError:
                continue
            mtime = info.st_mtime_ns / 1e9
            if prior is not None and mtime > prior:
                fn = strip_prefix(f.path, prefix)
                details.append(fn)
            if mtime > latest:
                latest = mtime
    return latest, details


def clear_out_folder(folder: str):
    """
    Remove all the files in a folder.
    """
    if not os.path.exists(folder):
        return
    if os.path.islink(folder):
        return
    for f in os.listdir(folder):
        fn = os.path.join(folder, f)
        if not os.path.isdir(fn) or os.path.islink(fn):
            os.remove(fn)
        else:
            shutil.rmtree(fn)


def end_with_slash(path: str):
    """
    Require that a string end with a slash.
    """
    if path.endswith("/"):
        return path
    else:
        return path + "/"


def normalize_path(path: str, safe: bool=True):
    """
    Clean up ".." and "." paths.

    :param path:  A path which may contain ".." or "." paths.
    :param safe:  Whether to prevent the overall path from 'breaking out', i.e. it may not start with '../'.
    """
    cleaned = path
    while True:
        c0 = cleaned
        cleaned = re.sub(r'(^|/)((?!\.\.\b)[^/]+/\.\.(/|$))', r'\1', cleaned)
        cleaned = re.sub(r'(^\.$|^\./|/\.(?=/)|/\.$|/\./$)', '', cleaned)
        if cleaned == c0:
            break
    if safe:
        if cleaned.startswith("../") or cleaned in ("..", "/.."):
            raise ValueError(f"Insecure path: {path}")
    return cleaned


def make_relative_path(base, path):
    """
    Force a path to be relative to a base.
    """
    # TODO look for equivalent in path.*, os.path, etc.
    if not path.startswith("/"):
        return path
    # find common
    base_parts = base.strip("/").split("/")
    path_parts = path.strip("/").split("/")
    if base_parts[0] == "":
        base_parts.pop(0)
    while base_parts and path_parts and base_parts[0] == path_parts[0]:
        base_parts.pop(0)
        path_parts.pop(0)
    out_parts = [".."] * len(base_parts) + path_parts
    return "/".join(out_parts)


def safe_relative_path(path):
    """
    Test for a relative path which does not attempt to break out of its context, i.e.
    os.path.join(ROOT, path) must be within ROOT.
    """
    if path.startswith("/"):
        return False
    if path.startswith("../") or path == ".." or "/../" in path or path.endswith("/.."):
        return False
    return True


def is_empty_folder(folder):
    """
    Test for an empty folder.
    """
    if not os.path.isdir(folder):
        return False
    return os.listdir(folder) == []
