# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/4 15:05
# @File 	:suite_login.py
# @Software :PyCharm

import unittest
from test_web.RW.Login import LoginTest


def return_login():
    suite = unittest.TestSuite()
    suite.addTests([LoginTest("test_login")])

    return suite


