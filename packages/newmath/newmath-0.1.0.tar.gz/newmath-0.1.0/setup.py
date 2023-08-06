# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['newmath']
install_requires = \
['pycryptodome>=3.15.0,<4.0.0']

setup_kwargs = {
    'name': 'newmath',
    'version': '0.1.0',
    'description': 'utilities for using NewBase60',
    'long_description': 'None',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
