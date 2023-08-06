# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nb_cli_plugin_docker']

package_data = \
{'': ['*'], 'nb_cli_plugin_docker': ['template/docker/*']}

install_requires = \
['nb-cli>=1.0.1,<2.0.0']

entry_points = \
{'nb': ['docker = nb_cli_plugin_docker.plugin:install']}

setup_kwargs = {
    'name': 'nb-cli-plugin-docker',
    'version': '0.1.0',
    'description': 'docker support for nb-cli',
    'long_description': '<!-- markdownlint-disable MD033 MD041 -->\n<p align="center">\n  <a href="https://cli.nonebot.dev/"><img src="https://cli.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# NB CLI Plugin Docker\n\n_✨ NoneBot2 命令行工具 Docker 插件 ✨_\n\n</div>\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/nonebot/nb-cli-plugin-docker/master/LICENSE">\n    <img src="https://img.shields.io/github/license/nonebot/nb-cli-plugin-docker" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nb-cli-plugin-docker">\n    <img src="https://img.shields.io/pypi/v/nb-cli-plugin-docker" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.8+-blue" alt="python">\n  <a href="https://results.pre-commit.ci/latest/github/nonebot/nb-cli-plugin-docker/master">\n    <img src="https://results.pre-commit.ci/badge/github/nonebot/nb-cli-plugin-docker/master.svg" alt="pre-commit" />\n  </a>\n  <br />\n  <a href="https://jq.qq.com/?_wv=1027&k=5OFifDh">\n    <img src="https://img.shields.io/badge/QQ%E7%BE%A4-768887710-orange?style=flat-square" alt="QQ Chat Group">\n  </a>\n  <a href="https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&appChannel=share&inviteCode=7b4a3&appChannel=share&businessType=9&from=246610&biz=ka">\n    <img src="https://img.shields.io/badge/QQ%E9%A2%91%E9%81%93-NoneBot-5492ff?style=flat-square" alt="QQ Channel">\n  </a>\n  <a href="https://t.me/botuniverse">\n    <img src="https://img.shields.io/badge/telegram-botuniverse-blue?style=flat-square" alt="Telegram Channel">\n  </a>\n  <a href="https://discord.gg/VKtE6Gdc4h">\n    <img src="https://discordapp.com/api/guilds/847819937858584596/widget.png?style=shield" alt="Discord Server">\n  </a>\n</p>\n\n## 准备\n\n在使用本插件前请确保 Docker CLI 以及 Docker Compose Plugin 已经安装，且可以从命令行直接使用。\n\n详细安装方法请参考 [Docker 文档](https://docs.docker.com/engine/install/)\n\n官方 Linux 快速安装一键脚本：\n\n```shell\ncurl -fsSL https://get.docker.com | sudo sh\n```\n\n## 安装插件\n\n```shell\nnb self install nb-cli-plugin-docker\n```\n',
    'author': 'yanyongyu',
    'author_email': 'yyy@nonebot.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nonebot/cli-plugin-docker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
