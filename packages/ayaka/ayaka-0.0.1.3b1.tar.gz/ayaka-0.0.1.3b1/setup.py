# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayaka', 'ayaka.adapters']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'pydantic>=1.10.0,<2.0.0', 'sqlmodel>=0.0.8,<0.0.9']

setup_kwargs = {
    'name': 'ayaka',
    'version': '0.0.1.3b1',
    'description': '猫猫，猫猫！',
    'long_description': '<div align="center">\n\n# Ayaka - 猫猫，猫猫！ - 0.0.1.3b1\n\n</div>\n\n根据py包的导入情况，猜测当前插件工作在哪个机器人框架下，已支持\n\n- [nonebot2](https://github.com/nonebot/nonebot2)(使用[onebotv11](https://github.com/nonebot/adapter-onebot)适配器)\n- [hoshino](https://github.com/Ice-Cirno/HoshinoBot)\n- [nonebot1](https://github.com/nonebot/nonebot)\n\n也可将其作为console程序离线运行\n\n## 文档\n\nhttps://bridgel.github.io/ayaka/\n\n## 历史遗留问题\n\n如果你之前安装过`nonebot_plugin_ayaka`，请先确保它卸载干净\n\n```\npip uninstall nonebot_plugin_ayaka\n```\n\n## 安装\n\n```\npip install ayaka\n```\n\n## 作为console程序离线运行\n\n```py\n# run.py\nimport ayaka.adapters as cat\n\n# 加载插件\n# do something\n\nif __name__ == "__main__":\n    cat.run()\n```\n\n```\npython run.py\n```\n\n## 其他\n\n本插件的前身：[nonebot_plugin_ayaka](https://github.com/bridgeL/nonebot-plugin-ayaka)\n',
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
