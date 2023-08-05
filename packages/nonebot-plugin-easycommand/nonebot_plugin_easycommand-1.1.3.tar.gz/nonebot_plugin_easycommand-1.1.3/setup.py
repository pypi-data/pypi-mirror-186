# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_easyCommand']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.0.0-beta.1',
 'nonebot2>=2.0.0-beta.1',
 'nonebot_plugin_apscheduler',
 'nonebot_plugin_txt2img']

setup_kwargs = {
    'name': 'nonebot-plugin-easycommand',
    'version': '1.1.3',
    'description': '一款基于NoneBot2的简单的用来扩充命令或添加定时任务的插件。',
    'long_description': '# nonebot_plugin_easyCommand\n 一个基于NoneBot2的简单的用来扩充命令或添加定时任务的插件\n\n一、概述\n\n1.起始符+"添加命令 标题 内容","删除命令 标题","查看命令","允许命令","结束命令"，"获取CQ"分达到如其字意的效果\n\n2.添加命令后当接收到命令后会自动匹配命令\n\n3."允许命令","结束命令"默认不开放群无起始符命令白名单，且不存录，为超级管理员游戏做\n\n4.群聊@、白名单、第一个字符为命令起始符且全部匹配(避免响应其他未加锁插件) 匹配回复，私聊不加起始符匹配回复或加且全部匹配\n\n5.起始符+"注册定时 时间 标题 内容" "删除定时 标题"\n\n\n二、详解\n\n1.添加命令 标题 内容 内容支持图像、表情、转发、文本\n\n2.删除命令 标题 不支持图像类型的标题 第一顺位超管输入"#+-*/真的啦已经确认过啦"删除所有命令\n\n3.查看命令 超管输入命令"查看命令全"查看所有命令、普通用户查看自己写的命令，最长皆为前3-400字符长度  如想要都可以全查自行删除约136行处 and uid in superList\n\n4.允许命令 群聊添加当前群聊或私聊添加当前私聊者到无需前缀命令起始符响应白名单 权限为超管 可自行修改代码剥离允许权限列表为群管可添加\n\n5.结束命令 同上\n\n6.获取CQ 当前聊天者可获取一次返回CQ码的机会，下次消息触发\n\n7.注册定时 时间 标题 内容 时间格式为时.分.秒 遵循corn规则，但表达式仅限于d */d d-d * ，其中d指时间实例如9、*/2、10-59、* \n内容支持同上支持CQ，都不支持视频CQ \n\n8.删除定时 标题\n\n三、致谢\n\n感谢NoneBot、nonebot_plugin_apscheduler、nonebot_plugin_txt2img及其开发者\n',
    'author': 'ziru-w',
    'author_email': '77319678+ziru-w@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
