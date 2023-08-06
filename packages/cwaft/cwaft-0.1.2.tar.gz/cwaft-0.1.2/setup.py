# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cwaft', 'cwaft.algorithms']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1,<2.0.0']

setup_kwargs = {
    'name': 'cwaft',
    'version': '0.1.2',
    'description': 'A Python library of mathematical tools and algorithms.',
    'long_description': '',
    'author': 'brentnequin',
    'author_email': 'brentnequin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/brentnequin/cwaft',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
