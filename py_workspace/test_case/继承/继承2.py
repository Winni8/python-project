# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/10 11:37
# @File 	:继承2.py
# @Software :PyCharm
class X(object):
    def f(self):
        print( 'x')


class A(X):
    def f(self):
        super(A, self).f()
        print( 'a')


class B(X):
    def f(self):
        super(B, self).f()
        print( 'b')


class C(A, B, X):
    def f(self):
        super(C, self).f()
        print( 'c')


class F(X):
    def f(self):
        super().f()
        print("f")


class D(C,F):
    def f(self):
        super(D, self).f()
        print("d")


d = D()
print(D.mro())
d.f()

# c = C()
# c.f()
#c.extral()
