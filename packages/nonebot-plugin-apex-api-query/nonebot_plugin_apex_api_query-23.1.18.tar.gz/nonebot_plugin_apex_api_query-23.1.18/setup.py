# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_apex_api_query']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'nonebot-adapter-onebot>=2.2.0,<3.0.0',
 'nonebot-plugin-apscheduler>=0.2.0,<0.3.0',
 'nonebot-plugin-txt2img>=0.2.1,<0.3.0',
 'nonebot2>=2.0.0rc2,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-apex-api-query',
    'version': '23.1.18',
    'description': '基于 NoneBot2 的 Apex Legends API 查询插件',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# nonebot-plugin-apex-api-query\n\n*✨ NoneBot Apex Legends API 查询插件 ✨*\n\n![GitHub](https://img.shields.io/github/license/H-xiaoH/nonebot-plugin-apex-api-query)\n![PyPI](https://img.shields.io/pypi/v/nonebot-plugin-apex-api-query)\n\n</div>\n\n## 配置项\n\n您可以在 [NoneBot2 官方文档](https://v2.nonebot.dev/docs/tutorial/configuration) 中查看配置文件的配置方法。\n\n例如:\n```text\nHOST=127.0.0.1\nPORT=8080\nLOG_LEVEL=DEBUG\nFASTAPI_RELOAD=true\nNICKNAME=["Bot"]\nCOMMAND_START=["/", ""]\nCOMMAND_SEP=["."]\nAPEX_API_KEY=\'173fd0ee53fb32d4c7063eb5bc700c9e\'\n```\n\n### APEX_API_KEY\n\n您的 32 位 API 密钥。\n\n`APEX_API_KEY=\'173fd0ee53fb32d4c7063eb5bc700c9e\'`\n\n### APEX_API_T2I\n\n文字转图片发送内容\n\n- `True` = 开启 (默认)\n- `False` = 关闭\n\n## Application Programming Interface\n\n您可以在 [此处](https://portal.apexlegendsapi.com/) 申请您自己的 API 密钥。\n申请密钥后重新在 [此页面](https://portal.apexlegendsapi.com/) 登录 API 密钥以测试密钥是否可用。\n必须将此 API 密钥 [链接](https://portal.apexlegendsapi.com/discord-auth) 至您的 Discord 账户后您的 API 密钥才可用。\n\n由于 API 的问题，您只能在查询玩家信息时使用 EA 账户用户名并非 Steam 账户用户名。\n\n## 使用方式\n\n`/bridge [玩家名称]` 、`/玩家 [玩家名称]` - 根据玩家名称查询玩家信息 (暂仅支持查询 PC 平台玩家信息)\n\n`/uid [玩家UID]`、`/UID [玩家UID]` - 根据玩家 UID 查询玩家信息 (暂仅支持查询 PC 平台玩家信息)\n\n`/maprotation` 、 `/地图` - 查询当前地图轮换\n\n`/predator` 、 `/猎杀` - 查询顶尖猎杀者信息\n\n`/crafting` 、 `/制造` - 查询当前制造轮换\n\n`/servers`、`/服务` - 查看当前服务器状态\n\n`/submap`、`/订阅地图` - 订阅地图轮换(每整点查询)(仅群聊可用)\n\n`/unsubmap`、`/取消订阅地图` - 取消订阅地图轮换(仅群聊可用)\n\n`/subcraft`、`/订阅制造` - 订阅制造轮换(每日2时查询)(仅群聊可用)\n\n`/unsubcraft`、`/取消订阅制造` - 取消订阅制造轮换(仅群聊可用)\n\n',
    'author': 'HxiaoH',
    'author_email': '412454922@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/H-xiaoH/nonebot-plugin-apex-api-query',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
