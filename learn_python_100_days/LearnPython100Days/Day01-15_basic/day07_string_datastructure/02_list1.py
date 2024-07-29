"""
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    # 定义列表
    fruits = ['grape', '@pple', 'strawberry', 'waxberry']
    print(fruits)

    # 通过下标访问元素
    print(fruits[0])  # grape
    print(fruits[1])  # @pple
    print(fruits[-1])  # waxberry
    print(fruits[-2])  # strawberry

    # print(fruits[-5]) # IndexError
    # print(fruits[4])  # IndexError

    fruits[1] = 'apple'
    print(fruits)

    # 添加元素
    print("add elements###################")
    fruits.append('pitaya')         # 添加到最后
    fruits.insert(0, 'banana')      # 添加到位置0
    fruits.insert(1, "avocado")     # 添加到位置1
    fruits += ['watermelon']        # 添加到最后
    print(fruits)

    # 删除元素
    del fruits[1]  # 删除第一个
    print(fruits)
    fruits.pop()  # 删除最后一个
    print(fruits)
    fruits.pop(0)  # 删除第0个
    print(fruits)
    fruits.pop(1)  # 删除第1个
    print(fruits)
    fruits.remove('strawberry')  # 删除 strawberry
    print(fruits)

    # 乘号表示列表元素的重复
    list2 = ['hello'] * 3
    print(list2)  # ['hello', 'hello', 'hello']

    # 计算列表长度(元素个数)
    list1 = [1, 3, 5, 7, 100]
    print(len(list1))  # 5

    # 下标(索引)运算
    print(list1[0])  # 1
    print(list1[4])  # 100
    # print(list1[5])  # IndexError: list index out of range
    print(list1[-1])  # 100
    print(list1[-3])  # 5
    list1[2] = 300
    print(list1)  # [1, 3, 300, 7, 100]

    # 通过循环用下标遍历列表元素
    for index in range(len(list1)):
        print(list1[index])

    # 通过for循环遍历列表元素
    for elem in list1:
        print(elem)

    # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
    for index, elem in enumerate(list1):
        print(index, elem)


if __name__ == '__main__':
    main()
