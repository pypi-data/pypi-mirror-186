from deciphon.cffi import ffi, lib

__all__ = ["DeciphonError"]


class DeciphonError(Exception):
    def __init__(self, errno: int):
        msg = ffi.string(lib.dcp_strerror(errno)).decode()
        super().__init__(f"Deciphon error: {msg}")
