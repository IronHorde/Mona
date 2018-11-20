# learn git

## 安装git
* *使用**sudo apt-get install git**就可以直接完成Git的安装*

## 创建版本库
1. *选择一个合适的地方，创建一个空目录*
2. *通过**git init**命令把这个目录变成Git可以管理的仓库*

## 使用版本库
* *用命令**git add**告诉Git，把文件添加到仓库*

* *用命令**git commit**告诉Git，把文件提交到仓库*

### 版本回退
* #### *用**git log**命令查看*
```bash
liyongjie@liyongjie-X455LD:~/git$ git log
commit 17c0c4ad82568b73a5821e3787795621fd232198
Author: guaimiriyan <316659146@qq.com>
Date:   Sun Nov 18 17:02:07 2018 +0800

    test

commit 90dd20c500aafecbc63843f21d43fd22389da821
Author: guaimiriyan <316659146@qq.com>
Date:   Sun Nov 18 16:38:24 2018 +0800

    modify two times

commit 1e6dcad82f31e3e7ae7e8ab84dab2f29318d2b12
Author: guaimiriyan <316659146@qq.com>
Date:   Sun Nov 18 16:37:14 2018 +0800

    modify one time

commit 249005a48e75d38038492cc9737bc90d0ed932bf
Author: guaimiriyan <316659146@qq.com>
Date:   Sun Nov 18 16:17:54 2018 +0800

    the second time use git

```
*看得眼花缭乱的，可以试试加上--pretty=oneline参数*
```bash
liyongjie@liyongjie-X455LD:~/git$ git log --pretty=oneline
17c0c4ad82568b73a5821e3787795621fd232198 test
90dd20c500aafecbc63843f21d43fd22389da821 modify two times
1e6dcad82f31e3e7ae7e8ab84dab2f29318d2b12 modify one time
249005a48e75d38038492cc9737bc90d0ed932bf the second time use git
7d75cf1f695c3ef482066b9cca87cae5dcfb0e07 the first time use git

```

* #### git reset --hard HEAD^
&emsp;&emsp;在Git中，用HEAD表示当前版本，也就是最新的提交1094adb...（注意我的提交ID和你的肯定不一样），上一个版本就是HEAD\^，上上一个版本就是HEAD\^\^，当然往上100个版本写100个\^ 比较容易数不过来，所以写HEAD~100。

* #### git reset --hard commit_id
&emsp;&emsp;版本号没必要写全，前几位就可以了，Git会自动去找。当然也不能只写前一两位，因为Git可能会找到多个版本号，就无法确定是哪一个了 
* #### Git提供了一个命令**git reflog**用来记录你的每一次命令
```bash
liyongjie@liyongjie-X455LD:~/Mona/notebook$ git reflog
150f784 HEAD@{0}: clone: from https://github.com/guaimiriyan/Mona
```
### 管理修改
&emsp;&emsp;若文档先添加到暂存区之后,再次修改直接提交,将不会把最新修改提交,想要提交必须再次将文件添加到暂存区在做提交.
### 撤销修改
* #### git status查看当前版本库状态
```bash
liyongjie@liyongjie-X455LD:~/Mona$ git status
位于分支 master
您的分支与上游分支 'origin/master' 一致。
尚未暂存以备提交的变更：
  （使用 "git add <文件>..." 更新要提交的内容）
  （使用 "git checkout -- <文件>..." 丢弃工作区的改动）

	修改：     notebook/Angus_Li/2018-11-18.md

修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
```
* #### git checkout -- file可以丢弃工作区的修改
在我理解这条命令是一个就近原则,若修改之后添加到暂存区里,则恢复到暂存区里的状态,若未修改之后未添加到暂存区则与版本库一致

* #### git reset HEAD \<file\>可以把暂存区的修改撤销掉
若已经添加但未提交时,可以使用次命令撤回暂存区里的修改回退到工作区
### 删除文件
* #### 情况一
    就是要删除,则可以使用**git rm**和**git commit**将文件在版本库里删除

* #### 情况二
    删错了,则可以使用**git checkout -- filename**,使其从版本库里还原到工作区

## 远程仓库

### 添加远程仓库
1. 在github里添加远程仓库
2. 关联远程仓库比如**git remote add origin https://github/guaimiriyan/demo1**
3. 最后push **git push -u origin master/dev**
4. 注意:origin 可以该为你想要的名字,但是在clone时候远程仓库就叫origin

