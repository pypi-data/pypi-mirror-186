# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lib', 'lib.api']

package_data = \
{'': ['*']}

modules = \
['cli']
install_requires = \
['PyYaml', 'docopt', 'gitpython', 'loguru>=0.6.0,<0.7.0', 'requests']

entry_points = \
{'console_scripts': ['trident = cli:cli']}

setup_kwargs = {
    'name': 'trident-sync',
    'version': '1.0.1',
    'description': '三叉戟，异构项目同步升级工具，The heterogeneous repo sync and upgrade CLI',
    'long_description': '# trident-sync 三叉戟同步\n\n异构项目同步升级CLI工具\n\n[中文](./readme.md) / [English](./readme-en.md)\n\n## 1. 简介\n\n当我们的monorepo项目内部使用了其他模版项目，那么那个模版项目就永远停留在当时的版本，无法方便的更新。\n\n本项目可以自动获取更新并提交PR到你的monorepo仓库，让集成的模版项目保持最新版本。\n\n本项目支持各类异构项目的同步升级\n\n* `多个模版项目` 同步到 `你项目的多个目录`\n* `模版项目的多个目录` 同步到 `你项目的多个目录`\n* `你项目的多个目录` 同步到 `多个模版项目`\n* `你项目的多个目录` 同步到 `模版项目的多个目录`\n\n\n## 2. 实现原理\n\n初始化：\n\n1. clone源仓库（src）和目标仓库（target）\n2. 给目标仓库创建并切换到同步分支（sync_branch）\n3. 将源仓库内的文件复制到目标仓库对应的目录，然后commit、push\n4. 此时目标仓库内的sync_branch分支拥有源仓库的副本\n\n升级：\n\n1. 当源仓库有变更时\n2. 拉取源仓库更新\n3. 删除目标仓库对应的目录，复制源仓库所有文件到目标仓库对应的目录\n4. 此时`git add . && git commit` 提交的就是源仓库有变更的那部分内容\n5. 然后创建`target.sync_branch` -> `target.main`的`PR`\n6. 处理`PR`\n\n![](./doc/images/desc.png)\n\n## 3. 应用场景\n\n例如：   \n我有一个 [certd](https://github.com/certd/certd) 项目，它是一个自动更新ssl证书的工具，但这不是重点。     \n重点是它一开始只是一个独立的命令行工具。   \n我通过`yarn`的`workspace`功能将多个子模块放在一个仓库中管理       \n它的目录结构如下：\n\n```js\nsrc\n| --packages\n| --core           //实现申请证书的核心\n| --plugins        //一些任务插件，部署证书到远程服务器、云服务之上。\n\n```\n\n某一天我想开发v2版本，想把它升级成一个带后台和界面的web项目。      \n恰好我找到了两个模版项目,可以帮我快速实现以上需求。\n\n* [fs-admin-antdv](https://github.com/fast-crud/fs-admin-antdv)  （前端admin模版）\n* [fs-server-js](https://github.com/fast-crud/fs-server-js)  （服务端）\n\n这时`certd`项目目录结构将变成如下：\n\n```js\nsrc\n| --packages\n| --core\n| --plugins\n| --ui\n| --certd - client   //这是fs-admin-antdv的副本\n| --certd - server   //这是fs-server-js的副本\n```\n\n为了使`certd-client`和`certd-server`能够随时同步`模版项目`的更新       \n我将使用`trident-sync`来自动帮我升级。\n\n<div style="text-align: center">\n<img src="./doc/images/trident.png" height="400"/>\n<div>像不像个三叉戟？</div>\n</div>\n\n## 4. 快速开始\n\n### 4.1 准备工作\n\n* 安装 [python](https://www.python.org/downloads/)\n* 准备你的项目和要同步的模版项目仓库地址和分支\n\n```shell\n# 安装本工具\npip install trident-sync\n# 创建一个同步目录，用来进行同步操作,你可以任意命名\nmkdir project-sync\n# 进入目录\ncd project-sync\n```\n\n### 4.2 编写`sync.yaml`文件\n\n下载 [sync.yaml模版](https://raw.githubusercontent.com/handsfree-work/trident-sync/main/sync.yaml) 文件保存到`sync`目录\n\n根据注释修改其中的配置\n\n### 4.3 初始化\n\n初始化会将sync初始化为一个git仓库    \n然后将`sync.yaml`中配置的多个`repo` 添加为`submodule`\n\n```shell\n# 执行初始化操作\ntrident init \n```\n> 注意：只需运行一次即可，除非你添加了新的`repo`\n\n### 4.4 进行同步\n\n将根据`sync.yaml`中`sync`配置的同步任务进行同步更新，并提交PR，当你有空时处理PR即可\n\n```shell\n# 以后你只需要定时运行这个命令，即可保持同步升级\ntrident sync \n```\n\n### 4.5 [可选] 保存 project-sync\n\n将`project-sync`提交到你的远程服务器，防止更换电脑丢失同步进度\n\n后续你可以在任意位置`clone`出`project-sync`之后，运行`trident sync`即可继续同步\n\n```shell\n# 执行初始化操作\ntrident remote --url=<project-sync_git_url> \n```\n\n> 注意：这个 `<project-sync_git_url>` 是一个全新的git仓库，用来保存同步进度的\n\n### 4.5 [可选] 定时运行\n\n你可以将 `<project-sync_git_url>` 这个远程仓库和 `trident sync` 命令配置到任何`CI/DI`工具（例如jenkins、github\naction、drone等）自动定时同步\n\n## 5. 其他问题：\n\n### 5.1 为何不fork模版项目，通过submodule来管理\n\n这是我最初采用的方法，确实可以通过set-upstream,然后进行合并来进行同步升级。        \n但管理众多的submodule仍然是一件费力且很容易出错的事情，比如：     \n* 想要采用git-flow模式，就得频繁切换所有的submodule的分支\n* 想要管控main分支的提交权限，多个submodule相当繁琐\n* lerna不支持submodule模块的发布\n\n',
    'author': 'xiaojunnuo',
    'author_email': 'xiaojunnuo@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
