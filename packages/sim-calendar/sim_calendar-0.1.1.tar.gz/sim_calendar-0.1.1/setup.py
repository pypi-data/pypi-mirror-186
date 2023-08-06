# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sim_calendar']

package_data = \
{'': ['*']}

install_requires = \
['datetime>=4.7,<5.0']

setup_kwargs = {
    'name': 'sim-calendar',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'Gabe Maayan',
    'author_email': 'gabemgem@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
