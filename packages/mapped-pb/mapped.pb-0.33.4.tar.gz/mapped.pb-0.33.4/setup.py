# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['mapped_pb', 'mapped_pb.cloud', 'mapped_pb.cloud.types', 'mapped_pb.gateway']

package_data = \
{'': ['*']}

install_requires = \
['betterproto==2.0.0b5', 'grpclib==0.4.3']

setup_kwargs = {
    'name': 'mapped.pb',
    'version': '0.33.4',
    'description': 'public Mapped Platform Service Definitions using protobuf',
    'long_description': '# Mapped Public Proto Package for Python\n',
    'author': 'Mapped',
    'author_email': 'support@mapped.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.mapped.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
