# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fluxwallet',
 'fluxwallet.config',
 'fluxwallet.services',
 'fluxwallet.tools',
 'fluxwallet.transactions']

package_data = \
{'': ['*'], 'fluxwallet': ['data/*', 'wordlist/*']}

install_requires = \
['SQLAlchemy>=1.4.28,<2.0.0',
 'numpy>=1.21.0,<2.0.0',
 'pycryptodome>=3.14.1,<4.0.0',
 'requests>=2.25.0,<3.0.0']

extras_require = \
{':sys_platform != "win32"': ['fastecdsa>=2.2.1,<3.0.0'],
 ':sys_platform == "win32"': ['ecdsa>=0.17,<0.18']}

entry_points = \
{'console_scripts': ['fluxwallet = fluxwallet.tools.clw:main']}

setup_kwargs = {
    'name': 'fluxwallet',
    'version': '0.0.1',
    'description': 'A Wallet implementation for Flux (based on fluxwallet)',
    'long_description': 'None',
    'author': 'David White',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': '',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
