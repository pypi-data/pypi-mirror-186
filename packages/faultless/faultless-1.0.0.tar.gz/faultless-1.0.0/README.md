# faultless: catch 'em segfaults!

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/dzshn/faultless/test.yml)](https://github.com/dzshn/faultless/actions)
[![Codecov](https://img.shields.io/codecov/c/github/dzshn/faultless)](https://app.codecov.io/gh/dzshn/faultless)
![GitHub top language](https://img.shields.io/github/languages/top/dzshn/faultless)

```py
import ctypes
from faultless import faultless, SegmentationFault


@faultless
def nullptr():
    return ctypes.c_void_p.from_address(0).value


try:
    nullptr()
except SegmentationFault:
    print("Safe!")
```

## Installation

Install with pip:

```sh
$ pip install git+https://github.com/dzshn/faultless
```

From source using [poetry](https://python-poetry.org):

```sh
$ poetry install
```

## Usage

A complete summary of the library is as follows:

```py
from faultless import Interrupt, SignalInterrupt, SegmentationFault, faultless

@faultless
def dangerous_function():
    ...

try:
    result = dangerous_function()

except SegmentationFault:
    # the function segfaulted
    ...
except SignalInterrupt:
    # the function was killed by a signal (e.g. `SIGKILL`)
    ...
except Interrupt:
    # the function has exit abruptly (e.g. `exit()`)
    ...
except Exception:
    # the function itself raised an exception
    ...
```

Functions wrapped by `faultless` will be unable to crash the interpreter
directly. It does, in short, execute the function in a fork, so that any sort
of fault can be handled. Currently, return values and exceptions are handled
correctly, but non-local variables aren't, so be wary of changing global state.

## wait what do you mean segfaults and python w-

yeah. you can do that. and I've done it too much
