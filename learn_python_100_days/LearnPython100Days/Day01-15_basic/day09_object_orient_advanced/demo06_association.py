"""
对象之间的关联关系

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import sqrt


# class Point
class Point(object):

    def __init__(self, x=0, y=0):
        """
        定义一个point,
        :param x: x坐标
        :param y: y坐标
        """
        self._x = x
        self._y = y

    # 移动到(x, y)
    def move_to(self, x, y):
        self._x = x
        self._y = y

    # 移动坐标(dx, dy)
    def move_by(self, dx, dy):
        self._x += dx
        self._y += dy

    # 与其他点的距离
    def distance_to(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx ** 2 + dy ** 2)

    # 输出点的坐标
    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))


# class Line
class Line(object):

    def __init__(self, start=Point(0, 0), end=Point(0, 0)):
        """
        定义一条线段，起始点start， 终点end
        :param start:
        :param end:
        """
        self._start = start
        self._end = end

    # getter_start
    @property
    def start(self):
        return self._start

    # setter_start
    @start.setter
    def start(self, start):
        self._start = start

    # getter_end
    @property
    def end(self):
        return self.end

    # setter_end
    @end.setter
    def end(self, end):
        self._end = end

    # getter_length
    @property
    def length(self):
        return self._start.distance_to(self._end)  # 起始点到终点的距离

    def __str__(self):
        return 'This line start at (%s), end at (%s), the length of this line is %s' \
               % (str(self._start), str(self._end), str(self.length))


if __name__ == '__main__':
    p1 = Point(3, 5)
    print(p1)

    p2 = Point(-2, -1.5)
    print(p2)

    line = Line(p1, p2)
    print(line.length)

    line.start.move_to(2, 1)    # 起始点移动到(2, 1)
    line.end = Point(1, 2)      # 终点设置为(1, 2)
    print(line.length)          # 计算并打印出长度
    print(line)                 # 打印line所有信息
