# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['embodyserial']

package_data = \
{'': ['*']}

install_requires = \
['embody-codec>=1.0.12', 'pyserial>=3.5,<4.0']

entry_points = \
{'console_scripts': ['embody-serial = embodyserial.cli:main']}

setup_kwargs = {
    'name': 'embody-serial',
    'version': '1.0.11',
    'description': 'Communicate with the embody device over a serial port',
    'long_description': '# Embody Serial\n\n[![PyPI](https://img.shields.io/pypi/v/embody-serial.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/embody-serial.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/embody-serial)][python version]\n[![License](https://img.shields.io/pypi/l/embody-serial)][license]\n\n[![Tests](https://github.com/aidee-health/embody-serial/workflows/Tests/badge.svg)][tests]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/embody-serial/\n[status]: https://pypi.org/project/embody-serial/\n[python version]: https://pypi.org/project/embody-serial\n[tests]: https://github.com/aidee-health/embody-serial/actions?workflow=Tests\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- Connects to an EmBody device over the serial port\n- Uses the EmBody protocol to communicate with the device\n- Integrates with [the EmBody Protocol Codec](https://github.com/aidee-health/embody-protocol-codec) project\n- Asynchronous send without having to wait for response\n- Synchronous send where response message is returned\n- Send facade for protocol agnostic communication with device\n- Provides callback interfaces for incoming messages, response messages and connect/disconnect\n- All methods and callbacks are threadsafe\n- Separate threads for send, receive and callback processing\n- Type safe code using [mypy](https://mypy.readthedocs.io/) for type checking\n\n## Requirements\n\n- Python 3.9\n- Access to private Aidee Health repositories on Github\n\n## Installation\n\nYou can install _Embody Serial_ via [pip]:\n\n```console\n$ pip install embody-serial\n```\n\nThis adds `embody-serial` as a library, but also provides the CLI application with the same name.\n\n## Usage\n\nA very basic example where you send a message request and get a response:\n\n```python\nfrom embodyserial.embodyserial import EmbodySerial\nfrom embodyserial.helpers import EmbodySendHelper\n\nembody_serial = EmbodySerial()\nsend_helper = EmbodySendHelper(sender=embody_serial)\nprint(f"Serial no: {send_helper.get_serial_no()}")\nembody_serial.shutdown()\n```\n\nIf you want to see more of what happens under the hood, activate debug logging before setting up `EmbodySerial`:\n\n```python\nimport logging\n\nlogging.basicConfig(level=logging.DEBUG)\n```\n\n## Using the application from the command line\n\nThe application also provides a CLI application that is automatically added to the path when installing via pip.\n\nOnce installed with pip, type:\n\n```\nembody-serial --help\n```\n\nTo see which options are available.\n\n> **Note**\n> The serial port is automatically detected, but can be overridden by using the `--device` option.\n\n### Example - List all attribute values\n\n```shell\nembody-serial --get-all\n```\n\n### Example - Get serial no of device\n\n```shell\nembody-serial --get serialno\n```\n\n### Example - List files over serial port\n\n```shell\nembody-serial --list-files\n```\n\n### Example - Set time current time (UTC)\n\n```shell\nembody-serial --set-time\n```\n\n### Example - Download files\n\n```shell\nembody-serial --download-files\n```\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n[file an issue]: https://github.com/aidee-health/embody-serial/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/aidee-health/embody-serial/blob/main/LICENSE\n[contributor guide]: https://github.com/aidee-health/embody-serial/blob/main/CONTRIBUTING.md\n[command-line reference]: https://embody-serial.readthedocs.io/en/latest/usage.html\n',
    'author': 'Aidee Health AS',
    'author_email': 'hello@aidee.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aidee-health/embody-serial',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
