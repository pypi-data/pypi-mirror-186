# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_chatrecorder', 'nonebot_plugin_chatrecorder.migrations']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.2.0,<3.0.0',
 'nonebot-plugin-datastore>=0.5.1,<0.6.0',
 'nonebot2>=2.0.0-rc.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-chatrecorder',
    'version': '0.2.0',
    'description': '适用于 Nonebot2 的聊天记录插件',
    'long_description': '## nonebot-plugin-chatrecorder\n\n适用于 [Nonebot2](https://github.com/nonebot/nonebot2) 的聊天记录插件。\n\n将聊天消息存至数据库中，方便其他插件使用。\n\n### 安装\n\n- 使用 nb-cli\n\n```shell\nnb plugin install nonebot_plugin_chatrecorder\n```\n\n- 使用 pip\n\n```shell\npip install nonebot_plugin_chatrecorder\n```\n\n### 配置项\n\n> 以下配置项可在 `.env.*` 文件中设置，具体参考 [NoneBot 配置方式](https://v2.nonebot.dev/docs/tutorial/configuration#%E9%85%8D%E7%BD%AE%E6%96%B9%E5%BC%8F)\n\n#### `chatrecorder_record_send_msg`\n - 类型：`bool`\n - 默认：`True`\n - 说明：是否记录机器人自己发出的消息\n\n#### `chatrecorder_record_migration_bot_id`\n - 类型：`Optional[str]`\n - 默认：`None`\n - 说明：在旧版本(0.1.x) 时使用的机器人账号(机器人qq号)，用于数据库迁移；若使用过此插件的旧版本则必须配置，数据库迁移完成后可删除；未使用过旧版本可不配置\n\n\n### 其他说明\n\n插件依赖 [nonebot-plugin-datastore](https://github.com/he0119/nonebot-plugin-datastore) 插件来提供数据库支持\n\n`nonebot-plugin-datastore` 插件默认使用 SQLite 数据库，\n消息记录文件会存放在 `nonebot-plugin-datastore` 插件设置的数据目录\n\n由于在 OneBot V11 适配器中，机器人发送的消息中可能存在 base64 形式的图片、语音等，\n为避免消息记录文件体积过大，本插件会将 base64 形式的图片、语音等存成文件，并在消息记录中以文件路径替代。\n这些文件会放置在 `nonebot-plugin-datastore` 插件设置的缓存目录，建议定期清理\n\n\n### 使用\n\n其他插件可使用本插件提供的接口获取消息记录\n\n先在插件代码最前面声明依赖：\n```python\nfrom nonebot import require\nrequire("nonebot_plugin_chatrecorder")\n```\n\n使用示例：\n\n - 获取当前群内成员 "12345" 和 "54321" 1天之内的消息记录\n\n```python\nfrom nonebot.adapters.onebot.v11 import GroupMessageEvent\nfrom nonebot_plugin_chatrecorder import get_message_records\n\n@matcher.handle()\nasync def _(event: GroupMessageEvent):\n    records = await get_message_records(\n        user_ids=["12345", "54321"],\n        group_ids=[str(event.group_id)],\n        time_start=datetime.utcnow() - timedelta(days=1),\n    )\n```\n\n - 获取所有 OneBot V11 适配器形式的消息\n\n```python\nfrom nonebot.adapters.onebot.v11 import Bot\nfrom nonebot_plugin_chatrecorder import get_messages\n\n@matcher.handle()\nasync def _(bot: Bot):\n    msgs = await get_messages(bot)\n```\n\n - 获取本群除机器人发出的消息外，其他消息的纯本文形式\n\n```python\nfrom nonebot.adapters.onebot.v11 import GroupMessageEvent\nfrom nonebot_plugin_chatrecorder import get_messages_plain_text\n\n@matcher.handle()\nasync def _(event: GroupMessageEvent):\n    msgs = await get_messages_plain_text(\n        types=["message"],\n        group_ids=[str(event.group_id)],\n    )\n```\n\n详细参数及说明见代码注释\n',
    'author': 'meetwq',
    'author_email': 'meetwq@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/noneplugin/nonebot-plugin-chatrecorder',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
