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
    'version': '0.2.3',
    'description': '',
    'long_description': '# sample-git-diffs\n\n```\nSample git diffs uniformly wrt. number of changes per file. The output is formatted as a .diff file.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --n N                 Total number of diffs to be sampled\n  --diffstat DIFFSTAT   Custom git diff command for the sampling probabilities\n  --diffcommand DIFFCOMMAND\n                        Custom git diff command for the actual diff\n```\n',
    'author': 'ninpnin',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ninpnin/sample-git-diffs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
