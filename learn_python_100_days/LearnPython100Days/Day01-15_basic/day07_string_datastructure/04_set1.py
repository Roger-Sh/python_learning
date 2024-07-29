"""
定义和使用集合

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    # 创建集合, 集合没有重复元素，
    set1 = {1, 2, 3, 3, 3, 2}       # 直接赋值，重复元素自动剔除
    print(set1)
    print('Length =', len(set1))

    set2 = set(range(1, 10))        # 使用生成器
    print(set2)
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3)

    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}   # 使用推导式生成器
    print(set4)

    # 向集合添加元素和从集合删除元素。
    set1.add(4)             # 最后添加元素4
    set1.add(5)             # 最后添加元素5
    set2.update([11, 12])   # 最后添加 [11, 12]
    print(set1)             # {1, 2, 3, 4, 5}
    print(set2)             # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}
    set2.discard(5)         # 移除元素5
    set2.discard(5)         # 使用discard移除不存在的元素时不会报错
    print(set2)             # {1, 2, 3, 4, 6, 7, 8, 9, 11, 12}

    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)

    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()

    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)


if __name__ == '__main__':
    main()
