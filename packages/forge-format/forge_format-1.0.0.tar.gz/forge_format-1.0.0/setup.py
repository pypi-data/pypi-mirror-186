# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forgeformat']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.0.0',
 'click>=8.0.0',
 'forge-core>=1.0.0,<2.0.0',
 'ruff>=0.0.226,<0.0.227']

entry_points = \
{'console_scripts': ['forge-format = forgeformat:cli']}

setup_kwargs = {
    'name': 'forge-format',
    'version': '1.0.0',
    'description': 'Formatting library for Forge',
    'long_description': '# forge-format\n\nA unified, opinionated code formatting command for Django projects.\n\nUses [black](https://github.com/psf/black) and [ruff](https://github.com/charliermarsh/ruff/) to format Python code.\n\n\n## Installation\n\nFirst, install `forge-format` from [PyPI](https://pypi.org/project/forge-format/):\n\n```sh\npip install forge-format\n```\n\nNow you will have access to the `format` command:\n\n```sh\nforge format\n```\n',
    'author': 'Dave Gaeddert',
    'author_email': 'dave.gaeddert@dropseed.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.forgepackages.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
