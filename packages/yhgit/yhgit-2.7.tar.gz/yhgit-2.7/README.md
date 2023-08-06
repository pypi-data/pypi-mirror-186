
## [yhmgit](http://gitlab.yonghui.cn/operation-xm-qdjg/yhgit): 一个多仓库管理插件

当项目存在多个组件依赖，我们可能有以下需求：

  需要在多个组件分别建立开发分支；同步多个组件的远程代码；提交多个组件的代码；合并开发分支到发布分支，并自动打tag
  
  以上需求分别基于每个组件进行操作，每项任务都将耗费大量的精力和时间。

  基于以上需求，开发了yhmgit插件，使用该插件可以很好的解决： 开发分支的创建，开发分支状态查看，开发分支代码拉取，开发分支代码提交，开发分支推送，开发分支合并，开发分支合并到发布分支并打tag


### 环境

- Python >= 3.0

### 安装

如果你已经下载了最新的源码:

    python3 setup.py install

或者你可以通过pypi安装

    pip3 install yhgit

这两个命令都将安装所需的包依赖项。

可以在以下位置获取分发包以进行手动安装

    http://pypi.python.org/pypi/yhgit

如果你想从源代码克隆，你可以这样做:


```bash
git http://gitlab.yonghui.cn/operation-xm-qdjg/yhgit
```


### 说明文档

#### 1. 通过 yhgit install 拉取或者创建新分支

    -b 指定新建的分支名
    
##### 1 使用

```
    yhgit install -b test abc    
    yhgit install 
```

##### 2 执行过程
    根据命令行或者本地PodfileLocal中指定的分支或者组件
    1. 判断本地是否有modules文件夹
    2. 获取PodfileModule中依赖的组件信息  
    3. 判断组件依赖的分支或者tag是否存在，不存在就抛出异常
    4. 判断本地是否有组件的文件夹，如果有就跳过并抛出异常
    5. 新建分支，如果分支存在就切到对应分支，如果分支不存在就新建分支
    6. 更新podfileModule中为分支依赖，如果顶部branch为空就更新顶部，如果顶部不为空就更新组件branch依赖
    7. 更新PodfileLocal中依赖为路径依赖

#### 2. 通过 yhgit status 查看组件状态 

##### 1 使用
```
yhgit status
```

##### 2 执行过程
    根据本地PodfileLocal.yaml中配置的仓库，获取所有仓库的开发分支及仓库状态
    1. 获取本地PodfileLocal中组件  
    2. 判断本地modules中的组件是否存在
    3. 执行git status状态，有变更就提示变更的文件，否则提示无变化
    4. 以表格的形式输出执行结果

#### 3. 通过 yhgit commit 提交本地修改

    -m 提交信息

##### 1 使用
```
yhgit commit -m '提交'
```
##### 2 执行过程

    根据本地PodfileLocal.yaml中配置的仓库，提交本地仓库中的修改
    1. 获取本地PodfileLocal中组件  
    2. 判断本地modules中的组件是否存在
    3. 判断本地是否有变更，有变更就提交，没有就提示没有提交记录
    4. 以表格的形式输出执行结果
   
#### 4. 通过 yhgit pull 拉取开发分支最新代码

##### 1 使用
```
yhgit pull
```
##### 2 执行过程

    根据本地PodfileLocal.yaml中配置的仓库，拉取远端仓库中代码
    1. 获取本地PodfileLocal中组件  
    2. 判断本地modules中的组件是否存在
    3. 判断本地是否有变更，有变更就提示异常，没有就执行git pull
    4. 以表格的形式输出执行结果

 #### 5. 通过 yhgit push 推送本地代码到远端

##### 1 使用
````
yhgit push
````
##### 2 执行过程
    根据本地PodfileLocal.yaml中配置的仓库，推送本地代码到远端
    1. 获取本地PodfileLocal中组件  
    2. 判断本地modules中的组件是否存在
    3. 判断本地是否有变更，有变更就提示异常，没有就执行git push
    4. 以表格的形式输出执行结果

 #### 6. 通过 yhgit merge 合并远端其他分支代码到当前分支

    组件 可以指定组件，默认为根据PodfileModule中所有组件

##### 1 使用
````
yhgit merge -b master abc
````

##### 2 执行过程
    根据组件，合并其他分支到当前分支
    1. 获取本地PodfileLocal中组件  
    2. 判断本地modules中的组件是否存在
    3. 判断本地是否有变更，有变更就提示异常，没有就执行git merge
    4. 以表格的形式输出执行结果

 #### 7. 通过 yhgit release 合并开发分支到master，并自动打新tag及更新本地yaml文件

    组件 可以指定组件，默认为根据PodfileModule中所有组件

##### 1 使用
````
yhgit release abc
````

##### 2 执行过程
    根据本地PodfileModule.yaml中配置的仓库，合并开发分支到master，并自动打新的tag，并更新yaml文件
    1. 如果path中不存在tagpath，先在path中新建tagpath目录，用于临时存放组件代码
    2. 根据PodfileModule.yaml中组件的依赖：
       clone开发分支代码；
       如果开发分支版本号大于master分支，那么新的版本号就是开发分支版本号，否则就自增1；
       更新版本号并提交代码；然后根据新版本号打tag，并提交到远端分支；
       更新PodfileModule.yaml中的依赖为tag，并清空PodfileLocal .yaml中的文件

 #### 8. 通过 yhgit clean 清空本地PodfileLocal.yaml 及 modules文件夹

##### 1 使用
````
yhgit clean
````
##### 2 执行过程

    清空本地PodfileLocal.yaml 及 modules文件夹

#### 9. 通过 yhgit version 清空本地PodfileLocal.yaml 及 modules文件夹

##### 1 使用
````
yhgit version
yhgit -v
````
##### 2 执行过程
    查看yhgit的版本号

#### 10. 通过 yhgit help 查看当前

##### 1 使用
````
yhgit help
yhgit -h
````
##### 2 执行过程
    
    查看yhgit的帮助文档


### 怎么用

```

    # 新建开发分支
    yghit install 
    # 拉取远端代码
    yhgit pull
    # 推送本地代码
    yhgit push
    # 提交本地代码
    yhgit commit -m "提交信息"
    # 合并其他分支到当前开发分支
    yhgit merge -b master abc
    # 查看本地代码状态
    yhgit status
    # 发布组件开发分支
    yhgit release abc / yhgit release
    # 清空本地开发分支
    yhgit clean
    # 查看版本号
    yhgit version / yhgit -v
    # 查看帮助文档
    yhgit help / yhgit -h
   
```

        

