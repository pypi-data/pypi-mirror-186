# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wearipedia',
 'wearipedia.devices',
 'wearipedia.devices.dexcom',
 'wearipedia.devices.dreem',
 'wearipedia.devices.fitbit',
 'wearipedia.devices.garmin',
 'wearipedia.devices.oura',
 'wearipedia.devices.polar',
 'wearipedia.devices.whoop',
 'wearipedia.devices.withings']

package_data = \
{'': ['*']}

install_requires = \
['garminconnect>=0.1.48,<0.2.0',
 'pandas>=1.1,<2.0',
 'rich>=12.6.0,<13.0.0',
 'scipy>=1.6,<2.0',
 'tqdm>=4.64.1,<5.0.0',
 'typer[all]>=0.6.1,<0.7.0',
 'wget>=3.2,<4.0']

entry_points = \
{'console_scripts': ['wearipedia = wearipedia.__main__:app']}

setup_kwargs = {
    'name': 'wearipedia',
    'version': '0.1.0',
    'description': 'wearables in development',
    'long_description': '# wearipedia\n\n<div align="center">\n\n[![Build status](https://github.com/Stanford-Health/wearipedia/workflows/build/badge.svg?branch=master&event=push)](https://github.com/Stanford-Health/wearipedia/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/wearipedia.svg)](https://pypi.org/project/wearipedia/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Stanford-Health/wearipedia/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Stanford-Health/wearipedia/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Stanford-Health/wearipedia/releases)\n[![License](https://img.shields.io/github/license/Stanford-Health/wearipedia)](https://github.com/Stanford-Health/wearipedia/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\n</div>\n\n<h3 align="center">\n    <p>A one-stop shop for wearable device data extraction and simulation</p>\n</h3>\n\nWearipedia provides a one-stop shop for accessing and extracting data from wearable devices.\n\nData from these devices may be used for:\n\n* Clinical research\n* Personal health monitoring\n* Health coaching\n* Health product development\n* Wearable device development\n\nWearipedia is developed and maintained by the [Snyder Lab](https://med.stanford.edu/snyderlab.html) at the Stanford University.\n\n## Accessing data from wearable devices\n\nThe data from these devices is accessed using an easy-to-use API. In order to use this API, you will need to import the `wearipedia` module:\n\n```python\nimport wearipedia\n```\n\nOnce you have imported the `wearipedia` module, accessing data from any wearable device is as easy as:\n\n```python\ndevice = wearipedia.get_device("whoop/whoop_4")\ndevice.authenticate({"email": "joesmith@gmail.com", "password": "foobar"})\n\n# data is a DataFrame\ndata = device.get_data("metrics")\n```\n\nIf you don\'t have access to your device, or need to demo data from a device without revealing your sensitive data or getting a device yourself, you can generate synthetic data, as shown below:\n\n```python\ndevice = wearipedia.get_device("whoop/whoop_4")\n\n# data is an automatically generated DataFrame\ndata = device.get_data("metrics")\n```\n\nand you\'re done!\n\n## Installing\n\nThe easiest way to install wearipedia is to use pip:\n\n`pip install wearipedia`\n\nWe currently support Python 3.7, 3.8, and 3.9.\n\n## Supported Devices\n\nWearipedia supports the following devices:\n\n| Company | Model Name | Description | Example Notebook | Kinds of Data Available | Unique name |\n|---|---|---|---|---|---|\n| [Whoop](https://www.whoop.com/) | Whoop | The WHOOP 4.0 strap tracks sleep and activity data. | [Notebook](https://github.com/snyder-lab/wearipedia/blob/master/notebooks/whoop/Example%20Notebook.ipynb) | cycles, hr. | `whoop/whoop_4` |\n| [Garmin](https://www.garmin.com/en-US) | Fenix 7S | The Garmin Fenix 7S is a watch that activity data. | [Notebook](https://github.com/snyder-lab/wearipedia/blob/master/notebooks/garmin/Example%20Notebook.ipynb) |  dates, steps, hrs, brpms. | `garmin/fenix_7s` |\n| [Dexcom](https://www.dexcom.com/) | Pro CGM | The Dexcom Pro CGM wearable device tracks blood sugar levels. | [Notebook](https://github.com/snyder-lab/wearipedia/blob/master/notebooks/dexcom/Example%20Notebook.ipynb) |  dataframe. | `dexcom/pro_cgm` |\n| [Withings](https://www.withings.com) | Body+ | The Withings Body+ is a smart scale that tracks weight and other metrics (body fat %). | [Notebook](https://github.com/snyder-lab/wearipedia/blob/master/notebooks/withings/Example%20Notebook.ipynb) | measurements. | `withings/bodyplus` |\n| [Withings](https://www.withings.com) | ScanWatch | The Withings ScanWatch wearable device tracks sleep and activity data. | [Notebook](https://github.com/snyder-lab/wearipedia/blob/master/notebooks/withings/Example%20Notebook.ipynb) | heart_rates, sleeps. | `withings/scanwatch` |\n\n## Documentation\n\nFor more information on how to use wearipedia, please refer to our [documentation](https://wearipedia.readthedocs.io).\n\n## Citing\n\nA paper is in progress!\n\n## Disclaimer\n\nThis project is currently in *alpha*. This means that formal tests are not yet integrated, and the codebase is still really a prototype. Expect for most things to work, but also small bugs, rough edges, and sparse documentation.\n\n## Contributing\n\nAs Wearipedia is still at an early stage, we are not yet accepting contributions from the broader community. Once Wearipedia reaches its first stable release, we will begin accepting contributions.\n\n## License\n\nWearipedia is released under the MIT license.\n\n## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)\n',
    'author': 'Rodrigo Castellon',
    'author_email': 'rjcaste@stanford.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rodrigo-castellon/wearipedia',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
