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
    'version': '0.1.0',
    'description': 'Library to interface with Glorious devices',
    'long_description': "# Glorious\nA [WIP] Python library to configure Glorious devices. A lot of the code comes from [this](https://github.com/korkje/mow) project, but I'm working on expanding it and adding more functionality.\n\n## Usage\nClone the repository: `git clone https://github.com/kbidlack/gloriously.git`\n\nMove into the project directory: `cd gloriously`\n\nInstall the requirements: `python -m pip install -Ur requirements.txt`\n\nRun the script: `python main.py`\n",
    'author': 'ksbidlack',
    'author_email': 'ksbidlack@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
