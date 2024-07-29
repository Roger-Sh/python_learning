from random import randint


def roll_dice(n=2):
    """
    roll a dice with n times
    :param n:
    :return: total
    """

    total = 0

    for i in range(n):
        print("roll {:d} time".format(i))
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """
    add 3 numbers
    :param a:
    :param b:
    :param c:
    :return: a + b + c
    """

    return a + b + c


# if no arg, use default n = 2
print(roll_dice())

# roll 3 times
print(roll_dice(3))

# transfer different args
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(c=3, b=2, a=1))  # args can be in different orders


# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
