# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_picstatus']

package_data = \
{'': ['*'], 'nonebot_plugin_picstatus': ['res/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'aiofiles>=22.1.0,<23.0.0',
 'aiohttp>=3.8.3,<4.0.0',
 'nonebot-adapter-onebot>=2.1.0',
 'nonebot2>=2.0.0b4',
 'psutil>=5.9.2,<6.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-picstatus',
    'version': '0.3.2',
    'description': 'A NoneBot2 plugin generates a picture which shows the status of current device',
    'long_description': '<!-- markdownlint-disable MD033 MD036 MD041 -->\n\n<div align="center">\n  <a href="https://v2.nonebot.dev/store">\n    <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/nbp_logo.png" width="180" height="180" alt="logo">\n  </a>\n  <br>\n  <p>\n    <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/NoneBotPlugin.svg" width="240" alt="logo">\n  </p>\n</div>\n\n<div align="center">\n\n# NoneBot-Plugin-PicStatus\n\n_✨ 运行状态图片版 for NoneBot2 ✨_\n\n<a href="./LICENSE">\n  <img src="https://img.shields.io/github/license/lgc2333/nonebot-plugin-picstatus.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot-plugin-picstatus">\n  <img src="https://img.shields.io/pypi/v/nonebot-plugin-picstatus.svg" alt="pypi">\n</a>\n<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n<a href="https://pypi.python.org/pypi/nonebot-plugin-picstatus">\n  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-picstatus" alt="pypi download">\n</a>\n<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/bfec6993-aa9e-42fb-9f3e-53a5d4739373">\n  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/bfec6993-aa9e-42fb-9f3e-53a5d4739373.svg" alt="wakatime">\n</a>\n\n</div>\n\n## 📖 介绍\n\n不多说，直接看图！\n\n### 效果图\n\n<details>\n  <summary>点击展开</summary>\n\n![example](https://raw.githubusercontent.com/lgc2333/nonebot-plugin-picstatus/master/readme/example.png)\n\n</details>\n\n## 💿 安装\n\n<details open>\n<summary>[推荐] 使用 nb-cli 安装</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n\n    nb plugin install nonebot-plugin-picstatus\n\n</details>\n\n<details>\n<summary>使用包管理器安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令\n\n<details>\n<summary>pip</summary>\n\n    pip install nonebot-plugin-picstatus\n\n</details>\n<details>\n<summary>pdm</summary>\n\n    pdm add nonebot-plugin-picstatus\n\n</details>\n<details>\n<summary>poetry</summary>\n\n    poetry add nonebot-plugin-picstatus\n\n</details>\n<details>\n<summary>conda</summary>\n\n    conda install nonebot-plugin-picstatus\n\n</details>\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n    nonebot.load_plugin(\'nonebot_plugin_picstatus\')\n\n</details>\n\n<details>\n<summary>从 github 安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 输入以下命令克隆此储存库\n\n    git clone https://github.com/lgc2333/nonebot-plugin-picstatus.git\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n    nonebot.load_plugin(\'src.plugins.nonebot_plugin_picstatus\')\n\n</details>\n\n## ⚙️ 配置\n\n见[.env.example](https://github.com/lgc2333/nonebot-plugin-picstatus/blob/master/.env.example)\n\n## 🎉 使用\n\n使用指令`运行状态`（或者`状态` / `zt` / `yxzt` / `status`）来触发插件功能  \n可以在消息后面跟一张图片或者回复一张图片来自定义背景图，默认为随机背景图  \n更多自定义项参见 [配置](#️-配置)\n\n## 📞 联系\n\nQQ：3076823485  \nTelegram：[@lgc2333](https://t.me/lgc2333)  \n吹水群：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  \n邮箱：<lgc2333@126.com>\n\n## 💡 鸣谢\n\n### [故梦 API](https://api.gmit.vip)\n\n- 随机背景图来源\n\n## 💰 赞助\n\n感谢大家的赞助！你们的赞助将是我继续创作的动力！\n\n- [爱发电](https://afdian.net/@lgc2333)\n- <details>\n    <summary>赞助二维码（点击展开）</summary>\n\n  ![讨饭](https://raw.githubusercontent.com/lgc2333/ShigureBotMenu/master/src/imgs/sponsor.png)\n\n  </details>\n\n## 📝 更新日志\n\n### 0.3.2\n\n- 只有当 `nickname` 配置项填写后，插件才会使用该项作为图片中 Bot 的显示名称\n\n### 0.3.1\n\n- 修复一处 Py 3.10 以下无法正常运行的代码\n\n### 0.3.0\n\n配置项更新详见 [配置](#️-配置)\n\n- 更新配置项 `PS_TEST_SITES` `PS_TEST_TIMEOUT`\n- 修复`PS_NEED_AT`配置无效的 bug\n- 现在只有命令完全匹配时才会触发\n\n### 0.2.5\n\n- 更新配置项 `PS_FOOTER_SIZE`\n\n### 0.2.4\n\n- 支持自定义默认背景图\n- 一些配置项类型更改（不影响原先配置）\n\n### 0.2.3\n\n- 尝试修复磁盘列表的潜在 bug\n\n### 0.2.2\n\n此版本在图片脚注中显示的版本还是`0.2.1`，抱歉，我大意了没有改版本号\n\n- 添加配置项`PS_IGNORE_NO_IO_DISK`用于忽略 IO 为 0B/s 的磁盘\n- 添加配置项`PS_IGNORE_0B_NET`用于忽略上下行都为 0B/s 的网卡\n- 添加触发指令`zt` `yxzt` `status`\n- 获取信息收发量兼容旧版 GoCQ ，即使获取失败也不会报错而显示`未知`\n- 将忽略 IO 统计磁盘名独立出一个配置项`PS_IGNORE_DISK_IOS`\n- 忽略 磁盘容量盘符/IO 统计磁盘名/网卡名称 改为匹配正则表达式\n- 配置项`PS_IGNORE_NETS`添加默认值`["^lo$", "^Loopback"]`\n- 修复空闲内存显示错误的问题\n\n### 0.2.1\n\n- 尝试修复`type object is not subscriptable`报错\n\n### 0.2.0\n\n- 新增磁盘 IO、网络 IO 状态显示\n- SWAP 大小为 0 时占用率将会显示`未部署`而不是`0%`\n- CPU 等占用下方灰色字排板更改\n- 获取失败的磁盘分区占用率修改为`未知%`\n- 图片下方脚注修改为居中文本，字号调小，优化显示的系统信息\n- 修改随机背景图 API 为[故梦 API 随机二次元壁纸](https://api.gmit.vip)\n- 现在会分 QQ 记录 Bot 连接时间（不同的 QQ 连接同一个 NoneBot 显示的连接时间将不同）\n- 背景图增加遮罩，颜色可配置\n- 可以配置各模块的背景底色\n- 可以配置分区列表中忽略的盘符（挂载点）\n- 可以忽略获取容量状态失败的分区\n- 可以使用`.env.*`文件中配置的`NICKNAME`作为图片中的 Bot 昵称\n- 添加必须 @Bot 才能触发指令的配置\n- 其他小优化/更改\n',
    'author': 'student_2333',
    'author_email': 'lgc2333@126.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
