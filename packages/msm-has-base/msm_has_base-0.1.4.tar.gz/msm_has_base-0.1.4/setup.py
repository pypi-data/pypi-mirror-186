# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['msm_has_base']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'msm-has-base',
    'version': '0.1.4',
    'description': 'Hardware Access Services Base Foundation',
    'long_description': '',
    'author': '袁首京',
    'author_email': 'yuanshoujing@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.13,<4.0.0',
}


setup(**setup_kwargs)
