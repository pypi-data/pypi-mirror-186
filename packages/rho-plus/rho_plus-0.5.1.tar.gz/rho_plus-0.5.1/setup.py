# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rho_plus', 'rho_plus.data']

package_data = \
{'': ['*'], 'rho_plus.data': ['fonts/*']}

install_requires = \
['hsluv>=5.0.3,<6.0.0', 'numpy>=1.21']

extras_require = \
{':(python_version >= "3.8" and python_version < "3.9") and (extra == "dev")': ['colour-science==0.4.1'],
 ':extra == "dev"': ['scipy>=1.7.0', 'matplotlib>=3,<4', 'seaborn>=0.11'],
 ':python_version >= "3.9" and python_version <= "3.11"': ['colour-science==0.4.2']}

setup_kwargs = {
    'name': 'rho-plus',
    'version': '0.5.1',
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
    'extras_require': extras_require,
    'python_requires': '>=3.8,<=3.11',
}


setup(**setup_kwargs)
