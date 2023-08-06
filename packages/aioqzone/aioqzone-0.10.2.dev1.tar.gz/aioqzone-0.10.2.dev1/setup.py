# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src',
 'jssupport': 'src/jssupport',
 'qqqr': 'src/qqqr',
 'qqqr.event': 'src/qqqr/event',
 'qqqr.qr': 'src/qqqr/qr',
 'qqqr.up': 'src/qqqr/up',
 'qqqr.up.captcha': 'src/qqqr/up/captcha',
 'qqqr.utils': 'src/qqqr/utils'}

packages = \
['aioqzone',
 'aioqzone.api',
 'aioqzone.event',
 'aioqzone.type',
 'aioqzone.utils',
 'jssupport',
 'qqqr',
 'qqqr.event',
 'qqqr.qr',
 'qqqr.up',
 'qqqr.up.captcha',
 'qqqr.utils']

package_data = \
{'': ['*'], 'qqqr.up.captcha': ['archive/*']}

install_requires = \
['cssselect>=1.1.0,<2.0.0',
 'httpx>=0.23.0,<0.24.0',
 'lxml>=4.9.1,<5.0.0',
 'opencv-python-headless>=4.7.0,<5.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'pytz>=2022.1,<2023.0',
 'rsa>=4.8,<5.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['numpy>=1.21.6,<1.22.0'],
 ':python_version >= "3.8" and python_version < "4.0"': ['numpy>=1.22.3,<2.0.0']}

setup_kwargs = {
    'name': 'aioqzone',
    'version': '0.10.2.dev1',
    'description': 'Python wrapper for Qzone web login and Qzone http api.',
    'long_description': '# aioqzone\n\naioqzone封装了一些Qzone接口。\n\n[![python](https://img.shields.io/pypi/pyversions/aioqzone?logo=python&logoColor=white)][home]\n[![QQQR](https://github.com/aioqzone/aioqzone/actions/workflows/qqqr.yml/badge.svg?branch=beta&event=schedule)](https://github.com/aioqzone/aioqzone/actions/workflows/qqqr.yml)\n[![version](https://img.shields.io/pypi/v/aioqzone?logo=python)][pypi]\n[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n[English](README_en.md) | 简体中文\n\n> 1. ⚠️ aioqzone 仍在开发阶段，任何功能和接口都有可能在未来的版本中发生变化。\n> 2. 🆘 **欢迎有意协助开发/维护的中文开发者**。不仅限于本仓库，[aioqzone][org] 所属的任何仓库都需要您的帮助。\n\n## 功能和特点\n\n### Qzone 功能\n\n- [x] 二维码登录\n- [x] 密码登录 (受限)\n- [x] 计算验证码答案\n- [ ] 通过网络环境检测\n- [x] 爬取HTML说说\n- [x] 爬取说说详细内容\n- [x] 爬取空间相册\n- [x] 点赞/取消赞\n- [x] 发布(仅文字)/修改/删除说说\n- [ ] 评论相关\n\n### 为什么选择 aioqzone\n\n- [x] 完整的 IDE 类型支持 (typing)\n- [x] API 结果类型验证 (pydantic)\n- [x] 异步设计\n- [x] 易于二次开发\n- [x] [文档支持](https://aioqzone.github.io/aioqzone)\n\n__在做了:__\n\n- [ ] 完善的测试覆盖\n\n## node 依赖\n\n- `jssupport.jsjson.AstLoader` 不需要借助其他进程；\n- 要使用 `jssupport.execjs` 和 `jssupport.jsjson.NodeLoader`，您（至少）需要安装 `Node.js` >= v14；\n- 要使用 `jssupport.jsdom`，您需要安装 `jsdom` 和 `canvas` 两个 npm 包。\n- 验证码部分需要使用 `canvas`，因此您需要正确配置运行环境内的 font config ([#45](https://github.com/aioqzone/aioqzone/issues/45)).\n\n## 包描述\n\n|包名    |简述  |\n|-----------|-------------------|\n|aioqzone   |封装Qzone API  |\n|jssupport  |执行JS            |\n|qqqr       |网页登录    |\n\n## 例子\n\n这些仓库提供了一些 aioqzone 的实际使用示例。\n\n### aioqzone 的插件们\n\n- [aioqzone-feed][aioqzone-feed]: 提供了操作 feed 的简单接口\n\n## 许可证\n\n```\nCopyright (C) 2022 aioqzone.\n\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU Affero General Public License as published\nby the Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU Affero General Public License for more details.\n\nYou should have received a copy of the GNU Affero General Public License\nalong with this program.  If not, see <https://www.gnu.org/licenses/>.\n```\n\n- aioqzone 以 [AGPL-3.0](LICENSE) 开源.\n- [免责声明](https://aioqzone.github.io/aioqzone/disclaimers.html)\n\n\n[home]: https://github.com/aioqzone/aioqzone "Python wrapper for Qzone web login and Qzone http api"\n[aioqzone-feed]: https://github.com/aioqzone/aioqzone-feed "aioqzone plugin providing higher level api for processing feed"\n[pypi]: https://pypi.org/project/aioqzone\n[org]: https://github.com/aioqzone\n',
    'author': 'aioqzone',
    'author_email': 'zzzzss990315@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aioqzone/aioqzone',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
