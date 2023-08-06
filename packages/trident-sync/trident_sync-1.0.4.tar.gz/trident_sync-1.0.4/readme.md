# trident-sync 🔱 三叉戟同步

三叉戟同步，是一款异构项目同步升级工具，二次开发同步神器。

[中文](./readme.md) / [English](./readme-en.md)

## 1. 简介

当我们的项目内部使用了其他模版项目进行二次开发，那么那个模版项目就永远停留在当时的版本，无法方便的更新。

本项目可以自动获取变更并合并到你的项目仓库，让集成的模版项目持续升级。

本项目支持各类异构项目的同步升级

* `多个模版项目` 同步到 `你项目的多个目录`
* `模版项目的多个目录` 同步到 `你项目的多个目录`
* `你项目的多个目录` 同步到 `多个模版项目`
* `你项目的多个目录` 同步到 `模版项目的多个目录`

## 2. 缘起

我有一个 [certd](https://github.com/certd/certd) 项目，这是一个自动更新ssl证书的工具，但这不是重点。     
重点是它一开始只是一个独立的命令行工具。    
目录结构如下：

```
src
| --packages
    | --core           //实现申请证书的核心
    | --plugins        //一些任务插件，部署证书到远程服务器、云服务之上。

```

某一天我想开发v2版本，把它升级成一个带后台和界面的web项目。      
恰好我找到了两个模版项目(其实也是我写的🤭),可以帮我快速实现以上需求。

* [fs-admin-antdv](https://github.com/fast-crud/fs-admin-antdv)  （前端admin模版）
* [fs-server-js](https://github.com/fast-crud/fs-server-js)  （服务端）

我把这两个项目复制到了`certd`项目中,进行二次开发。     
此时`certd`项目目录结构变成如下：

```
src
| --packages
    | --core
    | --plugins
    | --ui
        | --certd-client   //这是fs-admin-antdv的副本
        | --certd-server   //这是fs-server-js的副本
```

为了使`certd-client`和`certd-server`能够随时同步`模版项目`的更新       
我将使用本项目`trident-sync`来自动帮我升级。

<p align="center">
<img src="./doc/images/trident.png" height="400"/>
<p align="center">像不像个三叉戟🔱？</p>
<p>

## 3. 原理过程

初始化（init）：

1. 初始化`同步工作仓库`（sync_work_repo）
2. `clone` `源仓库`（src_repo）和`目标仓库`（target_repo），添加到`同步工作仓库`的`submodule`
3. 给`目标仓库`创建并切换到`同步分支`（sync_branch）
4. 将`源仓库内的文件`复制到`目标仓库对应的目录`，然后`commit、push`
5. 此时`目标仓库`内的`sync_branch`分支拥有`源仓库`的副本

同步（sync）：

1. 当`源仓库`有变更时、拉取`源仓库`更新
2. 删除`目标仓库对应的目录`，复制`源仓库所有文件`到`目标仓库对应的目录`
3. 此时`git add . && git commit` 提交的就是`源仓库变更部分`
4. 至此我们成功将`源仓库的更新`转化成了`目标仓库的commit`，后续就是常规的合并操作了。
5. 创建`target.sync_branch` -> `target.main`的`PR`
6. 处理`PR`，合并到开发主分支，升级完成

<p align="center">
<img src="./doc/images/desc.png" />
<p align="center">同步流程图</p>
<p>

> 没有冲突的话，同步过程可以全部自动化。    
> 解决冲突是唯一需要手动的部分。

## 4. 快速开始

### 4.1 准备工作

* 安装 [python (3.8+)](https://www.python.org/downloads/)
* 准备你的项目和要同步的源项目

### 4.2 安装本工具

```shell
# 安装本工具，安装成功后就可以使用 trident 命令了
pip install trident-sync -u
```

### 4.2 编写配置文件

* 创建一个同步工作目录，你可以任意命名，接下来都在这个目录下进行操作
```
mkdir sync_work_repo
cd sync_work_repo
```

* 编写`./sync_work_repo/sync.yaml`， 下面是示例，请根据其中注释说明改成你自己的内容
```yaml
# ./sync_work_repo/sync.yaml
repo: # 仓库列表，可以配置多个仓库
  fs-admin: # 上游项目1，可以任意命名
    url: "https://github.com/fast-crud/fs-admin-antdv" # 仓库地址
    path: "fs-admin-antdv"            # submodule保存路径，一般配置仓库名称即可
    branch: "main"                    # 要同步过来的分支
  certd: # 你的项目（接受同步项目），可以任意命名
    url: "https://github.com/certd/certd"  # 仓库地址
    path: "certd"                    # submodule保存路径，一般配置仓库名称即可
    branch: "dev"                    # 你的代码开发主分支（接受合并的分支）例如dev、main、v1、v2等
    # 以下配置与PR相关，更多关于PR的文档请前往 https://github.com/handsfree-work/trident-sync/tree/main/doc/pr.md
    # 不配置的话影响也不大，你可以手动操作合并
    token: ""                         # 仓库的token，用于提交PR
    type: github                      # 仓库类型，用于提交PR，可选项：[github/gitee/gitea]
    auto_merge: true                  # 是否自动合并,如果有冲突则需要手动处理
# 注意： 初始化之后，不要修改url和path，以免出现意外。但是可以添加新的repo.

sync: # 同步配置，可以配置多个同步任务
  client: # 同步任务1，可以任意命名
    src: # 源仓库
      repo: fs-admin                  # 源仓库名称，上面repo配置的仓库引用
      dir: '.'                        # 要同步给target的目录（不能为空目录）
    target: #接受合并的仓库，就是你的项目
      repo: certd                     # 目标仓库名称，上面repo配置的仓库引用
      dir: 'package/ui/certd-client'  # 接收src同步过来的目录（如果你之前已经使用过源仓库副本做了一部分特性开发，那么这里配置源仓库副本的目录）
      allow_reset_to_root: False      # 是否允许重置同步分支到root commit记录（如果你按上面配置了副本目录。请留意sync执行时的警告信息）
      branch: 'client_sync'           # 同步分支名称（需要配置一个未被占用的分支名称）

options: #其他选项 【使用默认值可以不配置】
  repo_root: repo          # submodule保存根目录
  push: true               # 同步后是否push
  pull_request: true       # 是否创建pull request，需要目标仓库配置token和type
  proxy_fix: true          # 是否将https代理改成http://开头，解决python开启代理时无法发出https请求的问题
  use_system_proxy: true   # 是否使用系统代理

```

### 4.3 初始化

此命令会将`sync_work_repo`目录初始化成一个git仓库，然后将`sync.yaml`中配置的`repo` 添加为`submodule`

```shell
cd sync_work_repo
# 执行初始化操作
trident init 
```

<p align="center">
<img src="./doc/images/init.png" />
<p align="center">初始化执行效果</p>
<p>

> 只需运行一次即可，除非你添加了新的`repo`


### 4.4 进行同步

将根据`sync.yaml`中`sync`配置的同步任务进行同步更新，并提交PR，等你有空时处理有冲突的PR即可

```shell
# 以后你只需要定时运行这个命令，即可保持同步升级
trident sync 
```

> 注意：不要在同步分支内写你自己的任何代码

### 4.5 [可选] 保存 sync_work_repo

将`sync_work_repo`提交到远程服务器，防止更换电脑丢失同步进度

```shell
# 给同步仓库设置远程地址，并push
trident remote --url=<sync_work_repo_git_url> 
```
> 注意： `sync_work_repo_git_url` 应该是一个空的远程仓库     
> 如果不是空的，可以加 `-f` 选项强制push（sync_work_repo原有的内容会被覆盖）。

### 4.5 [可选] 定时运行

你可以将 `<sync_work_repo>` 这个远程仓库和 `trident sync` 命令配置到任何`CI/DI`工具（例如jenkins、github
action、drone等）自动定时同步

### 4.6. 合并分支

同步完之后，将会有三种情况：

* 启用PR： [如何启用PR？](#启用PR)
    * 无冲突：自动创建PR，然后自动合并，你无需任何操作
    * 有冲突：自动创建PR，然后需要 [手动处理PR](#处理PR)
* 未启用PR：
    * 你需要 [手动合并](#手动合并)

#### 启用PR

要启用PR，你需要如下配置

```yaml
repo:
  target:
    token: xxxx      # 创建PR的token
    type: github     # upstream类型，支持[ github | gitee | gitea ]
    auto_merge: true   # 是否自动合并

```

[token如何获取？](./doc/pr.md)


#### 处理PR

当PR有冲突时，就需要手动处理冲突，才能合并进入主分支

* 其中 `github` `gitee`支持在web页面直接手动解决冲突
* `gitea`需要线下解决，此时你仍然需要 [手动合并](#手动合并)

#### 手动合并

一般出现冲突了，都建议在IDE上手动进行合并

1. 关闭PR（没有PR的话，请无视）
2. 本地更新所有分支
3. 通过IDE进行分支merge操作（rebase也行，用你平常熟悉的合并分支操作）

```
target:<sync_branch> -------->  target:<main_branch>
    同步分支            merge         开发主分支
```

#### 避免冲突建议

我们应该尽量避免冲突，请实际开发中遵循以下原则：

1. 尽量不删除、不移动源项目的目录和文件（否则容易造成意想不到的难以解决的冲突）
2. 尽量少在源项目的文件上进行修改（可以改，但尽量少）
3. 新功能和新特性应该写在自己建立的新目录和新文件中

总结就是六个字： 不删、少改、多加。

## 6. 其他问题：

### 5.1 为何不fork模版项目，通过submodule来管理

这是我最初采用的方法，确实可以通过set-upstream,然后进行合并来进行同步升级。        
但管理众多的submodule仍然是一件费力且很容易出错的事情，比如：

* 想要采用git-flow模式，就得频繁切换所有的submodule的分支
* 想要管控main分支的提交权限，多个submodule相当繁琐
* lerna不支持submodule模块的发布

