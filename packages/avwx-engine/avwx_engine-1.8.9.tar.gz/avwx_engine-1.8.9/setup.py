# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['avwx',
 'avwx.current',
 'avwx.data',
 'avwx.forecast',
 'avwx.parsing',
 'avwx.parsing.translate',
 'avwx.service',
 'avwx.static',
 'avwx.station']

package_data = \
{'': ['*'], 'avwx.data': ['files/*']}

install_requires = \
['geopy>=2.2', 'httpx>=0.23', 'python-dateutil>=2.8', 'xmltodict>=0.13']

extras_require = \
{':python_version < "3.10"': ['typing_extensions>=4.4'],
 'all': ['rapidfuzz>=2.3', 'scipy>=1.9', 'shapely>=1.8'],
 'fuzz': ['rapidfuzz>=2.3'],
 'scipy': ['scipy>=1.9'],
 'shape': ['shapely>=1.8']}

setup_kwargs = {
    'name': 'avwx-engine',
    'version': '1.8.9',
    'description': 'Aviation weather report parsing library',
    'long_description': "# AVWX\n\n![AVWX logo](docs/assets/images/avwx-logo-color-200.png)\n\n[![PyPI](https://img.shields.io/pypi/v/avwx-engine?style=flat)](https://pypi.python.org/pypi/avwx-engine/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/avwx-engine?style=flat)](https://pypi.python.org/pypi/avwx-engine/)\n[![PyPI - License](https://img.shields.io/pypi/l/avwx-engine?style=flat)](https://pypi.python.org/pypi/avwx-engine/)\n[![GitHub - Test Suite Status](https://github.com/avwx-rest/avwx-engine/actions/workflows/test.yml/badge.svg)]()\n\n---\n\n**Documentation**: [https://engine.avwx.rest](https://engine.avwx.rest)\n\n**Source Code**: [https://github.com/avwx-rest/avwx-engine](https://github.com/avwx-rest/avwx-engine)\n\n**PyPI**: [https://pypi.org/project/avwx-engine/](https://pypi.org/project/avwx-engine/)\n\n---\n\nAVWX is a global aviation weather fetching and parsing engine. It sources reports from a variety of government sources, parses individual elements, and calculates additional information like flight rules and time range interpolation.\n\nAVWX currently supports:\n\n- Station data and search\n- METAR\n- TAF\n- PIREP\n- AIRMET / SIGMET\n- NOTAM\n- NBM (NBH, NBS, NBE)\n- GFS (MAV, MEX)\n\n## Install\n\nThe easiest way to get started is to download the library from pypi using pip:\n\n```bash\npython -m pip install avwx-engine\n```\n\n## Basic Usage\n\nReports use ICAO, IATA, or GPS idents when specifying the desired station. Exceptions are thrown if a potentially invalid ident is given.\n\n```python\n>>> import avwx\n>>>\n>>> metar = avwx.Metar('KJFK')\n>>> metar.station.name\n'John F Kennedy International Airport'\n>>> metar.update()\nTrue\n>>> metar.data.flight_rules\n'IFR'\n```\n\nYou can learn more by reading the [project documentation](https://engine.avwx.rest)\n\n**Note**: This library requires Python 3.8 or above\n\n## Development\n\nDownload and install the source code and its development dependencies:\n\n* Clone this repository\n\n```sh\ngit clone https://github.com/avwx-rest/avwx-engine\ncd avwx-engine\n```\n\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.8+\n* Create a virtual environment and install the dependencies\n\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n\n```sh\npoetry shell\n```\n\n### Testing\n\nThe test suite was built while using the `pytest` library, which is also installed as a dev dependency.\n\n```bash\npytest\n```\n\nThe end-to-end test files were generated using `util/build_tests.py` and placed into `tests/{report}/data`. Because Timestamp generation interprets the text based on the current date, Timestamp objects are nullified in the end-to-end tests.\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings of the public signatures of the source code. The documentation is updated and published to [engine.avwx.rest](https://engine.avwx.rest) automatically as part each release.\n\n You can also preview local changes during development:\n\n```sh\ncd docs\nmkdocs serve\n```\n\n### Releasing\n\nTrigger the [Draft release workflow](https://github.com/avwx-rest/avwx-engine/actions/workflows/draft_release.yml) (press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.\n\nFind the draft release from the\n[GitHub releases](https://github.com/avwx-rest/avwx-engine/releases) and publish it. When a release is published, it'll trigger [release](https://github.com/avwx-rest/avwx-engine/blob/main/.github/workflows/release.yml) workflow which creates PyPI\n release and deploys updated documentation.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters, linters, and other quality checks to make sure the changeset is in good shape before a commit/push happens.\n\nYou can install the hooks with (runs for each commit):\n\n```sh\npre-commit install\n```\n\nOr if you want them to run only for each push:\n\n```sh\npre-commit install -t pre-push\n```\n\nOr if you want e.g. want to run all checks manually for all files:\n\n```sh\npre-commit run --all-files\n```\n",
    'author': 'Michael duPont',
    'author_email': 'michael@dupont.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://engine.avwx.rest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
