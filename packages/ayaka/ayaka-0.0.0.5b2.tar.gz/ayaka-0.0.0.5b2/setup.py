# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayaka', 'ayaka.adapters', 'ayaka.adapters.nonebot2']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'ayaka',
    'version': '0.0.0.5b2',
    'description': '猫猫，猫猫！',
    'long_description': '<div align="center">\n\n# Ayaka - 猫猫，猫猫！ - 0.0.0.5b2\n\n</div>\n\n根据py包的导入情况，猜测当前插件工作在哪个机器人框架下，已支持\n\n- [nonebot2](https://github.com/nonebot/nonebot2)(使用[onebotv11](https://github.com/nonebot/adapter-onebot)适配器)\n- [hoshino](https://github.com/Ice-Cirno/HoshinoBot)\n- [nonebot1](https://github.com/nonebot/nonebot)\n\n## 历史遗留问题\n\n如果你之前安装过`nonebot_plugin_ayaka`，请先确保它卸载干净\n\n```\npip uninstall nonebot_plugin_ayaka\n```\n\n## 安装\n\n```\npip install ayaka\n```\n\n## 配置\n\n### 必须满足的要求\n\n1. 已配置command_start、command_sep\n2. command_start、command_sep 均只有一项\n3. command_sep 不为空字符串\n\nayaka仅保证在此限制下正常工作\n\n### 推荐配置\n\n```\ncommand_start = [""]\ncommand_sep = [" "]\n```\n\n## 其他\n\n本插件的前身：[nonebot_plugin_ayaka](https://github.com/bridgeL/nonebot-plugin-ayaka)\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://bridgel.github.io/ayaka/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
