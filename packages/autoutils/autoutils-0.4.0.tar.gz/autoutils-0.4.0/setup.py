# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autoutils', 'autoutils.matrixcli']

package_data = \
{'': ['*']}

install_requires = \
['blessings>=1.0,<2.0',
 'func-timeout>=4.0,<5.0',
 'paramiko>=2.0,<3.0',
 'persiantools>=2.0,<3.0',
 'pytz>=2022.1,<2023.0',
 'redis>=4.0,<5.0',
 'requests>=2.0,<3.0',
 'sshtunnel>=0.1,<1.0',
 'urllib3>=1.0,<2.0']

setup_kwargs = {
    'name': 'autoutils',
    'version': '0.4.0',
    'description': 'Some Good Function',
    'long_description': '# autoutils',
    'author': 'Reza Zeiny',
    'author_email': 'rezazeiny1998@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rezazeiny/autoutils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