### 克隆远程仓库
使用命令 **git clone https://github.com/guaimiriyan/demo1**

## 分支管理
### 创建分支与合并分支
* 使用**git branch**查看所有分支,且带*号的为HEAD指针指向的分支
* 使用**git branch \<name>** 创建分支,但不移动HEAD指针
* 使用**git checkout \<name>** 切换分支
* 使用**git checkout -b \<name>** 创建且切换分支
* 使用**git merge \<name>** 合并某分支到当前分支
* 使用**git branch -d \<name>** 删除分支
### 解决冲突
当不同分支对同一文件作出修改,使用git merge不能快速合并,则只有手动解决冲突
```bash
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git checkout -b feature
M	notebook/Angus_Li/2018-11-18.md
切换到一个新分支 'feature'
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ vim test.txt
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ cat test.txt
hello world!
hello feature!
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git add test.txt 
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git commit -m "feature commit"
[feature aa77782] feature commit
 1 file changed, 2 insertions(+)
 create mode 100644 notebook/Angus_Li/test.txt
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git checkout master
M	notebook/Angus_Li/2018-11-18.md
切换到分支 'master'
您的分支与上游分支 'origin/master' 一致。
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ vim test.txt
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ ls
2018-11-18.md
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ vim test.txt
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git add test.txt 
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git commit -m "master commit"
[master 15bc5c0] master commit
 1 file changed, 2 insertions(+)
 create mode 100644 notebook/Angus_Li/test.txt
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git merge feature
自动合并 notebook/Angus_Li/test.txt
冲突（添加/添加）：合并冲突于 notebook/Angus_Li/test.txt
自动合并失败，修正冲突然后提交修正的结果。
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ cat test.txt
hello world!
<<<<<<< HEAD
hello master!
=======
hello feature!
>>>>>>> feature
```
此时就需要手动修改将冲突解决掉,再进行提交
```bash
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ vim test.txt 
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ cat test.txt 
hello world!
hello master!
hello feature!

liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git add test.txt 
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git commit -m "solution"
[master a69a66c] solution
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git log --graph --pretty=oneline --abbrev-commit
*   a69a66c solution
|\  
| * aa77782 feature commit
* | 15bc5c0 master commit
|/  
* 8691214 git_day01
* 40f93da git_day01
* 85966aa git_day01
* 844f1a6 git_day01
* 150f784 create task example for other memebers
* ccaa2bf Update README.md
* aba7af2 Initial commit
liyongjie@liyongjie-X455LD:~/Mona/notebook/Angus_Li$ git branch -d feature
已删除分支 feature（曾为 aa77782）。
```
### 分支管理策略
由于在git优先使用fast forward方式合并时,这种方式在删除分支之后分支信息也会随之删除,所以使用**git merge --no-ff -m**则可以不使用Fast forwarf方式,就可以体现分支的信息
```bash
liyongjie@liyongjie-X455LD:~/git$ git checkout -b dev
切换到一个新分支 'dev'
liyongjie@liyongjie-X455LD:~/git$ vim test.txt 
liyongjie@liyongjie-X455LD:~/git$ cat test.txt 
aaaaaaaa
liyongjie@liyongjie-X455LD:~/git$ vim test.txt 
liyongjie@liyongjie-X455LD:~/git$ cat test.txt 
aaaaaaaa
dev come here!
liyongjie@liyongjie-X455LD:~/git$ git add test.txt 
liyongjie@liyongjie-X455LD:~/git$ git commit -m "dev come here"
[dev 71671e4] dev come here
 1 file changed, 1 insertion(+)
liyongjie@liyongjie-X455LD:~/git$ git checkout master
切换到分支 'master'
您的分支与上游分支 'origin/master' 一致。
liyongjie@liyongjie-X455LD:~/git$ git merge --no-ff -m "merge dev" dev
Merge made by the 'recursive' strategy.
 test.txt | 1 +
 1 file changed, 1 insertion(+)
liyongjie@liyongjie-X455LD:~/git$  git log --graph --pretty=oneline --abbrev-commit
*   1dbf22f merge dev
|\  
| * 71671e4 dev come here
|/  
* 17c0c4a test
* 90dd20c modify two times
* 1e6dcad modify one time
* 249005a the second time use git
* 7d75cf1 the first time use git
```
### Bug分支
1. 当未完成手中的工作,不得不改Bug时,可以使用**git stash**将当前工作现场隐藏起来
2. 然后到需要修复Bug的分支上,建立修复Bug的分支,进行修复
3. 接着回到刚才工作的分支进行工作,使用**git stash pop**或者不会删除stash内容的**git stash apply**l来进行恢复,但是第二种方法需要使用**git stash drop**来删除stash

