# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rho_plus', 'rho_plus.data']

package_data = \
{'': ['*'], 'rho_plus.data': ['fonts/*']}

install_requires = \
['scipy>=1.7.0']

setup_kwargs = {
    'name': 'rho-plus',
    'version': '0.4.6',
    'description': 'Aesthetic and ergonomic enhancements to common Python data science tools',
    'long_description': None,
    'author': 'Nicholas Miklaucic',
    'author_email': 'nicholas.miklaucic@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
