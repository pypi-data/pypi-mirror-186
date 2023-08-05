# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_datastore',
 'nonebot_plugin_datastore.script',
 'nonebot_plugin_datastore.script.migration']

package_data = \
{'': ['*']}

install_requires = \
['aiosqlite>=0.17.0,<0.18.0',
 'alembic>=1.9.1,<2.0.0',
 'nonebot-plugin-localstore>=0.2.0,<0.3.0',
 'nonebot2[httpx]>=2.0.0-rc.1,<3.0.0',
 'sqlmodel>=0.0.8,<0.1.0']

entry_points = \
{'nb_scripts': ['datastore = nonebot_plugin_datastore.script.cli:main']}

setup_kwargs = {
    'name': 'nonebot-plugin-datastore',
    'version': '0.5.0',
    'description': '适用于 Nonebot2 的数据存储插件',
    'long_description': '<!-- markdownlint-disable MD033 MD036 MD041 -->\n\n<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# NoneBot Plugin DataStore\n\n_✨ NoneBot 数据存储插件 ✨_\n\n</div>\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/he0119/nonebot-plugin-datastore/main/LICENSE">\n    <img src="https://img.shields.io/github/license/he0119/nonebot-plugin-datastore.svg" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-datastore">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-datastore.svg" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n  <a href="https://codecov.io/gh/he0119/nonebot-plugin-datastore">\n    <img src="https://codecov.io/gh/he0119/nonebot-plugin-datastore/branch/main/graph/badge.svg?token=jd5ufc1alv"/>\n  </a>\n</p>\n\n## 使用方式\n\n先在插件代码最前面声明依赖\n\n```python\nfrom nonebot import require\nrequire("nonebot_plugin_datastore")\n```\n\n插件数据相关功能\n\n```python\nfrom nonebot_plugin_datastore import get_plugin_data\n\nDATA = get_plugin_data()\n\n# 缓存目录\nDATA.cache_dir\n# 配置目录\nDATA.config_dir\n# 数据目录\nDATA.data_dir\n```\n\n数据库相关功能\n\n```python\nfrom nonebot.params import Depends\nfrom nonebot_plugin_datastore import get_plugin_data, get_session\nfrom sqlmodel.ext.asyncio.session import AsyncSession\n\n# 定义模型\nModel = get_plugin_data().Model\n\nclass Example(Model, table=True):\n    """示例模型"""\n\n    __table_args__ = {"extend_existing": True}\n\n    id: Optional[int] = Field(default=None, primary_key=True)\n    message: str\n\n# 数据库相关操作\n@matcher.handle()\ndef handle(session: AsyncSession = Depends(get_session)):\n    example = Example(message="matcher")\n    session.add(example)\n    await session.commit()\n\n# 因为 driver.on_startup 无法保证函数运行顺序\n# 如需在 NoneBot 启动时且数据库初始化后运行的函数\n# 请使用 post_db_init 而不是 Nonebot 的 on_startup\nfrom nonebot_plugin_datastore.db import post_db_init\n\n@post_db_init\nasync def do_something():\n  pass\n```\n\nCLI 功能（需要安装 nb-cli）\n\n```shell\n# 自动生成迁移文件\nnb datastore revision --autogenerate --name plugin_name -m example\n# 升级数据库\nnb datastore upgrade --name plugin_name\n# 降级数据库\nnb datastore downgrade --name plugin_name\n```\n\n## 配置项\n\n配置方式：直接在 `NoneBot` 全局配置文件中添加以下配置项即可。\n\n### datastore_cache_dir\n\n- 类型: `str`\n- 默认: [nonebot_plugin_localstore](https://github.com/nonebot/plugin-localstore) 插件提供的缓存目录\n- 说明: 缓存目录\n\n### datastore_config_dir\n\n- 类型: `str`\n- 默认: [nonebot_plugin_localstore](https://github.com/nonebot/plugin-localstore) 插件提供的配置目录\n- 说明: 配置目录\n\n### datastore_data_dir\n\n- 类型: `str`\n- 默认: [nonebot_plugin_localstore](https://github.com/nonebot/plugin-localstore) 插件提供的数据目录\n- 说明: 数据目录\n\n### datastore_enable_database\n\n- 类型: `bool`\n- 默认: `True`\n- 说明: 是否启动数据库\n\n### datastore_database_url\n\n- 类型: `str`\n- 默认: `sqlite+aiosqlite:///data_dir/data.db`\n- 说明: 数据库连接字符串，默认使用 SQLite 数据库\n\n### datastore_database_echo\n\n- 类型: `bool`\n- 默认: `False`\n- 说明: 是否显示数据库执行的语句与其参数列表\n\n## 计划\n\n- [x] 调整配置为 K-V 存储\n- [x] 调整配置存放位置至专门的配置目录\n- [x] 数据库为可选项\n- [ ] 支持将配置存放至数据库中\n- [x] 支持 Alembic\n',
    'author': 'hemengyang',
    'author_email': 'hmy0119@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/he0119/nonebot-plugin-datastore',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
