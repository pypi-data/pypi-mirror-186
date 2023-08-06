# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['websocket_rpcs_tool']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0', 'requests>=2.28.2,<3.0.0', 'wget>=3.2,<4.0']

entry_points = \
{'console_scripts': ['wrpc = websocket_rpcs_tool.__main__:__main__']}

setup_kwargs = {
    'name': 'websocket-rpcs-tool',
    'version': '0.1.0',
    'description': 'websocket rpc protobuf generate tool',
    'long_description': 'websocket rpc protobuf generate tool',
    'author': 'jawide',
    'author_email': 'jawide@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