### Feature分支
* 开发一个新feature，最好新建一个分支
* 如果要丢弃一个没有被合并过的分支，可以通过git branch -D \<name>强行删除。
### 多人协作
* 使用**git push orgin \<branch_name>** 将分支推送到远程仓库
* 使用**git checkout -b origin/\<branch_name>** 抓取远程仓库的分支
* 此时便可以在分支上工作了,然后add后commit,但此时如果令一个人也在此分支上对相同分件进行了修改.push步骤哦将失败,只有先pull最新的提交从该分支抓取下来,在本地合并
* 但在之前,必须使用**git branch --set-upstream-to \<branch-name> origin/\<branch-name>** 使本地dev与远程dev链接
* 使用**git pull**更新最新提交
* 解决合并冲突之后,再次提交
### rabase
* 在很多人pull和push会让分支变得十分复杂，使用**git rebase**可以让分支重新回到一条直线
## 标签管理
### 创建标签
* 切换到需要打标签的分支上去
* 使用**git tag \<name>**为最新提交打上标签
* 可以使用命令**git tag -a \<tagname> -m \"blablabla...\"** 可以指定标签信息
* **git tag**查看标签
* **git show \<tag_name>**可以查看说明文字
### 操作标签
* 命令**git push origin \<tagname>** 可以推送一个本地标签；
* 命令**git push origin --tags**可以推送全部未推送过的本地标签；
* 命令**git tag -d \<tagname>** 可以删除一个本地标签；
* 命令**git push origin :refs/tags/\<tagname>** 可以删除一个远程标签。
## 使用github pull request
* 在GitHub上，可以任意Fork开源仓库；
* 自己拥有Fork后的仓库的读写权限；
* 可以推送pull request给官方仓库来贡献代码。
## 自定义Git
### 忽略特殊文件
* 原则:
    1. 忽略操作系统自动生成的文件，比如缩略图等；
    2. 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的.class文件；
    3. 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。


* 编写.gitignore(如下)
```
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini

# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build

# My configurations:
db.ini
deploy_key_rsa

``` 
* 若文件想要传得文件在内,则使用**git add -f**强制加入
* 能是.gitignore写得有问题，需要找出来到底哪个规则写错了，可以用**git check-ignore**命令检查：
```
$ git check-ignore -v App.class
.gitignore:3:*.class    App.class
```
### 设置别名
*  **git config --global alias.st status**是将**git status**区别名为**git st**
* 配置Git的时候，加上--global是针对当前用户起作用的，如果不加，那只针对当前的仓库起作用
* 每个仓库的Git配置文件都放在.git/config文件中,若想删除别名找到alias删除即可
* 而当前用户的Git配置文件放在用户主目录下的一个隐藏文件.gitconfig中,配置别名也可以直接修改这个文件，如果改错了，可以删掉文件重新通过命令配置。
### 搭建Git服务器
1. 安装git：$ sudo apt-get install git
2. 创建一个git用户，用来运行git服务：$ sudo adduser git
3. 创建证书登录：收集所有需要登录的用户的公钥，就是他们自己的id_rsa.pub文件，把所有公钥导入到/home/git/.ssh/authorized_keys文件里，一行一个。
4. 初始化Git仓库：先选定一个目录作为Git仓库，假定是/srv/sample.git，在/srv目录下输入命令：$ sudo git init --bare sample.git ,Git就会创建一个裸仓库，裸仓库没有工作区，因为服务器上的Git仓库纯粹是为了共享，所以不让用户直接登录到服务器上去改工作区，并且服务器上的Git仓库通常都以.git结尾。然后，把owner改为git：$ sudo chown -R git:git sample.git
5. 禁用shell登录：出于安全考虑，第二步创建的git用户不允许登录shell，这可以通过编辑/etc/passwd文件完成。找到类似下面的一git:x:1001:1001:,,,:/home/git:/bin/bash改为：git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell这样，git用户可以正常通过ssh使用git，但无法登录shell，因为我们为git用户指定的git-shell每次一登录就自动退出。




