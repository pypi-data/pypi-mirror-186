# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sample_git_diffs']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.0,<2.0.0']

entry_points = \
{'console_scripts': ['sample-git-diffs = '
                     'sample_git_diffs.sample_git_diffs:cli']}

setup_kwargs = {
    'name': 'sample-git-diffs',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ninpnin',
    'author_email': 'vainoyrjanainen@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
