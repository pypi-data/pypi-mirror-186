# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dumbo_esse3']

package_data = \
{'': ['*']}

install_requires = \
['dateutils>=0.6.12,<0.7.0',
 'dumbo-utils>=0.1.4,<0.2.0',
 'lxml>=4.9.2,<5.0.0',
 'selenium>=4.4.3,<5.0.0']

setup_kwargs = {
    'name': 'dumbo-esse3',
    'version': '0.3.19',
    'description': 'Esse3 command line utility, to save my future time!',
    'long_description': 'None',
    'author': 'Mario Alviano',
    'author_email': 'mario.alviano@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
