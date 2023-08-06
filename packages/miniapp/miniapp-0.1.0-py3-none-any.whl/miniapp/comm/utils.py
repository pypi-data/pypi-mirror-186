import json
import io
import tempfile

from miniapp.utils.misc import format_iso_datetime


def json_dumps(obj, indent=2):
    """
    Alternate JSON dumps method that sets up all the defaults, and handles GenericObject, plus a few common
    object types.

    NOTE: there is a much more comprehensive version at wbcommon.misc.json_safe_value().
    """
    class AltEncoder(json.JSONEncoder):
        def default(self, obj):
            if obj and obj.__class__.__name__ == "GenericObject":
                return obj._to_json()
            if obj and obj.__class__.__name__ == "UUID":
                return str(obj)
            if obj and obj.__class__.__name__ == "datetime":
                return format_iso_datetime(obj)
            if hasattr(obj, "to_json"):
                return obj.to_json()
            return super(AltEncoder, self).default(obj)
    return json.dumps(obj, indent=indent, cls=AltEncoder, allow_nan=False)


class ChunkStreamWrapper(io.RawIOBase):
    """
    Read from a stream, up to a limit, with very limited seek support.  This class is used to convert upload streams
    (i.e. from BaseHttpRequestHandler's rfile stream (which does not support seek), to a stream suitable for use with
    requests.post(..., data=<stream>).
    """
    def __init__(self, source, length):
        self._source = source
        self._pos = 0
        self._total = length
        self._remaining = length
        self._seek = 0
        self._shadow_file = None
        self._binary = None

    def close(self) -> None:
        if self._shadow_file:
            self._shadow_file.close()
            self._shadow_file = None

    def __del__(self):
        self.close()

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def seek(self, offset: int, whence: int = None):
        if not self._shadow_file and self._pos == 0:
            # if seek is used right away we start shadowing the data we read
            self._shadow_file = tempfile.NamedTemporaryFile(mode='rb+', delete=True)
        if whence == 2 and offset == 0:
            self._seek = self._pos + self._remaining + offset
        elif whence == 1:
            self._seek = self._pos + offset
        else:
            self._seek = offset

    def tell(self) -> int:
        return self._seek

    def read(self, n=None):
        chunk0 = None
        # are we reading from a position beyond what we've read?
        self._pre_read()
        # read as much as we can from the shadow file
        if self._seek < self._pos:
            # this is only possible/allowed if we have been recording the data we read
            if not self._shadow_file:
                raise Exception(f"SEEK NOT FULLY IMPLEMENTED: {self._seek}, {self._pos}")
            self._shadow_file.seek(self._seek)
            n1 = self._total - self._seek
            if n is not None:
                if n < n1:
                    n1 = n
                n -= n1
            chunk0 = self._shadow_file.read(n1)
            if not self._binary:
                chunk0 = chunk0.decode("utf-8")
            self._seek += n1
        # reading from current position in 'self._source'
        if n is None or n < 0 or n > self._remaining:
            n = self._remaining
        self._pos += n
        self._remaining -= n
        self._seek = self._pos
        chunk1 = self._source.read(n)
        if self._binary is None:
            self._binary = not isinstance(chunk1, str)
        if self._shadow_file:
            self._shadow_file.write(chunk1.encode("utf-8") if isinstance(chunk1, str) else chunk1)
        return chunk0 + chunk1 if chunk0 else chunk1

    def _pre_read(self):
        """
        Catch up reading of source stream to current seek position.
        Continue to read from 'self._source' until we reach the current seek position.
        """
        pre_read = self._seek - self._pos
        while pre_read > 0:
            n1 = min(pre_read, 100000)
            bit = self._source.read(n1)
            if self._binary is None:
                self._binary = not isinstance(bit, str)
            if self._shadow_file:
                self._shadow_file.write(bit.encode("utf-8") if isinstance(bit, str) else bit)
            pre_read -= n1
            self._pos += n1
            self._remaining -= n1


class StreamFromChunks(object):
    """
    Turns a chunked stream into a proper stream.

    If a size is provided, very limited seek ability will be enabled.
    """
    def __init__(self, chunk_iter, mode: str=None, size: int=None):
        self._chunk_iter = chunk_iter
        self._buf = None
        self._pos = 0
        self._size = size
        self._mode = mode
        self._seek_end = False

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return self._size is not None

    def read(self, n: int=None):
        if n is None:
            n = 99000000000
        out = None
        while n > 0 and not self._seek_end:
            if self._buf is None:
                try:
                    self._buf = next(self._chunk_iter)
                    if not self._mode:
                        self._mode = 'r' if isinstance(self._buf, str) else 'rb'
                except StopIteration:
                    break
            amt = min(len(self._buf), n)
            if out is None:
                out = self._buf[:amt]
            else:
                out += self._buf[:amt]
            self._buf = self._buf[amt:]
            self._pos += amt
            n -= amt
            if not self._buf:
                self._buf = None
        if out is None:
            out = b'' if not self._mode or 'b' in self._mode else ''
        return out

    def seek(self, n, whence=0):
        # seek to current position is ok (nop)
        if (n == self._pos and whence == 0) or (n == 0 and whence == 1):
            self._seek_end = False
            return
        # seek to end is possible if the size is known
        if self._size is not None:
            if n == 0 and whence == 2:
                self._seek_end = True
                return
        # 'requests' will bypass size measurement when this exception is raised
        raise IOError("not seekable")

    def tell(self):
        if self._seek_end:
            return self._size
        return self._pos

    def close(self):
        """ override if self._chunk_iter needs to be closed """
        pass

    def __iter__(self):
        return self._chunk_iter
