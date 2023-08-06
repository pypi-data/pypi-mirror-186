# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['croc']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pycroc',
    'version': '0.0.1',
    'description': 'An integration testing framework written in Python :)',
    'long_description': '# pycroc\n\n`pycroc` makes integration testing easy and accessible, as it is very easy to use in new or existing projects!\n\nIt allows to test real applications, whether they are APIs, web pages or anything that you can test really.\n\n# Roadmap\n\nCurrently there is no implementation of the package, this is a placeholder for the project.\n',
    'author': 'Vitaman02',
    'author_email': 'filip1253@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
