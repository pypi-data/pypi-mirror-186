# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forgetest']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0',
 'coverage>=7.0.1,<8.0.0',
 'forge-core>=1.0.0,<2.0.0',
 'pytest-django>=4.5.2,<5.0.0',
 'pytest>=7.0.0,<8.0.0']

entry_points = \
{'console_scripts': ['forge-test = forgetest:cli']}

setup_kwargs = {
    'name': 'forge-test',
    'version': '1.0.0',
    'description': 'Testing for Forge',
    'long_description': '# forge-test\n',
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
