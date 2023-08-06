# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['glorious']

package_data = \
{'': ['*']}

install_requires = \
['aenum>=3.1.11,<4.0.0', 'hidapi>=0.13.1,<0.14.0']

setup_kwargs = {
    'name': 'glorious',
    'version': '0.1.2',
    'description': 'Library to interface with Glorious devices',
    'long_description': '# Glorious\nA Python library to interface with Glorious devices. Still heavily in development!\n\n## Usage\nYou can install the library with pip: `pip install glorious`\n',
    'author': 'Kavi Bidlack',
    'author_email': 'ksbidlack@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kbidlack/glorious',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
