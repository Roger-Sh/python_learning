"""
练习
修一个游泳池 半径(以米为单位)在程序运行时输入 游泳池外修一条3米宽的过道
过道的外侧修一圈围墙 已知过道的造价为25元每平米 围墙的造价为32.5元每米
输出围墙和过道的总造价分别是多少钱(精确到小数点后2位)

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""

import math


class Circle(object):

    def __init__(self, radius):
        """
        swimming pool radius
        :param radius:
        """
        self._radius = radius       # private variable

    # get private variable, @property装饰器,负责把一个方法变成属性调用的：
    # 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@radius.setter，负责把一个setter方法变成属性赋值
    @property
    def radius(self):
        return self._radius

    # set private variable
    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    @property
    def perimeter(self):            # 周长
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius


if __name__ == '__main__':  
    radius = float(input('请输入游泳池的半径: '))
    small = Circle(radius)
    big = Circle(radius + 3)
    print('围墙的造价为: ￥%.1f元' % (big.perimeter * 115))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area) * 65))
