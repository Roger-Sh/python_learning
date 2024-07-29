"""
练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
"""

from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        """
        init constructor
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        move to point(x, y)
        :param x: new x coordinate
        :param y: new y coordinate
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        move by vector(dx, dy)
        :param dx:
        :param dy:
        :return:
        """
        self.x += dx
        self.y += dy

    def distance_to(self, point):
        """
        distance to another point
        :param x:
        :param y:
        :return:
        """
        dx = self.x - point.x
        dy = self.y - point.y
        distance = sqrt(dx ** 2 + dy ** 2)
        return distance

    def __str__(self):
        """
        return string when print this object
        :return:
        """
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()
