"""Catch abnormal program state. Allows handling segfaults & more."""

import functools
import gc
import inspect
import os
import pickle
import signal
from multiprocessing.shared_memory import SharedMemory
from sys import byteorder, maxsize
from typing import Any, Callable, TypeVar, cast

__all__ = ["Interrupt", "SignalInterrupt", "SegmentationFault", "faultless"]
__version__ = "1.0.1"

F = TypeVar("F", bound=Callable[..., Any])

MAX_ADDR = maxsize.bit_length() + 1


class Interrupt(OSError):
    """OS or program interrupt caught."""

    def __init__(self, exit_code: int) -> None:
        self.exit_code = exit_code
        super().__init__(exit_code)

    def __str__(self) -> str:
        if self.exit_code & ~0xFFFF:
            return "caught unknown status"  # pragma: no cover
        if self.exit_code:
            return f"caught non-zero status: {self.exit_code}"
        return "caught abrupt exit with status 0"


class SignalInterrupt(Interrupt):
    """Signal interrupt caught."""

    def __str__(self) -> str:
        sig = -self.exit_code
        desc = signal.strsignal(sig)
        name = signal.Signals(sig).name
        msg = f"{name} caught: {desc}"
        if os.WCOREDUMP(self.exit_code):
            msg += " (core dumped)"
        return msg


class SegmentationFault(SignalInterrupt):
    """Segmentation fault (SIGSEGV) caught."""

    def __init__(self) -> None:
        super().__init__(exit_code=-signal.SIGSEGV)


def faultless(fn: F) -> F:
    """Decorate a function so abnormal state can be caught.

    Raises
    ------
    SegmentationFault
        The function segfaulted.
    SignalInterrupt
        The function was killed by signal.
    Interrupt
        The function exit abruptly
    """

    if inspect.isgeneratorfunction(fn):
        raise ValueError("callable can't be a generator")  # TODO: or could it be?

    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # this suffix tries to be unique to each function & invdividual calls
        name_suffix = (
            ((hash(fn) ^ hash(args) ^ hash(tuple(kwargs.values()))) & 0xFF_FF_FF_FF)
            .to_bytes(4, byteorder)
            .hex()
        )

        # first shared memory, which holds 0xFF + the length of the next shmem in bytes
        mem0 = SharedMemory("_cat0_" + name_suffix, create=True, size=MAX_ADDR + 1)
        pid = os.fork()
        if hasattr(gc, "freeze"):
            gc.freeze()
        if pid == 0:  # pragma: no cover (lol)
            try:
                try:
                    res = (False, fn(*args, **kwargs))
                except Exception as e:
                    res = (True, e)
                try:
                    data = pickle.dumps(res)
                except pickle.PicklingError as e:
                    data = pickle.dumps((True, e))
                mem0.buf[:] = b"\xff" + len(data).to_bytes(MAX_ADDR, byteorder)
                data_mem = SharedMemory(
                    "_cat1_" + name_suffix, create=True, size=len(data)
                )
                data_mem.buf[:] = data
            except SystemExit as e:
                if e.code is None:
                    os._exit(0)
                if isinstance(e.code, str):
                    os._exit(1)
                os._exit(e.code)
            finally:
                os._exit(0)

        if hasattr(gc, "unfreeze"):
            gc.unfreeze()
        try:
            _, code = os.waitpid(pid, 0)
            # if 0xFF didn't get set, our child exploded, raise appropriate error
            if mem0.buf[0] != 0xFF:
                if os.WIFEXITED(code):
                    raise Interrupt(os.WEXITSTATUS(code))
                elif os.WIFSIGNALED(code):
                    exit_signal = os.WTERMSIG(code)
                    if exit_signal == signal.SIGSEGV:
                        raise SegmentationFault()
                    raise SignalInterrupt(-exit_signal)
                raise RuntimeError(f"invalid return code: {code}")  # pragma: no cover
            size = int.from_bytes(mem0.buf[1:], byteorder)
            data_mem = SharedMemory("_cat1_" + name_suffix, size=size)
            if size != data_mem.size:  # pragma: no cover
                raise RuntimeError("shared memory is potentially corrupt, congrats")
            res = pickle.loads(data_mem.buf)
            if res[0]:
                raise res[1]
            return res[1]
        finally:
            mem0.unlink()
            try:
                data_mem.unlink()
            except NameError:
                pass

    return cast(F, wrapper)
