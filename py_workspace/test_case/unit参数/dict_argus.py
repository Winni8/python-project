# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/11 17:59
# @File 	:dict_argus.py
# @Software :PyCharm
"""
注意执行顺序,不知道；
"""

import paramunittest
import unittest
import time


@paramunittest.parametrized(
    {"user": "admin", "psw": "0", "result": "true"},
    {"user": "admin1", "psw": "12", "result": "true"},
    {"user": "admin2", "psw": "2", "result": "true"},
    {"user": "admin3", "psw": "3", "result": "true"},
    {"user": "admin4", "psw": "4", "result": "true"},
    {"user": "admin5", "psw": "5", "result": "true"},
    {"user": "admin6", "psw": "6", "result": "true"},
    {"user": "admin7", "psw": "7", "result": "true"},
    {"user": "admin8", "psw": "8", "result": "true"},
    {"user": "admin9", "psw": "9", "result": "true"},
    {"user": "admin10", "psw": "10", "result": "true"},
    {"user": "admin11", "psw": "11", "result": "true"},
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
