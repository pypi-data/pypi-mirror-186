# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymtom']

package_data = \
{'': ['*']}

install_requires = \
['zeep>=4.2.1,<5.0.0']

setup_kwargs = {
    'name': 'pymtom',
    'version': '0.1.2',
    'description': './README.md',
    'long_description': None,
    'author': 'Mirek Zvolský',
    'author_email': 'zvolsky@seznam.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
