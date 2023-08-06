# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['beauty-mouse']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=39.0.0,<40.0.0',
 'pyinstaller>=5.7.0,<6.0.0',
 'pynput==1.7.6',
 'pyopenssl>=23.0.0,<24.0.0']

entry_points = \
{'console_scripts': ['greet = beauty-mouse.main:main']}

setup_kwargs = {
    'name': 'beauty-mouse',
    'version': '0.1.0',
    'description': 'Fuck cima',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
