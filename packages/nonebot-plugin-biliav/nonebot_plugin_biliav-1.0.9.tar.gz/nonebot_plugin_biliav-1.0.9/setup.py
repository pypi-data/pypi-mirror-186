# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_biliav']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.18.0,<1.0.0',
 'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
 'nonebot2>=2.0.0-beta.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-biliav',
    'version': '1.0.9',
    'description': 'NoneBot biliav小程序 查看插件',
    'long_description': 'None',
    'author': 'knva',
    'author_email': 'txt_ch@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.9,<4.0.0',
}


setup(**setup_kwargs)
