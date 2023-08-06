# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kconvert']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['kconvert = bin2dec.bin2dec:main']}

setup_kwargs = {
    'name': 'kconvert',
    'version': '0.1.0',
    'description': 'Binary to decimal and decimal to binary converter',
    'long_description': '',
    'author': 'dongjin2008',
    'author_email': 'dkim@icsparis.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
