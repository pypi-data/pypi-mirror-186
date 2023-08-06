# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_mc_server_status']

package_data = \
{'': ['*']}

install_requires = \
['mcstatus>=10.0.0,<11.0.0',
 'nonebot-adapter-onebot>=2.0.0,<3.0.0',
 'nonebot2>=2.0.0rc1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-mc-server-status',
    'version': '0.2.4',
    'description': 'Nonebot2查询MC服务器在线信息插件',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/store">\n  <img src="https://user-images.githubusercontent.com/44545625/209862575-acdc9feb-3c76-471d-ad89-cc78927e5875.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n</p>\n\n<div align="center">\n\n# nonebot_plugin_mc_server_status\n\n_✨ Nonebot2查询MC服务器在线信息插件 ✨_\n\n</div>\n\n<p align="center">\n  <a href="https://opensource.org/licenses/MIT">\n    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license">\n  </a>\n  <a href="https://v2.nonebot.dev/">\n    <img src="https://img.shields.io/static/v1?label=nonebot&message=v2rc1%2B&color=green" alt="nonebot2">\n  </a>\n  <img src="https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue" alt="python">\n</p>\n\n## 简介\n使用mcstatus库，支持Java和Bedrock服务器的服务器查询。   \n\n<img width="300" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_mc_server_status/readme_img/xinxi.jpg"/>\n\n## 安装\n\n使用nb-cli安装\n```bash\nnb plugin install nonebot_plugin_mc_server_status\n```\n\n或者  \n直接把插件clone下来放进去plugins文件夹，记得把依赖装上 pip install mcstatus  \n\n## 使用\n\n添加了服务器信息后，会在bot根目录下的data目录创建一个mc_status_data.json文件，用于存储插件信息  \n在bot对应的.env文件修改\n\n```bash\n# 管理员的QQ号（别问我为什么要另外写）\nmc_status_admin_qqnum = 114514\n\n# 可选配置\n# 机器人的QQ号列表，如果有多个bot连接，会按照填写的list，左边的机器人QQ优先级最高 1234 > 5678 > 6666，会自动切换\n# 如果不填该配置则由第一个连上的bot响应\ntutu_bot_qqnum_list = [\'1234\',\'5678\',\'6666\']\n```\n\n## 插件命令  \n| 指令 | 说明 |\n|:-----:|:----:|\n| 信息|所有人都能使用，查看当前群添加的服务器状态|\n| 添加服务器|字面意思，bot超级管理员用|\n| 删除服务器|字面意思，bot超级管理员用|\n| 信息数据|查看已添加的群和服务器信息，bot超级管理员用|\n\n## 更新日志\n### 2023/1/17 \\[v0.2.4]\n\n* 又忘记删东西导致无法运行\n\n### 2023/1/16 \\[v0.2.3]\n\n* 最低python版本兼容至3.8\n\n### 2023/1/15 \\[v0.2.2]\n\n* 优化多bot逻辑，机器人qq号配置改为可选\n\n### 2023/1/15 \\[v0.2.1]\n\n* 插件重构',
    'author': 'nikissXI',
    'author_email': '1299577815@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nikissXI/nonebot_plugins/tree/main/nonebot_plugin_mc_server_status',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
