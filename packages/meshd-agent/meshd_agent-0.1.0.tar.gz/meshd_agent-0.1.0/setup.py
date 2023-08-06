# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meshd_agent']

package_data = \
{'': ['*']}

install_requires = \
['fastapi-websocket-pubsub>=0.3.1,<0.4.0',
 'pandas>=1.5.2,<2.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'requests>=2.28.2,<3.0.0',
 'sqlalchemy==1.4.41']

setup_kwargs = {
    'name': 'meshd-agent',
    'version': '0.1.0',
    'description': 'The open source part of the Meshd Cloud.Remove the need to directly connect to your sources via the API and connect with this agent instead. https://meshd.cloud',
    'long_description': '# The Meshd Cloud Agent\nhttps://meshd.cloud\n',
    'author': 'Toby Devlin',
    'author_email': 'hello@meshd.cloud',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
