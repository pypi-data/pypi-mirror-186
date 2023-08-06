# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src', 'yamls': 'src/yamls'}

packages = \
['akira', 'yamls']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['my_package_cli = akira.teste:return_ola_mundo_string']}

setup_kwargs = {
    'name': 'akira',
    'version': '0.1.6',
    'description': 'A short description of the package.',
    'long_description': '# library_publish_test',
    'author': 'Bruno-Felix',
    'author_email': 'auxbfelix@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/PDA-FGA/Playground',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
