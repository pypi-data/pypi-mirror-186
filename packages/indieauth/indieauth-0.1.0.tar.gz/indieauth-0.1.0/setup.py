# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['indieauth']
install_requires = \
['pycryptodome>=3.15.0,<4.0.0', 'txtint>=0.0', 'webcli>=0.0']

entry_points = \
{'console_scripts': ['indieauth = indieauth:main']}

setup_kwargs = {
    'name': 'indieauth',
    'version': '0.1.0',
    'description': 'utilities for implementing IndieAuth clients and servers',
    'long_description': 'None',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
