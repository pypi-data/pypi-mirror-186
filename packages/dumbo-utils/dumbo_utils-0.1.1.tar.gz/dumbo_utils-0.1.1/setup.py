# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dumbo_utils']

package_data = \
{'': ['*']}

install_requires = \
['rich>=13.0.1,<14.0.0',
 'typeguard>=2.13.3,<3.0.0',
 'typer>=0.7.0,<0.8.0',
 'valid8>=5.1.2,<6.0.0']

setup_kwargs = {
    'name': 'dumbo-utils',
    'version': '0.1.1',
    'description': 'Different utilities to be reused in other projects',
    'long_description': '# dumbo-utils\nDifferent utilities to be reused in other projects\n',
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
