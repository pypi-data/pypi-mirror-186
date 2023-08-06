# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flow360', 'flow360.cli', 'flow360.cloud', 'flow360.component']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.63,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'h5py>=3.7.0,<4.0.0',
 'pydantic>=1.9.2,<2.0.0',
 'pytest>=7.1.2,<8.0.0',
 'requests>=2.28.1,<3.0.0',
 'toml>=0.10.2,<0.11.0']

extras_require = \
{':python_version >= "3.10" and python_version < "4.0"': ['numpy>=1.23.0,<2.0.0',
                                                          'matplotlib>=3.6.2,<4.0.0'],
 ':python_version >= "3.7" and python_version < "4.0"': ['numpy>=1.19.0,<2.0.0',
                                                         'matplotlib>=3.5.3,<4.0.0'],
 ':python_version >= "3.8" and python_version < "4.0"': ['numpy>=1.20.0,<2.0.0',
                                                         'matplotlib>=3.6.2,<4.0.0'],
 ':python_version >= "3.9" and python_version < "4.0"': ['numpy>=1.23.0,<2.0.0',
                                                         'matplotlib>=3.6.2,<4.0.0']}

entry_points = \
{'console_scripts': ['flow360 = flow360.cli:flow360']}

setup_kwargs = {
    'name': 'flow360',
    'version': '0.1.5',
    'description': '',
    'long_description': 'None',
    'author': 'Flexcompute',
    'author_email': 'support@flexcompute.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
