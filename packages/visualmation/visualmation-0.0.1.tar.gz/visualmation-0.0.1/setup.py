# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['visualmation']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'visualmation',
    'version': '0.0.1',
    'description': 'computer graphics animation engine',
    'long_description': '# kamilu\n\n计算机绘图，动画引擎\n\n## 安装\n\n```bash\npip install kamilu\n```\n\n## 支持\n\n- [ ] 添加文字转语音\n\n## 使用方法\n\n见[使用文档](https://luzhixing12345.github.io/kamilu/)\n',
    'author': 'luzhixing12345',
    'author_email': 'luzhixing12345@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/luzhixing12345/visualmation',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
