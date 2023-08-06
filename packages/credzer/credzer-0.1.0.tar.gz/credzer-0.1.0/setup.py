# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['credzer', 'credzer.lib']

package_data = \
{'': ['*']}

install_requires = \
['tinydb>=4.7.0,<5.0.0']

entry_points = \
{'console_scripts': ['credzer = credzer.credzer:main']}

setup_kwargs = {
    'name': 'credzer',
    'version': '0.1.0',
    'description': 'One to rule them all',
    'long_description': 'None',
    'author': 'shoxxdj',
    'author_email': 'remi.martin-de-abia@advens.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
