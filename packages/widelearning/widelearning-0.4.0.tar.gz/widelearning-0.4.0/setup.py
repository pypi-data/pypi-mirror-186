# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['widelearning']
setup_kwargs = {
    'name': 'widelearning',
    'version': '0.4.0',
    'description': 'Library for searching the optimal neural network architecture',
    'long_description': 'None',
    'author': 'Brinkinvision',
    'author_email': 'brinkinvision@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
