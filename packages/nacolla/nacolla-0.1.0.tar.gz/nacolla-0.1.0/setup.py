# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nacolla', 'nacolla.operations', 'nacolla.parsing', 'nacolla.utilities']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'typing-extensions>=4.3.0,<5.0.0']

setup_kwargs = {
    'name': 'nacolla',
    'version': '0.1.0',
    'description': 'Type validated flows in Python',
    'long_description': 'None',
    'author': 'DPaletti',
    'author_email': 'danielepaletti98@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
