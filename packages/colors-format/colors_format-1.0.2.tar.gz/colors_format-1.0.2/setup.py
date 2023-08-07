# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['colors_format']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'colors-format',
    'version': '1.0.2',
    'description': 'Tired of having to type up ANSI escape codes whenever you want to color some text, then use this package, Note: this only supports a few colors for now.',
    'long_description': None,
    'author': 'Stefan Dikov',
    'author_email': 'stefan.v.dikov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
