# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faultless']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'faultless',
    'version': '1.0.1',
    'description': 'Catch segfaults as normal exceptions',
    'long_description': '# faultless: catch \'em segfaults!\n\n[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/dzshn/faultless/test.yml?style=for-the-badge)](https://github.com/dzshn/faultless/actions)\n[![Codecov](https://img.shields.io/codecov/c/github/dzshn/faultless?style=for-the-badge)](https://app.codecov.io/gh/dzshn/faultless)\n[![PyPI](https://img.shields.io/pypi/v/faultless?style=for-the-badge)](https://pypi.org/project/faultless)\n![GitHub top language](https://img.shields.io/github/languages/top/dzshn/faultless?style=for-the-badge)\n\n```py\nimport ctypes\nfrom faultless import faultless, SegmentationFault\n\n\n@faultless\ndef nullptr():\n    return ctypes.c_void_p.from_address(0).value\n\n\ntry:\n    nullptr()\nexcept SegmentationFault:\n    print("Safe!")\n```\n\n## Installation\n\nInstall with pip: (only requires python 3.8 or higher)\n\n```sh\n$ pip install faultless\n```\n\nInstall from source with [poetry](https://python-poetry.org/): (includes test tools)\n\n```sh\n$ git clone https://github.com/dzshn/faultless\n$ cd faultless\n$ poetry install\n```\n\n> **Note**\n> Windows is currently unsupported. Other OSes (Linux, BSD, MacOS, anything POSIX) \n> will work fine and Cygwin and WSL likely work. Contributions are welcome!\n\n## Usage\n\nA complete summary of the library is as follows:\n\n```py\nfrom faultless import Interrupt, SignalInterrupt, SegmentationFault, faultless\n\n@faultless\ndef dangerous_function():\n    ...\n\ntry:\n    result = dangerous_function()\n\nexcept SegmentationFault:\n    # the function segfaulted\n    ...\nexcept SignalInterrupt:\n    # the function was killed by a signal (e.g. `SIGKILL`)\n    ...\nexcept Interrupt:\n    # the function has exit abruptly (e.g. `exit()`)\n    ...\nexcept Exception:\n    # the function itself raised an exception\n    ...\n```\n\nFunctions wrapped by `faultless` will be unable to crash the interpreter\ndirectly. It does, in short, execute the function in a fork, so that any sort\nof fault can be handled. Currently, return values and exceptions are handled\ncorrectly, but non-local variables aren\'t, so be wary of changing global state.\n\n## wait what do you mean segfaults and python w-\n\nuhhhhhhhhh\n\nyeah you can do that\n',
    'author': 'Sofia Lima',
    'author_email': 'me@dzshn.xyz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dzshn/faultless',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
