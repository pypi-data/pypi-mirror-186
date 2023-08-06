# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['systemy']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.2.0,<23.0.0',
 'py-expression-eval>=0.3.14,<0.4.0',
 'pydantic>=1.9.0,<2.0.0',
 'pyyaml>=6.0,<7.0']

setup_kwargs = {
    'name': 'systemy',
    'version': '0.1.2',
    'description': 'A core package to manipulate model or system hierarchical classes',
    'long_description': '',
    'author': 'Sylvain Guieu',
    'author_email': 'sylvain.guieu@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
