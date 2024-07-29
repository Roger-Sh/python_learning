# LearnPython100Days

### 语言元素

##### 变量类型

- 整型 int
- 浮点型 float
- 字符串型 string
- 布尔型 bool
  - True, False
- 复数型

##### 变量类型转换

- `int()`：将一个数值或字符串转换成整数，可以指定进制。
- `float()`：将一个字符串转换成浮点数。
- `str()`：将指定的对象转换成字符串形式，可以指定编码。
- `chr()`：将整数转换成该编码对应的字符串（一个字符）。
- `ord()`：将字符串（一个字符）转换成对应的编码（整数）。

##### 命名规则

- 硬性规则：
  - 变量名由字母（广义的Unicode字符，不包括特殊字符）、数字和下划线构成，数字不能开头。
  - 大小写敏感（大写的`a`和小写的`A`是两个不同的变量）。
  - 不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
- PEP 8要求：
  - 用小写字母拼写，多个单词用下划线连接。
  - 受保护的实例属性用单个下划线开头（后面会讲到）。
  - 私有的实例属性用两个下划线开头（后面会讲到）

### 

### 判断

```python
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
```



### 循环

##### for-in 循环

```python
sum = 0
for x in range(101):
    sum += x
print(sum)
```

##### while 循环

```python
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
```



### 函数

```python
def func_name(arg1=1, arg2=2, *args, **kwargs):
    pass
	# return return_var
```

- 使用 def 定义函数
- 函数的参数可以使用默认值
- 不确定参数个数时，使用可变参数 `*args` 或者 `**kwargs`

```python
# example for *args
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

>>> test_var_args('yasoob', 'python', 'eggs', 'test')
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
```

```python
# example for **kwargs
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

>>> greet_me(name="yasoob")
name = yasoob
```

```python
# example for both *args and **kwargs
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    
# first with *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# now with **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```



### 模块

##### 导入不同模块

`module1.py`

```python
def foo():
    print('hello, world!')
```

`module2.py`

```python
def foo():
    print('goodbye, world!')
```

`test.py`

```python
import module1 as m1
import module2 as m2

m1.foo() 	# 'hello, world!'
m2.foo() 	# 'googdbye, world!'
```



##### 避免导入模块的可执行代码

`module3.py`

```python
def foo():
    pass

def bar():
    pass

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
```

`test.py`

```python
import module3

# 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
```

### Python 常用数据结构

##### 字符串

```python
# 字符串定义
s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""

# \ 斜杠表示转义
s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
# 字符串前面加r表示不希望 \ 体现转义功能
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'

```



##### 列表