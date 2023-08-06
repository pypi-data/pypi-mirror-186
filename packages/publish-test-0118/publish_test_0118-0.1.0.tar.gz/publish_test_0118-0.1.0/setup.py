# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['publish_test_0118']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'publish-test-0118',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Xiaodong Yang',
    'author_email': 'xiaoyan@microsoft.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
