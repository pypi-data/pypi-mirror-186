# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['web_proxy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'web-proxy',
    'version': '0.1.0',
    'description': 'Use web proxy website to proxy http clients such as urllib or requests',
    'long_description': 'Use web proxy website to proxy http clients such as urllib or requests',
    'author': 'zyg',
    'author_email': 'jawide@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
