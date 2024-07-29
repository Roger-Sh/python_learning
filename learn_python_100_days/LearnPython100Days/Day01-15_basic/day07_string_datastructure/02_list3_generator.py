"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""

import sys


# 生成Fibonacci序列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b         # 这里相当于 a:=b, b:=a+b
        yield a                 # 通过 yield 关键字将一个普通函数改造成生成器函数, 返回 a


def fib2(n):
    a, b = 1, 2
    for _ in range(n):
        a, b = b, a - b
        yield a


def main():
    # 用range创建数值列表
    list1 = list(range(1, 11))                  # 列表 1到10
    print(list1)

    # 生成表达式
    list2 = [x * x for x in range(1, 11)]

    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))

    # 生成器对象(节省空间但生成下一个元素时需要花费时间)
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)                      # <generator object main.<locals>.<genexpr> at 0x000002047C425048>
    print(sys.getsizeof(gen))       # 120
    for elem in gen:
        print(elem, end=' ')        # A1 A2 A3 A4 A5 B1 B2 B3 B4 B5 C1 C2 C3 C4 C5 D1 D2 D3 ...
    print()

    # 自定义生成器方法
    gen = fib(20)
    print(gen)                      # <generator object fib at 0x000002047C47BD48>
    print(sys.getsizeof(gen))
    for elem in gen:
        print(elem, end=' ')        # 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
    print()

    gen = fib2(20)
    for elem in gen:
        print(elem, end=' ')
    print()


if __name__ == '__main__':
    main()
