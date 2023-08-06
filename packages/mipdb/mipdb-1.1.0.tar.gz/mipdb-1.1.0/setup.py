# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mipdb']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.3,<1.4',
 'click>=8.1,<8.2',
 'pandas>=1.5,<1.6',
 'pandera>=0.13,<0.14',
 'pymonetdb>=1.6,<1.7',
 'sqlalchemy_monetdb>=1.0,<1.1']

entry_points = \
{'console_scripts': ['mipdb = mipdb.commands:entry']}

setup_kwargs = {
    'name': 'mipdb',
    'version': '1.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
