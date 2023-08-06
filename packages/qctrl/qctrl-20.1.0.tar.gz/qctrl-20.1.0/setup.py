# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrl',
 'qctrl.builders',
 'qctrl.builders.custom_handlers',
 'qctrl.builders.graphql_utils',
 'qctrl.builders.graphql_utils.handlers',
 'qctrl.qctrlauth',
 'qctrl.qctrlauth.tests',
 'qctrl.queries']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.3.0,<21.0.0',
 'boulder-opal-toolkits==2.0.0-beta.2',
 'cached-property>=1.5.1,<2.0.0',
 'click>=8.0,<9.0',
 'commonmark>=0.9.1,<0.10.0',
 'gql[requests]>=3.4.0,<4.0.0',
 'importlib-metadata>=4.12.0,<5.0.0',
 'inflection>=0.5.1,<0.6.0',
 'packaging>=22.0,<23.0',
 'pyjwt>=2.4.0,<3.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'python-forge>=18.6.0,<19.0.0',
 'pytz>=2020.1,<2021.0',
 'qctrl-commons>=17.8.0,<18.0.0',
 'qctrl-visualizer>=4.4.0,<5.0.0',
 'requests-oauthlib>=1.3.0,<2.0.0',
 'requests>=2.27.1,<2.28.0',
 'rich>=11.2.0,<12.0.0',
 'tenacity>=8.1.0,<9.0.0',
 'toml>=0.10.0,<0.11.0',
 'tqdm>=4.63.0',
 'typing-utils>=0.1.0,<0.2.0',
 'urllib3>=1.26.8,<1.27.0']

extras_require = \
{':python_full_version >= "3.7.2" and python_version < "3.8"': ['numpy>=1.21.6,<2.0.0'],
 ':python_version >= "3.8" and python_version < "3.12"': ['numpy>=1.23.5,<2.0.0']}

entry_points = \
{'console_scripts': ['qctrl = qctrl.scripts:main']}

setup_kwargs = {
    'name': 'qctrl',
    'version': '20.1.0',
    'description': 'Q-CTRL Python',
    'long_description': "# Q-CTRL Python\n\nThe Q-CTRL Python Package provides an intuitive and convenient Python interface\nto Q-CTRL's quantum control solutions for customers of Q-CTRL. To use the Q-CTRL\nPython Package, you will need a\n[Boulder Opal](https://q-ctrl.com/products/boulder-opal/) account.\n",
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<3.12',
}


setup(**setup_kwargs)
