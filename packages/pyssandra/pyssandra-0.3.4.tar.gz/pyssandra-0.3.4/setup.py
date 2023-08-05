# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyssandra']

package_data = \
{'': ['*']}

install_requires = \
['case-switcher>=1.3.4,<2.0.0',
 'cassandra-driver>=3.25.0,<4.0.0',
 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'pyssandra',
    'version': '0.3.4',
    'description': 'Use pydantic models to create basic CQL queries.',
    'long_description': None,
    'author': 'Matthew Burkard',
    'author_email': 'matthewjburkard@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
