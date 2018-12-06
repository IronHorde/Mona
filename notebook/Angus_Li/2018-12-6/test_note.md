# TEST NOTE
## mock
Mock是Python中一个用于支持的测试的库，它的主要功能是使用mock对象替代掉指定的Python对象，以达到模拟对象的行为。

例子:如果此时有个项目a,有个模块b且其中有个方法c.方法c请求服务器并获取json返回值进行处理.此时我们如何对方法c进行单元测试

答:我们可以搭建一个简单的服务器,但是效率很低,而且搭建的服务器不可能返回所有有可能的值.所以需要Mock模块.

<font color="red">我的理解:Mock是在测试里模拟一个的类的实例来方便测试,因为程序耦合的问题这样可以进行准确的单元测试</font>

### mock的一般用法
1. 找到需要替代的对象(类 函数 类的实例)
2. 实例化Mock类得到mock实例且实现其行为
3. 使用这个mock对象替换需要代替的对象
4. 之后可以写测试代码,比较

比如:
```python
class client():
    def check(name):
       result = check_name(name)
       return result
    
    def login():
        return check('angus')
```
我想对login进行测试但是肯定会使用到check函数,所以为了准确的对login进行测试则需要模拟check函数.
```python
import unittest
import client
import mock
class TestClient(unittest.TestCase):
    def test_success_login(self):
        success_login = mock.Moc(return_value='success')
        client.check = success.login
        self.assertEqual(client.login,'sucess')

```
### mock的参数
* spec:设置mock对象的属性
* return_value
* side_effect：可以定义异常，也可以定义一系列的参数．如［１，２，３］
1. 当side_effect调用的时候,return_value会失效
2. 还有一点需要强调的就是，如果要模拟一个对象而不是函数，你可以直接在mock对象上添加属性和方法，并且每一个添加的属性都是一个mock对象，也就是说可以对这些属性进行配置,并且可以一直递归的定义下去。
### mock断言
* assert_called_with(*args, **kwargs)
* assert_called_once_with(*args, **kwargs)
* assert_any_call(*args, **kwargs)
* assert_has_calls(calls, any_order=False)
### patch
* @mock.patch("client.check")可以进行模拟
* @mock.patch.obiext(client,'check') 

文档：https://docs.python.org/3.4/library/unittest.mock.html
## stub