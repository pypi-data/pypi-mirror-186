# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bigledger_sdk']

package_data = \
{'': ['*']}

install_requires = \
['twine>=4.0.2,<5.0.0']

entry_points = \
{'console_scripts': ['twin = twin:main']}

setup_kwargs = {
    'name': 'bigledger-sdk',
    'version': '0.1.0',
    'description': 'PythonBot Twin Framework',
    'long_description': '# Twin Framework\n\nThis is a simple example package. You can use\n[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)\nto write your content.',
    'author': 'Vincent Lee',
    'author_email': 'vincent@akaun.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://bigledger.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
