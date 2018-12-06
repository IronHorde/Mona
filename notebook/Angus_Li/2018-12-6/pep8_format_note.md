# pep8 note
* 每行不超过80个字符（长的导入模块语句和注释里的URL除外）
* 不要使用反斜杠连接行。Python会将圆括号, 中括号和花括号中的行隐式的连接起来 
* 如果一个文本字符串在一行放不下, 可以使用圆括号来实现隐式行连接
```python
str = ('哈哈哈哈哈啊哈哈哈哈哈哈哈啊哈哈哈阿哈哈'
       ＇这个字符串太长了吧哈哈哈哈哈哈哈哈哈哈哈阿哈哈＇)
```
* 在注释中，如果必要，将长的URL放在一行上。 
## 缩进
用4个空格来缩进代码，不要用tab, 也不要tab和空格混用.
```python
    Yes:   # 与起始变量对齐
       foo = long_function_name(var_one, var_two,
                                var_three, var_four)
       # 字典中与起始值对齐
       foo = {
           long_dictionary_key: value1 +
                                value2,
           ...
       }
       # 4 个空格缩进，第一行不需要
       foo = long_function_name(
           var_one, var_two, var_three,
           var_four)
       # 字典中 4 个空格缩进
       foo = {
           long_dictionary_key:
               long_dictionary_value,
           ...
       }
```
## 空行
顶级定义之间空2行, 方法定义之间空1行，顶级定义之间空两行, 比如函数或者类定义. 方法定义, 类定义与第一个方法之间, 都应该空一行. 函数或方法中, 某些地方要是你觉得合适, 就空一行.

## 空格
* 括号内不要有空格
* 不要在逗号, 分号, 冒号前面加空格
* 参数列表, 索引或切片的左括号前不应加空格
```python
Yes: spam(1)
no: spam (1)
Yes: dict['key'] = list[index]
No:  dict ['key'] = list [index]
```
* 在二元操作符两边都加上一个空格
* 当’=’用于指示关键字参数或默认参数值时, 不要在其两侧使用空格
*　不要用空格来垂直对齐多行间的标记, 因为这会成为维护的负担
```python
Yes: foo = 1000  # 注释
     long_name = 2  # 注释不需要对齐
     dictionary = {
         "foo": 1,
         "long_name": 2,
         }
No: foo       = 1000  # 注释
     long_name = 2     # 注释不需要对齐
     dictionary = {
         "foo"      : 1,
         "long_name": 2,
         }
``` 
## 注释
### 函数和方法
* 列出每个参数的名字, 并在名字后使用一个冒号和一个空格, 分隔对该参数的描述.如果描述太长超过了单行80字符,使用2或者4个空格的悬挂缩进(与文件其他部分保持一致). 描述应该包括所需的类型和含义. 如果一个函数接受*foo(可变长度参数列表)或者**bar (任意关键字参数), 应该详细列出*foo和**bar. 
* Returns: (或者 Yields: 用于生成器)描述返回值的类型和语义. 如果函数返回None, 这一部分可以省略. 
* Raises:列出与接口有关的所有异常.
例如：
```python
    def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass
```
### 类
类应该在其定义下有一个用于描述该类的文档字符串. 如果你的类有公共属性(Attributes), 那么文档中应该有一个属性(Attributes)段. 并且应该遵守和函数参数相同的格式.
```python
    class SampleClass(object):
    """
    Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```
### 块注释和行注释：
最需要写注释的是代码中那些技巧性的部分. 如果你在下次 代码审查 的时候必须解释一下, 那么你应该现在就给它写注释. 对于复杂的操作, 应该在其操作开始前写上若干行注释. 对于不是一目了然的代码, 应在其行尾添加注释.为了提高可读性, 注释应该至少离开代码2个空格.
```python
    # We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.

if i & (i-1) == 0:        # true iff i is a power of 2
```
## 类
如果一个类不继承自其它类, 就显式的从object继承. 嵌套类也一样.

## 字符串
* 避免在循环中用+和+=操作符来字符串拼接. 
```python
   Yes: items = ['<table>']
     for last_name, first_name in employee_list:
         items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
     items.append('</table>')
     employee_table = ''.join(items)

No: employee_table = '<table>'
    for last_name, first_name in employee_list:
        employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
    employee_table += '</table>'
```
* 在同一个文件中, 保持使用字符串引号的一致性.

## 导包
* 每个导入应该独占一行
* 导入总应该放在文件顶部, 位于模块注释和文档字符串之后, 模块全局变量和常量之前. 导入应该按照从最通用到最不通用的顺序分组:
  1. 标准库导入
  2. 第三方库导入
  3. 应用程序指定导入
* 每种分组中, 应该根据每个模块的完整包路径按字典序排序, 忽略大小写.

##命名规范
* 模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
* 类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
* 函数名一律小写，如有多个单词，用下划线隔开
* 私有函数在函数前加一个下划线_
* 变量名尽量小写, 如有多个单词，用下划线隔开
* 常量使用以下划线分隔的大写命名