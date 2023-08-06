# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quqie',
 'quqie.core',
 'quqie.settings',
 'quqie.spiders',
 'quqie.utils',
 'quqie.web']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.5,<0.6']

entry_points = \
{'console_scripts': ['quqie-cli = quqie.cli:main']}

setup_kwargs = {
    'name': 'quqie',
    'version': '0.0.2',
    'description': '',
    'long_description': '# quqie\n\n[![ci](https://github.com/maguowei/quqie/actions/workflows/ci.yml/badge.svg)](https://github.com/maguowei/quqie/actions/workflows/ci.yml)\n[![Publish Python Package](https://github.com/maguowei/quqie/actions/workflows/publish.yml/badge.svg)](https://github.com/maguowei/quqie/actions/workflows/publish.yml)\n\n## Install\n\n```bash\n$ pip install quqie\n```\n\n## Dev\n```bash\n$ poetry run quqie-cli --help\n```',
    'author': 'maguowei',
    'author_email': 'imaguowei@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/maguowei/quqie',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
