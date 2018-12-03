# Mona

以松散小组的形式完成一些小项目，帮助大家适应合作开发的模式.

## 任务列表

### 2018-11-16~2018-11-23

* 搭建本地开发环境： pycharm + python3 + virtualenv。
* 学习使用markdown，推荐vscode + markdown插件。
* 熟悉git的使用。[廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)。
* 学习了解如何创建github的Pull Request。

* (可选) 学习vim，掌握基本操作。 推荐CoolShell的[vim简明练级攻略](https://coolshell.cn/articles/5426.html)
* vim的练习可以选择vscode + vim插件，或者pycharm + vim插件.

_本周目标_:

* 用markdown文档记录本周学习情况，把记录以pull request的形式提交到 /notebook/{名字}/{日期}.md

### 2018-11-26~2018-12-01

#### 反馈

##### jxy

* 可以把记录分成几个文件，总结归类，方便日后查阅；总结成工作日志。
* 在VSCode中装一个Markdown Lint格式检查插件，规范Markdown书写。 工作中代码也会有相应的Lint工具检查代码风格。

##### Angus_li

* 在VSCode中装一个Markdown Lint格式检查插件，规范Markdown书写。 工作中代码也会有相应的Lint工具检查代码风格。

#### 本周任务

* 继续学习使用vim。
* 用Python模拟实现一组Linux命令：
  例1：
  * input: python cmd.py ls
  * output: README.md notebook

  例2：
  * input: python cmd.py ls -l
  * output:
    > total 8
    > -rw-r--r--  1 Guang  staff  973 Nov 26 19:52 README.md
    > drwxr-xr-x  5 Guang  staff  160 Nov 26 19:49 notebook
* 给自己写的代码加上测试自动化用例：用unitTest2 + nosetests实现。学习Mock库的基本用法。
* 完整的开发环境: virtualenv + python3. 外部依赖配置在requirements.txt。

_本周目标_:

* 完成代码和测试用例，提交PR. 要求代码通过自己编写的所有测试用例.

### 2018-12-03~2018-12-08

#### 上周任务反馈

* 请参考PR里的comments，review了大家的代码，请修正comments。

先说代码中存在的问题:
1. 格式问题。Python是很讲究代码风格的，尤其是它通过代码缩进来控制程序流程，风格很重要。
2. 命名规则。命名规则不统一，缺少必要的注释。会对别人阅读你的代码造成很大的障碍。好的代码不是要让别人看不懂，而是要逻辑和调理清晰，别人接手的话可以很快看懂。
3. 测试用例覆盖不够。大家只简单测试了基本功能。我希望的是大家对自己的代码有完备的单元测试。这是好的开发者必备的技能。

做的好的地方：
1. 基本都满足了功能需求，还对chmod做了支持。
2. 掌握了unittest库和nose的使用。
3. 学会使用mock有点让我意外。单元测试中会大量使用到mock，了解mock是怎么工作，基本的使用方法，对将来的工作会有很多好处。

#### 本周任务

1. 重构上周的代码，务必做到代码清晰，可读。给代码加上docstring.
2. 学习编写单元测试用例。参考微软的这篇文章学习[单元测试的原则](https://docs.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices)
3. 了解Pep8，学习python代码编写的基本风格。
4. 学习使用click库来优化自己的代码。让代码更易懂，可扩展。可扩展意味着：ls 命令我可以先只支持部分功能，但是当我想添加更多功能的时候只要编写新的代码即可，不用对原先的代码做太多改动。


