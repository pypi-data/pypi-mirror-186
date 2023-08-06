# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetrytest_yxd_1020', 'poetrytest_yxd_1020.world']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'poetrytest-yxd-1020',
    'version': '0.1.2',
    'description': '',
    'long_description': '',
    'author': 'Xiaodong Yang',
    'author_email': 'xiaoyan@microsoft.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
