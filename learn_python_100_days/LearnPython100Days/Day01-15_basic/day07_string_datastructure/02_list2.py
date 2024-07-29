"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():

    # 定义列表
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ') # 输出元素，没有列表的格式，只有内容
    print()

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)

    # 列表的复制
    fruit3 = fruits                     # 没有复制列表只创建了新的引用，改变原列表会同时改变新列表
    fruits3 = fruits[:]                 # 复制到一个新的列表, 改变原列表不会改变新列表
    print(fruit3)                       # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits.append('avocado')
    print(fruit3)                       # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango', 'avocado']
    print(fruits3)                      # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

    # 列表的逆向，倒数切片
    fruits4 = fruits[-3:-1]             # 复制原列表倒数第三到倒数第二，-1是开区间
    print(fruits4)

    # 列表 逆向，
    fruits5 = fruits[::-1]              # 从倒数第一到倒数最后
    print(fruits5)
    fruits6 = fruits[:-4:-1]            # 从倒数第一到倒数第三
    print(fruits6)

    # 清空列表
    fruits5.clear()
    print(fruits5)

    # 列表排序
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort()
    print(list1)
    list1.sort(reverse=True)
    print(list1)


if __name__ == '__main__':
    main()
