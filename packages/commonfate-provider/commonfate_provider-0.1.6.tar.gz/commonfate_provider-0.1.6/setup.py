# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['commonfate_provider',
 'commonfate_provider.runtime',
 'commonfate_provider.runtime.tests']

package_data = \
{'': ['*']}

install_requires = \
['click==8.1.3',
 'pydantic==1.10.2',
 'pytest==7.2.0',
 'toml==0.10.2',
 'treelib==1.6.1',
 'typing-extensions==4.4.0']

setup_kwargs = {
    'name': 'commonfate-provider',
    'version': '0.1.6',
    'description': 'This is the core Provider framework on top of which Access Provider are written.',
    'long_description': '# commonfate-provider-core\nCommonfate Provider Core Python Package\n',
    'author': 'Chris Norman',
    'author_email': 'chris@commonfate.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
