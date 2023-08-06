# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rekuest',
 'rekuest.actors',
 'rekuest.actors.reactive',
 'rekuest.agents',
 'rekuest.agents.transport',
 'rekuest.agents.transport.protocols',
 'rekuest.api',
 'rekuest.contrib.fakts',
 'rekuest.definition',
 'rekuest.postmans',
 'rekuest.postmans.transport',
 'rekuest.postmans.transport.protocols',
 'rekuest.qt',
 'rekuest.structures',
 'rekuest.structures.serialization',
 'rekuest.traits']

package_data = \
{'': ['*']}

install_requires = \
['annotated-types>=0.4.0,<0.5.0',
 'docstring-parser>=0.11',
 'inflection>=0.5.1,<0.6.0',
 'koil>=0.2.10',
 'pydantic>=1.9.0',
 'pytest-aiohttp>=1.0.4,<2.0.0',
 'pytest-asyncio>=0.20.2,<0.21.0',
 'rath>=0.3.4',
 'websockets>=10.0,<11.0']

setup_kwargs = {
    'name': 'rekuest',
    'version': '0.1.16',
    'description': 'rpc and node backbone',
    'long_description': 'None',
    'author': 'jhnnsrs',
    'author_email': 'jhnnsrs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
