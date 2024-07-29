"""
双色球随机选号程序, 6 + 1, 从1-33中选取六个，从1-16中选取一个

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    # 从 1- 33 中选择六个随机数，不放回，即在选取之后应该删除
    red_balls = [x for x in range(1, 34)]       # number from 1 - 33
    selected_balls = []

    for _ in range(6):
        index = randrange(len(red_balls))       # randrange() 从递增基数集合中返回一个随机值
        selected_balls.append(red_balls[index])
        del red_balls[index]                    # 删除被选中的红色球

    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数, 实现从列表中选择不重复的n个元素。
    # selected_balls = sample(red_balls, 6)

    # 把选择的6个数进行排序
    selected_balls.sort()

    # 重新从1-16中选择一个随机数
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
