# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dral',
 'dral.adapter',
 'dral.devices',
 'dral.devices.arm',
 'dral.devices.arm.example',
 'dral.devices.stm32',
 'dral.devices.stm32.f4',
 'dral.filter',
 'dral.format',
 'dral.templates',
 'dral.templates.dral',
 'dral.templates.mbedAutomatify']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1,<9.0',
 'pylama[all]>=8.4.1,<9.0.0',
 'rich>=12.5,<13.0',
 'svd2py>=0.1,<0.2']

entry_points = \
{'console_scripts': ['dral = dral.app:cli']}

setup_kwargs = {
    'name': 'dral',
    'version': '0.3.2',
    'description': 'D-RAL - Device Register Access Layer',
    'long_description': '![Logo](https://raw.githubusercontent.com/gembcior/d-ral/main/doc/logo.svg)\n\n<h1 align="center">D-RAL - Device Register Access Layer</h1>\n\n[![PyPI](https://img.shields.io/pypi/v/dral?label=dral)](https://pypi.org/project/dral/)\n[![PyPI - License](https://img.shields.io/pypi/l/dral)](https://pypi.org/project/dral/)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/dral)](https://pypi.org/project/dral/)\n[![PyPI - Format](https://img.shields.io/pypi/format/dral)](https://pypi.org/project/dral/)\n[![PyPI - Wheel](https://img.shields.io/pypi/wheel/dral)](https://pypi.org/project/dral/)\n\n---\n\n### Introduction\n\n### Installing\n\n### Usage\n',
    'author': 'Gembcior',
    'author_email': 'gembcior@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gembcior/d-ral',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
