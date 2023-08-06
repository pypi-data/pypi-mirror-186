# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nonebot_plugin_mystool']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.1.1',
 'httpx>=0.22.0',
 'nonebot_adapter_onebot>=2.1.3',
 'nonebot_plugin_apscheduler>=0.2.0',
 'ntplib>=0.4.0,<0.5.0',
 'requests>=2.28.1,<3.0.0',
 'tenacity>=2.28.1']

setup_kwargs = {
    'name': 'nonebot-plugin-mystool',
    'version': '0.2.3',
    'description': 'NoneBot2插件|米游社工具-每日米游币任务、游戏签到、商品兑换、免抓包登录、原神树脂提醒',
    'long_description': '```\n __    __     __  __     ______     ______   ______     ______     __\n/\\ "-./  \\   /\\ \\_\\ \\   /\\  ___\\   /\\__  _\\ /\\  __ \\   /\\  __ \\   /\\ \\\n\\ \\ \\-./\\ \\  \\ \\____ \\  \\ \\___  \\  \\/_/\\ \\/ \\ \\ \\/\\ \\  \\ \\ \\/\\ \\  \\ \\ \\____\n \\ \\_\\ \\ \\_\\  \\/\\_____\\  \\/\\_____\\    \\ \\_\\  \\ \\_____\\  \\ \\_____\\  \\ \\_____\\\n  \\/_/  \\/_/   \\/_____/   \\/_____/     \\/_/   \\/_____/   \\/_____/   \\/_____/\n```\n\n<div>\n  <a href="https://www.codefactor.io/repository/github/ljzd-pro/nonebot-plugin-mystool" target="_blank">\n    <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/ljzd-pro/nonebot-plugin-mystool/badge?style=for-the-badge">\n  </a>\n  <a href="https://github.com/Ljzd-PRO/nonebot-plugin-mystool/releases/latest" target="_blank">\n    <img alt="最新发行版" src="https://img.shields.io/github/v/release/Ljzd-PRO/nonebot-plugin-mysTool?logo=python&style=for-the-badge">\n  </a>\n  <a href="https://github.com/Ljzd-PRO/nonebot-plugin-mystool/commits/" target="_blank">\n    <img alt="最后提交" src="https://img.shields.io/github/last-commit/Ljzd-PRO/nonebot-plugin-mysTool?style=for-the-badge">\n  </a>\n</div>\n\n# mysTool - 米游社辅助工具插件\n\n**版本 - v0.2.3**\n\n### 📣 更新内容\n#### 2023.1.17\n- 修复群聊中手动签到不会模糊处理手机号的问题\n- 配置中可控制加好友是否发送欢迎以及使用指引信息\n\n#### 2022.12.24\n- 支持群聊使用\n\n#### 2022.12.23\n- 新增原神树脂、洞天宝钱、质量参变仪状态查看和提醒等功能。\n\n## 功能和特性\n\n- 短信验证登录，免抓包获取 Cookie\n- 自动完成每日米游币任务\n- 自动进行游戏签到\n- 可制定米游币商品兑换计划，到点兑换\n- 可支持多个 QQ 账号，每个 QQ 账号可绑定多个米哈游账户\n- QQ 推送执行结果通知\n- 原神树脂、洞天宝钱、质量参变仪已满时推送通知\n\n## 使用说明\n\n### 🛠️ NoneBot2 机器人部署和插件安装\n\n请查看 -> [🔗Installation](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Installation)\n\n### 📖 插件具体使用说明\n\n请查看 -> [🔗Wiki 文档](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki)\n\n### ❓ 获取插件帮助信息\n\n#### 插件命令\n\n```\n/帮助\n```\n\n> ⚠️ 注意 此处没有使用 [🔗 插件命令头](https://github.com/Ljzd-PRO/nonebot-plugin-mystool/wiki/Configuration-Config#command_start)\n\n## 其他\n### 适配 [绪山真寻Bot](https://github.com/HibiKier/zhenxun_bot) 的分支\n- https://github.com/MWTJC/zhenxun-plugin-mystool\n- https://github.com/ayakasuki/nonebot-plugin-mystool\n',
    'author': 'Ljzd-PRO',
    'author_email': 'ljzd@office.ljzd-pro.ml',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Ljzd-PRO/nonebot-plugin-mystool',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
