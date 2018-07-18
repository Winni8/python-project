# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/9 11:06
# @File 	:suite_batch_login.py
# @Software :PyCharm

from test_web.RW.Batch_Login import Test_Batchlogin
import unittest


def return_batchlogin():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Batchlogin))

    return suite
