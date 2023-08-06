# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lib', 'lib.api', 'lib.handler', 'lib.model']

package_data = \
{'': ['*']}

modules = \
['cli']
install_requires = \
['docopt>=0.6.2,<0.7.0',
 'gitpython>=3.1.30,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['trident = cli:cli']}

setup_kwargs = {
    'name': 'trident-sync',
    'version': '1.0.4',
    'description': '三叉戟，异构项目同步升级工具，The heterogeneous repo sync and upgrade CLI',
    'long_description': '# trident-sync 🔱 三叉戟同步\n\n三叉戟同步，是一款异构项目同步升级工具，二次开发同步神器。\n\n[中文](./readme.md) / [English](./readme-en.md)\n\n## 1. 简介\n\n当我们的项目内部使用了其他模版项目进行二次开发，那么那个模版项目就永远停留在当时的版本，无法方便的更新。\n\n本项目可以自动获取变更并合并到你的项目仓库，让集成的模版项目持续升级。\n\n本项目支持各类异构项目的同步升级\n\n* `多个模版项目` 同步到 `你项目的多个目录`\n* `模版项目的多个目录` 同步到 `你项目的多个目录`\n* `你项目的多个目录` 同步到 `多个模版项目`\n* `你项目的多个目录` 同步到 `模版项目的多个目录`\n\n## 2. 缘起\n\n我有一个 [certd](https://github.com/certd/certd) 项目，这是一个自动更新ssl证书的工具，但这不是重点。     \n重点是它一开始只是一个独立的命令行工具。    \n目录结构如下：\n\n```\nsrc\n| --packages\n    | --core           //实现申请证书的核心\n    | --plugins        //一些任务插件，部署证书到远程服务器、云服务之上。\n\n```\n\n某一天我想开发v2版本，把它升级成一个带后台和界面的web项目。      \n恰好我找到了两个模版项目(其实也是我写的🤭),可以帮我快速实现以上需求。\n\n* [fs-admin-antdv](https://github.com/fast-crud/fs-admin-antdv)  （前端admin模版）\n* [fs-server-js](https://github.com/fast-crud/fs-server-js)  （服务端）\n\n我把这两个项目复制到了`certd`项目中,进行二次开发。     \n此时`certd`项目目录结构变成如下：\n\n```\nsrc\n| --packages\n    | --core\n    | --plugins\n    | --ui\n        | --certd-client   //这是fs-admin-antdv的副本\n        | --certd-server   //这是fs-server-js的副本\n```\n\n为了使`certd-client`和`certd-server`能够随时同步`模版项目`的更新       \n我将使用本项目`trident-sync`来自动帮我升级。\n\n<p align="center">\n<img src="./doc/images/trident.png" height="400"/>\n<p align="center">像不像个三叉戟🔱？</p>\n<p>\n\n## 3. 原理过程\n\n初始化（init）：\n\n1. 初始化`同步工作仓库`（sync_work_repo）\n2. `clone` `源仓库`（src_repo）和`目标仓库`（target_repo），添加到`同步工作仓库`的`submodule`\n3. 给`目标仓库`创建并切换到`同步分支`（sync_branch）\n4. 将`源仓库内的文件`复制到`目标仓库对应的目录`，然后`commit、push`\n5. 此时`目标仓库`内的`sync_branch`分支拥有`源仓库`的副本\n\n同步（sync）：\n\n1. 当`源仓库`有变更时、拉取`源仓库`更新\n2. 删除`目标仓库对应的目录`，复制`源仓库所有文件`到`目标仓库对应的目录`\n3. 此时`git add . && git commit` 提交的就是`源仓库变更部分`\n4. 至此我们成功将`源仓库的更新`转化成了`目标仓库的commit`，后续就是常规的合并操作了。\n5. 创建`target.sync_branch` -> `target.main`的`PR`\n6. 处理`PR`，合并到开发主分支，升级完成\n\n<p align="center">\n<img src="./doc/images/desc.png" />\n<p align="center">同步流程图</p>\n<p>\n\n> 没有冲突的话，同步过程可以全部自动化。    \n> 解决冲突是唯一需要手动的部分。\n\n## 4. 快速开始\n\n### 4.1 准备工作\n\n* 安装 [python (3.8+)](https://www.python.org/downloads/)\n* 准备你的项目和要同步的源项目\n\n### 4.2 安装本工具\n\n```shell\n# 安装本工具，安装成功后就可以使用 trident 命令了\npip install trident-sync -u\n```\n\n### 4.2 编写配置文件\n\n* 创建一个同步工作目录，你可以任意命名，接下来都在这个目录下进行操作\n```\nmkdir sync_work_repo\ncd sync_work_repo\n```\n\n* 编写`./sync_work_repo/sync.yaml`， 下面是示例，请根据其中注释说明改成你自己的内容\n```yaml\n# ./sync_work_repo/sync.yaml\nrepo: # 仓库列表，可以配置多个仓库\n  fs-admin: # 上游项目1，可以任意命名\n    url: "https://github.com/fast-crud/fs-admin-antdv" # 仓库地址\n    path: "fs-admin-antdv"            # submodule保存路径，一般配置仓库名称即可\n    branch: "main"                    # 要同步过来的分支\n  certd: # 你的项目（接受同步项目），可以任意命名\n    url: "https://github.com/certd/certd"  # 仓库地址\n    path: "certd"                    # submodule保存路径，一般配置仓库名称即可\n    branch: "dev"                    # 你的代码开发主分支（接受合并的分支）例如dev、main、v1、v2等\n    # 以下配置与PR相关，更多关于PR的文档请前往 https://github.com/handsfree-work/trident-sync/tree/main/doc/pr.md\n    # 不配置的话影响也不大，你可以手动操作合并\n    token: ""                         # 仓库的token，用于提交PR\n    type: github                      # 仓库类型，用于提交PR，可选项：[github/gitee/gitea]\n    auto_merge: true                  # 是否自动合并,如果有冲突则需要手动处理\n# 注意： 初始化之后，不要修改url和path，以免出现意外。但是可以添加新的repo.\n\nsync: # 同步配置，可以配置多个同步任务\n  client: # 同步任务1，可以任意命名\n    src: # 源仓库\n      repo: fs-admin                  # 源仓库名称，上面repo配置的仓库引用\n      dir: \'.\'                        # 要同步给target的目录（不能为空目录）\n    target: #接受合并的仓库，就是你的项目\n      repo: certd                     # 目标仓库名称，上面repo配置的仓库引用\n      dir: \'package/ui/certd-client\'  # 接收src同步过来的目录（如果你之前已经使用过源仓库副本做了一部分特性开发，那么这里配置源仓库副本的目录）\n      allow_reset_to_root: False      # 是否允许重置同步分支到root commit记录（如果你按上面配置了副本目录。请留意sync执行时的警告信息）\n      branch: \'client_sync\'           # 同步分支名称（需要配置一个未被占用的分支名称）\n\noptions: #其他选项 【使用默认值可以不配置】\n  repo_root: repo          # submodule保存根目录\n  push: true               # 同步后是否push\n  pull_request: true       # 是否创建pull request，需要目标仓库配置token和type\n  proxy_fix: true          # 是否将https代理改成http://开头，解决python开启代理时无法发出https请求的问题\n  use_system_proxy: true   # 是否使用系统代理\n\n```\n\n### 4.3 初始化\n\n此命令会将`sync_work_repo`目录初始化成一个git仓库，然后将`sync.yaml`中配置的`repo` 添加为`submodule`\n\n```shell\ncd sync_work_repo\n# 执行初始化操作\ntrident init \n```\n\n<p align="center">\n<img src="./doc/images/init.png" />\n<p align="center">初始化执行效果</p>\n<p>\n\n> 只需运行一次即可，除非你添加了新的`repo`\n\n\n### 4.4 进行同步\n\n将根据`sync.yaml`中`sync`配置的同步任务进行同步更新，并提交PR，等你有空时处理有冲突的PR即可\n\n```shell\n# 以后你只需要定时运行这个命令，即可保持同步升级\ntrident sync \n```\n\n> 注意：不要在同步分支内写你自己的任何代码\n\n### 4.5 [可选] 保存 sync_work_repo\n\n将`sync_work_repo`提交到远程服务器，防止更换电脑丢失同步进度\n\n```shell\n# 给同步仓库设置远程地址，并push\ntrident remote --url=<sync_work_repo_git_url> \n```\n> 注意： `sync_work_repo_git_url` 应该是一个空的远程仓库     \n> 如果不是空的，可以加 `-f` 选项强制push（sync_work_repo原有的内容会被覆盖）。\n\n### 4.5 [可选] 定时运行\n\n你可以将 `<sync_work_repo>` 这个远程仓库和 `trident sync` 命令配置到任何`CI/DI`工具（例如jenkins、github\naction、drone等）自动定时同步\n\n### 4.6. 合并分支\n\n同步完之后，将会有三种情况：\n\n* 启用PR： [如何启用PR？](#启用PR)\n    * 无冲突：自动创建PR，然后自动合并，你无需任何操作\n    * 有冲突：自动创建PR，然后需要 [手动处理PR](#处理PR)\n* 未启用PR：\n    * 你需要 [手动合并](#手动合并)\n\n#### 启用PR\n\n要启用PR，你需要如下配置\n\n```yaml\nrepo:\n  target:\n    token: xxxx      # 创建PR的token\n    type: github     # upstream类型，支持[ github | gitee | gitea ]\n    auto_merge: true   # 是否自动合并\n\n```\n\n[token如何获取？](./doc/pr.md)\n\n\n#### 处理PR\n\n当PR有冲突时，就需要手动处理冲突，才能合并进入主分支\n\n* 其中 `github` `gitee`支持在web页面直接手动解决冲突\n* `gitea`需要线下解决，此时你仍然需要 [手动合并](#手动合并)\n\n#### 手动合并\n\n一般出现冲突了，都建议在IDE上手动进行合并\n\n1. 关闭PR（没有PR的话，请无视）\n2. 本地更新所有分支\n3. 通过IDE进行分支merge操作（rebase也行，用你平常熟悉的合并分支操作）\n\n```\ntarget:<sync_branch> -------->  target:<main_branch>\n    同步分支            merge         开发主分支\n```\n\n#### 避免冲突建议\n\n我们应该尽量避免冲突，请实际开发中遵循以下原则：\n\n1. 尽量不删除、不移动源项目的目录和文件（否则容易造成意想不到的难以解决的冲突）\n2. 尽量少在源项目的文件上进行修改（可以改，但尽量少）\n3. 新功能和新特性应该写在自己建立的新目录和新文件中\n\n总结就是六个字： 不删、少改、多加。\n\n## 6. 其他问题：\n\n### 5.1 为何不fork模版项目，通过submodule来管理\n\n这是我最初采用的方法，确实可以通过set-upstream,然后进行合并来进行同步升级。        \n但管理众多的submodule仍然是一件费力且很容易出错的事情，比如：\n\n* 想要采用git-flow模式，就得频繁切换所有的submodule的分支\n* 想要管控main分支的提交权限，多个submodule相当繁琐\n* lerna不支持submodule模块的发布\n\n',
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
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
