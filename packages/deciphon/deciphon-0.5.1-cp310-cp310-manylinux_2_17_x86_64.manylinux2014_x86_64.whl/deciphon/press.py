from __future__ import annotations

from os import PathLike
from pathlib import Path

from deciphon.cffi import ffi, lib
from deciphon.error import DeciphonError

__all__ = ["Press"]


class Press:
    def __init__(self, hmm: str | PathLike[str], db: str | PathLike[str]):
        self._cpress = lib.dcp_press_new()
        if self._cpress == ffi.NULL:
            raise MemoryError()

        self._hmm = Path(hmm)
        self._db = Path(db)

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *_):
        self.close()
        return True

    def open(self):
        rc = lib.dcp_press_open(self._cpress, bytes(self._hmm), bytes(self._db))
        if rc:
            raise DeciphonError(rc)

    def close(self):
        rc = lib.dcp_press_close(self._cpress)
        if rc:
            raise DeciphonError(rc)

    def __len__(self):
        return lib.dcp_press_nproteins(self._cpress)

    def __iter__(self):
        return self

    def __next__(self):
        rc = lib.dcp_press_next(self._cpress)
        if rc:
            raise DeciphonError(rc)

        if lib.dcp_press_end(self._cpress):
            raise StopIteration

        return 1

    def __del__(self):
        lib.dcp_press_del(self._cpress)
