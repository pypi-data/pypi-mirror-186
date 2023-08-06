# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_nya_cook_menu']

package_data = \
{'': ['*'], 'nonebot_plugin_nya_cook_menu': ['font/*']}

install_requires = \
['Pillow>=9.0.0,<10.0.0',
 'nonebot-adapter-onebot>=2.0.0,<3.0.0',
 'nonebot2>=2.0.0rc1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-nya-cook-menu',
    'version': '0.1.2',
    'description': 'Nonebot2 喵喵自记菜谱，记录生活中的小菜谱',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/store">\n  <img src="https://user-images.githubusercontent.com/44545625/209862575-acdc9feb-3c76-471d-ad89-cc78927e5875.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n</p>\n\n<div align="center">\n\n# nonebot_plugin_nya_cook_menu\n\n_✨ Nonebot2 喵喵自记菜谱 ✨_\n\n</div>\n<p align="center">\n  <a href="https://opensource.org/licenses/MIT">\n    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license">\n  </a>\n  <a href="https://v2.nonebot.dev/">\n    <img src="https://img.shields.io/static/v1?label=nonebot&message=v2rc1%2B&color=green" alt="nonebot2">\n  </a>\n  <img src="https://img.shields.io/static/v1?label=python+&message=3.9%2B&color=blue" alt="python">\n</p>\n\n## 简介\n我和老婆经常做菜忘记以前某个菜咋做，于是就整了这个插件记录一下我们的菜谱，顺便发到商店，嘿嘿~  \n<img width="500" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_nya_cook_menu/readme_img/caipu.jpg"/>\n\n## 安装\n\n使用nb-cli安装\n```bash\nnb plugin install nonebot_plugin_nya_cook_menu\n```\n\n或者  \n直接把插件clone下来放进去plugins文件夹\n\n## 配置\n在bot对应的.env文件修改\n\n```bash\n# 使用用户qq号，必填\nnya_cook_user_list: list[int] = [1234, 5678]\n# 机器人的QQ号列表，选填\n# 如果有多个bot连接，会按照填写的list，左边的机器人QQ优先级最高 1234 > 5678 > 6666，会自动切换\n# 如果不填该配置则由第一个连上的bot响应\nnya_cook_bot_qqnum_list = [\'1234\',\'5678\',\'6666\']\n```\n\n## 插件命令  \n| 指令 | 说明 |\n|:-----:|:----:|\n| 菜谱 | 你发一下就知道啦 |\n\n## 更新日志\n### 2023/1/16 \\[v0.1.2]\n\n* 最低python版本兼容至3.8\n\n### 2023/1/16 \\[v0.1.1]\n\n* 发布插件',
    'author': 'nikissXI',
    'author_email': '1299577815@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nikissXI/nonebot_plugins/tree/main/nonebot_plugin_nya_cook_menu',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
