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
    'version': '0.1.5',
    'description': '企业微信文档接口, 包括文档的创建, 删除, 以及表格的操作',
    'long_description': '# 企业微信文档接口\n\n## 案例\n\n```python\nfrom wedoc import WedocClient\n\n\nif __name__ =="__main__":\n    corpid = "xxxxxxxxxxxxx"\n    corpsecret = "xxxxxxxxxxxxx"\n\n    client = WedocClient(corpid, corpsecret)\n    res = client.get_crop_access_token()\n    client.doc.create_doc()\n\n```\n\n## 文档接口\n\n- 创建文档\n- 重命名文档\n- 删除文档\n- 获取文档基础信息\n\n## 表格接口\n\n- 获取表格行列信息\n- 获取表格数据\n- 编辑表格内容\n',
    'author': 'wn',
    'author_email': '320753691@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://wedoc.woni.link/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
