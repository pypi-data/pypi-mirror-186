# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wedoc', 'wedoc.api']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'wedoc',
    'version': '0.1.2',
    'description': '',
    'long_description': '# 企业微信文档接口\n\n## 应用\n\n## 文档接口\n\n## 表格接口\n',
    'author': 'wn',
    'author_email': '320753691@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
