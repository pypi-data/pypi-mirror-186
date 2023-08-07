# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forgelogging']

package_data = \
{'': ['*']}

install_requires = \
['forge-core>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'forge-logging',
    'version': '1.0.0',
    'description': 'Logging for Forge',
    'long_description': '# forge-logging\n',
    'author': 'Dave Gaeddert',
    'author_email': 'dave.gaeddert@dropseed.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.forgepackages.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
