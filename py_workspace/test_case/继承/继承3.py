# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/10 14:12
# @File 	:继承3.py
# @Software :PyCharm

class A():
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        super().__init__()
        print("B")


class C(A):
    def __init__(self):
        #super().__init__()
        print("C")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")
d = D()
print(C.mro())

# 因为D的关系，导致B是继承C的，用关键字super可以看出来，B的对象继承父类的方法，输出的是C；

