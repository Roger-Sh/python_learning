"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""


class A(object):

    def foo(self):
        print('foo of A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo of C')


class D(B, C):
    def test(self):
        super(B, self).foo()        # foo of C
        super(C, self).foo()        # foo of A
    # pass


class E(D):

    def foo(self):
        print('foo in E')        # foo in E
        super().foo()            # foo of C           # D.foo() ==> C.foo()
        super(B, self).foo()     # foo of C           # A.foo() ==>(override) C.foo()
        super(C, self).foo()     # foo of A           # A.foo()


if __name__ == '__main__':
    d = D()
    d.foo()
    print("=========")

    e = E()
    e.foo()
    print("=========")

    d = D()
    d.test()