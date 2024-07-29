"""
在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，
如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
"""

"""
在实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问（后面会讲到）。
所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
本类之外的代码在访问这样的属性时应该要保持慎重。这种做法并不是语法上的规则，
单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻，
关于这一点可以看看我的《Python - 那些年我们踩过的那些坑》文章中的讲解。
"""


class Test:
    # private attribute 私有属性
    def __init__(self, foo):
        self.__foo = foo            # __foo, private variable

    # private attribute
    def __bar(self):                # __bar, private method
        print(self.__foo)
        print('__bar')

    # like-private attribute, 类私有属性，实际上可以访问, 单下划线开头
    def _test(self):
        print("It's not a private attribute, so you can access it, but better not")


def main():
    # generate a new instance of Test
    test = Test('hello')

    # 无法直接访问 __ 开头的变量或方法，他们是私有变量和私有方法
    # test.__bar()            # AttributeError: 'Test' object has no attribute '__bar'
    # print(test.__foo)       # AttributeError: 'Test' object has no attribute '__foo'

    # 通过改写私有变量和私有方法的名字，在前面加上 _类名 即可
    test._Test__bar()
    print(test._Test__foo)

    # 单下划线的属性可以访问，但建议不要
    test._test()


if __name__ == "__main__":
    main()
