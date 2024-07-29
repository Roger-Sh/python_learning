from math import sqrt
import pygame
import sys

import color as c


class Ball(object):

    def __init__(self, x, y, radius, sx, sy, color=c.Color.RED):
        """
        :param x:       初始坐标x
        :param y:       初始坐标y
        :param radius:  半径
        :param sx:      改变坐标sx
        :param sy:      改变坐标sy
        :param color:   颜色
        """

        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """move"""
        self.x += self.sx
        self.y += self.sy

        # 判断边缘，若超出边缘，则反方向弹回
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            # 解决球在边缘无法挣脱的bug
            if self.x - self.radius <= 0:
                self.x = self.radius
            else:
                self.x = screen.get_width() - self.radius
            # 设置速度为反方向
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            # 解决球在边缘无法挣脱的bug
            if self.y - self.radius <= 0:
                self.y = self.radius
            else:
                self.y = screen.get_height() - self.radius
            self.sy = -self.sy

    def eat(self, other):
        """eat"""
        if self.alive and other.alive and self != other:
            # distance between self and other
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)

            # 当发生碰撞，且self半径大于other半径
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.1)

                self.sx = -(self.sx * self.radius**2 + other.sx * other.radius**2)/(self.radius**2 + other.radius**2)
                self.sy = -(self.sy * self.radius**2 + other.sy * other.radius**2)/(self.radius**2 + other.radius**2)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


if __name__ == '__main__':
    pass
