# faultless: catch 'em segfaults!

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/dzshn/faultless/test.yml?style=for-the-badge)](https://github.com/dzshn/faultless/actions)
[![Codecov](https://img.shields.io/codecov/c/github/dzshn/faultless?style=for-the-badge)](https://app.codecov.io/gh/dzshn/faultless)
[![PyPI](https://img.shields.io/pypi/v/faultless?style=for-the-badge)](https://pypi.org/project/faultless)
![GitHub top language](https://img.shields.io/github/languages/top/dzshn/faultless?style=for-the-badge)

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

Install with pip: (only requires python 3.8 or higher)

```sh
$ pip install faultless
```

Install from source with [poetry](https://python-poetry.org/): (includes test tools)

```sh
$ git clone https://github.com/dzshn/faultless
$ cd faultless
$ poetry install
```

> **Note**
> Windows is currently unsupported. Other OSes (Linux, BSD, MacOS, anything POSIX) 
> will work fine and Cygwin and WSL likely work. Contributions are welcome!

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

uhhhhhhhhh

yeah you can do that
