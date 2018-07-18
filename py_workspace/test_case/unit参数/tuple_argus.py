# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/11 18:17
# @File 	:tuple_argus.py
# @Software :PyCharm
# 执行顺序不知道
import paramunittest
import unittest
import time


@paramunittest.parametrized(
    ("admin", "0", "true"),
    ("admin1", "1", "true"),
    ("admin3", "3", "true"),
    ("admin5", "5", "true"),
    ("admin6", "6", "true"),
    ("admin7", "7", "true"),
    ("admin8", "8", "true"),
    ("admin10", "10", "true"),
    ("admin11", "11", "true"),
    ("admin12", "12", "true"),
    ("admin12", "13", "true"),
    ("admin12", "22", "true"),
    ("admin12", "32", "true"),
    ("admin12", "01", "true")
)


class TestDemo(unittest.TestCase):
    def setParameters(self, user, psw, result):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.user = user
        self.user = psw
        self.result = result

    def testcase(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.user)
        print("期望结果：%s " % self.result)
        time.sleep(0.5)
        self.assertTrue(self.result == "true")


if __name__ == "__main__":
    unittest.main(verbosity=2)
