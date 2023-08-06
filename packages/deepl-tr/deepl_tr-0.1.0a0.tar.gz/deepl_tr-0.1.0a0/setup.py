# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deepl_tr']

package_data = \
{'': ['*']}

install_requires = \
['icecream>=2.1.1,<3.0.0',
 'install>=1.3.5,<2.0.0',
 'logzero>=1.7.0,<2.0.0',
 'set-loglevel>=0.1.2,<0.2.0',
 'typer>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['deepl-tr-webui = deepl_tr.__main__:app']}

setup_kwargs = {
    'name': 'deepl-tr',
    'version': '0.1.0a0',
    'description': 'deepl_tr',
    'long_description': '# deepl-tr\n[![pytest](https://github.com/ffreemt/deepl-tr-webui/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/deepl-tr-webui/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/deepl_tr.svg)](https://badge.fury.io/py/deepl-tr)\n\ndeepl translate using deepl-fastapi and webui2\n\n## Install it\n\n```shell\npip install deepl-tr\n# pip install git+https://github.com/ffreemt/deepl-tr-webui\n# poetry add git+https://github.com/ffreemt/deepl-tr-webui\n# git clone https://github.com/ffreemt/deepl-tr-webui && cd deepl-tr-webui\n```\n\n## Use it\n```bash\npython -m deepl-tr\n\n# or\ndeepl-tr\n\n```\n',
    'author': 'ffreemt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ffreemt/deepl-tr-webui',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.3,<4.0.0',
}


setup(**setup_kwargs)
