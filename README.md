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
