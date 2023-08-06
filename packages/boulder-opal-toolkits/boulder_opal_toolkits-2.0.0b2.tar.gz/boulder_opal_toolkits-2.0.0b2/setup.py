# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boulderopaltoolkits',
 'boulderopaltoolkits.closed_loop',
 'boulderopaltoolkits.deprecated',
 'boulderopaltoolkits.ions',
 'boulderopaltoolkits.signals',
 'boulderopaltoolkits.superconducting',
 'boulderopaltoolkits.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpydoc>=1.1.0,<2.0.0',
 'packaging>=22.0,<23.0',
 'python-forge>=18.6.0,<19.0.0',
 'qctrl-commons>=17.8.0,<18.0.0',
 'toml>=0.10.0,<0.11.0']

extras_require = \
{':python_full_version >= "3.7.2" and python_version < "3.8"': ['numpy>=1.21.6,<2.0.0',
                                                                'scipy>=1.7.3'],
 ':python_version >= "3.8" and python_version < "3.12"': ['numpy>=1.23.5,<2.0.0',
                                                          'scipy>=1.9.3']}

setup_kwargs = {
    'name': 'boulder-opal-toolkits',
    'version': '2.0.0b2',
    'description': 'Q-CTRL Boulder Opal Toolkits',
    'long_description': '# Q-CTRL Boulder Opal Toolkits\n\nToolkit of convenience functions and classes for Boulder Opal.\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.2,<3.12',
}


setup(**setup_kwargs)
