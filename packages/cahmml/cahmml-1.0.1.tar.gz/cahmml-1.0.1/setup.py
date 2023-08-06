# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cahmml', 'cahmml.test']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.5,<2.0.0', 'rich>=12.6.0,<13.0.0']

setup_kwargs = {
    'name': 'cahmml',
    'version': '1.0.1',
    'description': 'Custom Lambda HMM Library',
    'long_description': None,
    'author': 'Ryan Eveloff, Denghui Chen',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
