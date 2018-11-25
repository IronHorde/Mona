#<center>git笔记</center>
##一、git是什么
git是一个分布式版本控制系统，其每个用户都是一个完整的版本库，在使用时可以离线工作，而不需要联网从版本库同步文件。
##二、git安装
###1.环境
centOS7
###2.安装指令
#####centOS/Redhat
    yum install -y git-core
#####ubuntu
    apt-get install git
##三、git常用指令
###1.创建git版本库
找一个适合的位置，进入该位置，通过git init指令创建版本库
###2.向git中添加文件
将文件创建或移动到git版本库文件夹中或其子文件夹中
git add 文件名
git commit -m [添加该文件或该次改动注释]
修改文件添加到git中也是一样的步骤
###3.查看git状态
git status
能够查看是否有已修改文件但没有提交的
###4.查看文件做了什么修改
git diff
+后面是修改的内容
###5.历史记录
git log
查看每次修改，
--pretty=oneline可以简化视图
###6.回退版本
git reset --hard [版本号]
<b>原理：git中有一个head指针，指向当前版本的上一个版本，该条指令就是重新定位head指针的位置</b>
###7.查看历史操作
git reflog
如果要回退到未来的版本，则可以通过该指令查询版本号
###8.git工作区暂存区概念
git文件所处的位置为工作区，.git文件中属于版本库，当对工作区文件进行修改后，通过git add 命令添加到暂存区，最后commit，commit只会提交暂存区的修改到系统中
###9.撤销未add的修改
git checkout -- [filename]
如果已经add，则通过git reset HEAD [filename] 从暂存区中删除该文件的修改，此时该文件的修改状态变为未add，然后通过git checkout撤销更改
###10.删除文件
git rm [filename] 在版本库中删除文件，回退到以前版本可以恢复该文件，但会丢失更改
##四、远程git
###1.在github上连接自己的仓库
在本地生成ssh公钥，将公钥复制到github上的sshkey中，添加完毕后再github上创建git仓库，在本地连接即可
 git remote add origin git@github.com:jxy121/learngit.git
创建命令
git push -u origin master
同步
###2.从github上克隆仓库
git clone
##五、git分支控制
###1.分支
分支是另外一个独立的版本控制，建立在当前版本分支控制之上，但是其修改对当前版本分支不造成影响，对当前版本分支不可见
###2.创建分支
git checkout -b [分支名]
相当于
git branch dev	创建dev
git checkout dev 切换到dev

git branch 查看分支
###3.删除分支
git branch -d [分支]
###4.合并分支
git merge [分支] 合并某分支到当前分支
###5.合并分支发生冲突
git会将两文件不同处保存到文件中，并要求修改，修改完后重新合并即可
###6.关于合并分支并删除分支后信息丢失问题
git merge --no-ff -m "注释" [分支名]
该种方式禁用fast forward 可以在历史记录中查询到被合并分支信息
fast forward无法查询信息
####7.修复bug
临时保存运行环境 git stash
创建修复分支 git checkout -b []
修改完之后将分支合并 git merge
查看保存运行环境git stash list
恢复工作环境
一是用git stash apply恢复，但是恢复后，stash内容并不删除，你需要用git stash drop来删除。
另一种方式是用git stash pop，恢复的同时把stash内容也删了。
####8.创建future分支
销毁分支git branch -d feature-vulcan
如果没有合并，则会销毁失败，强行删除需要使用-D参数
####9.提交本地分支到远程库
git push origin [分支名]
####10.提取远程特定分支到本地
git checkout -b dev origin/dev
多人协作的工作模式通常是这样：

首先，可以试图用git push origin <branch-name>推送自己的修改；

如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；

如果合并有冲突，则解决冲突，并在本地提交；

没有冲突或者解决掉冲突后，再用git push origin <branch-name>推送就能成功！

如果git pull提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream-to <branch-name> origin/<branch-name>。

这就是多人协作的工作模式，一旦熟悉了，就非常简单。
####9.git rebase
rebase操作可以把本地未push的分叉提交历史整理成直线；
rebase的目的是使得我们在查看历史提交的变化时更容易，因为分叉的提交需要三方对比。
##六、标签管理
####1.定义
标签是版本库的一个快照。
Git的标签虽然是版本库的快照，但其实它就是指向某个commit的指针（跟分支很像对不对？但是分支可以移动，标签不能移动），所以，创建和删除标签都是瞬间完成的。
####2.创建标签
git tag [标签名]
默认标签是打在最新提交的commit上的
对历史提交打标签
git tag v0.9 [commit id]
git tag查看标签，标签不是按时间顺序列出，而是按字母排序的
可以用git show <tagname>查看标签信息

还可以创建带有说明的标签，用-a指定标签名，-m指定说明文字：
git tag -a v0.1 -m "version 0.1 released" 1094adb

<b>标签总是和某个commit挂钩。如果这个commit既出现在master分支，又出现在dev分支，那么在这两个分支上都可以看到这个标签。</b>
####3.删除标签
git tag -d v0.1
要推送某个标签到远程，使用命令git push origin <tagname>：
git push origin v1.0
一次性推送全部尚未推送到远程的本地标签：
git push origin --tags
删除已经推送到远程的标签
先从本地删除，在删除远程
git push origin :refs/tags/v0.9
##七、自定义git
####1.忽略特殊文件
创建一个特殊的.gitignore文件，然后把要忽略的文件名填进去，Git就会自动忽略这些文件。
忽略文件的原则是：

忽略操作系统自动生成的文件，比如缩略图等；
忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的.class文件；
忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

添加一个被git忽略的文件
git add -f [filename]

git check-ignore -v [filename]可以查看哪条规则忽略了该文件
####2.配置别名
git config --global alias.[别名] [原命令]
--global参数是全局参数，也就是这些命令在这台电脑的所有Git仓库下都有用。加上--global是针对当前用户起作用的，如果不加，那只针对当前的仓库起作用。
