# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebridge']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-antelegram>=0.2.0-dev10,<0.3.0',
 'nonebot-adapter-onebot>=2.2.0,<3.0.0',
 'nonebot2>=2.0.0rc2,<3.0.0']

setup_kwargs = {
    'name': 'nonebridge',
    'version': '0.1.4',
    'description': 'A adapter event bridge for nonebot2 makes plugins run on different adapters without any modify',
    'long_description': '# nonebridge\nA adapter event bridge for nonebot2 makes plugins running on different adapters without any modify   \n一个让你能够在不修改插件的情况下使其运行在不同adapter中的魔法bridge，开发目的是为了给[Yuki Clanbattle](https://github.com/ColdThunder11/yuki_clanbattle)提供Telegram支持\n## 还在开发中请勿生产环境使用\n女生自用插件，目前仅支持让为onebotv11编写的插件运行在自己写的[nonebot-adapter-telegram](https://github.com/ColdThunder11/nonebot-adapter-telegram)上，仅会支持有限的消息类型和API模拟   \n目前不支持~~主动发送消息和~~向非事件触发的聊天发送消息，支持主动向群聊使用send_group_msg发送群组消息了(必须在tg端收到任意消息后虚假的obv11 bot连接才会被注册)\n## 支持的接收类型\n- [x] 纯文字(MessageSegment.text)\n- [x] 图片(MessageSegment.image)\n\n## 支持的发送类型\n- [x] 文字(MessageSegment.text)\n- [x] 图片(MessageSegment.image)\n- [x] AT(MessageSegment.at)\n- [x] 语音(MessageSegment.record)\n\n## 支持的额外API\n| Onebot v11 API        | 对应的Telegarm API                                                       |\n| --------------------- | ------------------------------------------------------------------------ |\n| get_group_info        | getChat和getChatMemberCount                                              |\n| get_group_member_list | getChatAdministrators(由于tg并没有提供相关API，仅能够直接获取管理员信息) |\n| get_group_member_info | getChatMember                                                            |\n| send_group_msg        | ---                                                                      |\n## 配置\nnonebridge所需的配置直接写入到nonebot2的.env文件内即可\n```\nnonebridge_ob11_caption_ahead_photo: 将从telegram收到的带文字描述的图片消息中文字部分作为文字消息在ob11的消息段中前置以配合ob11中大部分插件的习惯写法，默认为True\nnonebridge_httpx_hook: 安装httpx钩子以拦截获取qq头像的http api，默认为False\n```\n\n## 使用方法\n同时安装并两个adapter，在bot.py紧随nonebot之后导入nonebridge，必须在任何adapter导入之前导入nonebridge，需要同时注册两个Adapter才能正常运行   \n### Example bot.py\n```python\nimport nonebot\nimport nonebridge\nfrom nonebot.adapters.onebot.v11 import Adapter as OneBot_V11_Adapter\nfrom nonebot.adapters.telegram.adapter import Adapter as Telegram_Adapter\n\nnonebot.init()\ndriver = nonebot.get_driver()\ndriver.register_adapter(OneBot_V11_Adapter)\ndriver.register_adapter(Telegram_Adapter)\nnonebot.load_plugin("your_onebotv11_plugin")\n\nif __name__ == "__main__":\n    nonebot.run()   \n```',
    'author': 'ColdThunder11',
    'author_email': 'lslyj27761@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ColdThunder11/nonebot-adapter-telegram',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
