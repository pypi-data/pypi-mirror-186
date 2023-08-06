# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_easy_translate']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.22.0,<0.23.0',
 'nonebot-adapter-onebot>=2.0.0,<3.0.0',
 'nonebot2>=2.0.0rc1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-easy-translate',
    'version': '0.1.3',
    'description': 'Nonebot2 免api key简单翻译插件',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/store">\n  <img src="https://user-images.githubusercontent.com/44545625/209862575-acdc9feb-3c76-471d-ad89-cc78927e5875.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n</p>\n\n<div align="center">\n\n# nonebot_plugin_easy_translate\n\n_✨ Nonebot2 简单易用谷歌翻译插件，免key！ ✨_\n\n</div>\n<p align="center">\n  <a href="https://opensource.org/licenses/MIT">\n    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="license">\n  </a>\n  <a href="https://v2.nonebot.dev/">\n    <img src="https://img.shields.io/static/v1?label=nonebot&message=v2rc1%2B&color=green" alt="nonebot2">\n  </a>\n  <img src="https://img.shields.io/static/v1?label=python+&message=3.9%2B&color=blue" alt="python">\n</p>\n\n## 简介\n使用了sena-nana大佬给的接口，他的仓库\n<a href="https://github.com/sena-nana/nonebot-plugin-novelai/blob/main/nonebot_plugin_novelai/extension/translation.py">sena-nana/nonebot-plugin-novelai</a>，不需要使用梯子和api key就能使用的翻译插件\n\n<img width="500" src="https://raw.githubusercontent.com/nikissXI/nonebot_plugins/main/nonebot_plugin_easy_translate/readme_img/fanyi.jpg"/>\n\n## 安装\n\n使用nb-cli安装\n```bash\nnb plugin install nonebot_plugin_easy_translate\n```\n\n或者  \n直接把插件clone下来放进去plugins文件夹\n\n## 可选配置\n在bot对应的.env文件修改\n\n```bash\n# 机器人的QQ号列表，如果有多个bot连接，会按照填写的list，左边的机器人QQ优先级最高 1234 > 5678 > 6666，会自动切换\n# 如果不填该配置则由第一个连上的bot响应\neasy_translate_bot_qqnum_list = [\'1234\',\'5678\',\'6666\']\n```\n\n## 插件命令  \n| 指令 | 说明 |\n|:-----:|:----:|\n| 翻译 | 你发一下就知道啦 |\n\n## 更新日志\n### 2023/1/16 \\[v0.1.3]\n\n* 最低python版本兼容至3.8\n\n### 2023/1/15 \\[v0.1.2]\n\n* 发布插件',
    'author': 'nikissXI',
    'author_email': '1299577815@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nikissXI/nonebot_plugins/tree/main/nonebot_plugin_easy_translate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
