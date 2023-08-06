# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['lcacollect_config', 'lcacollect_config.graphql']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy[asyncio]==1.4.35',
 'aiocache',
 'asyncpg>=0.26.0,<0.27.0',
 'fastapi-azure-auth',
 'pydantic',
 'sqlmodel>=0.0.8',
 'strawberry-graphql[fastapi]>=0.126.0']

setup_kwargs = {
    'name': 'lcacollect-config',
    'version': '1.0.0',
    'description': 'This package contains shared config and utils to be used across LCAcollect backends.',
    'long_description': 'None',
    'author': 'Christian Kongsgaard',
    'author_email': 'chrk@arkitema.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lcacollect/shared-config-backend',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
