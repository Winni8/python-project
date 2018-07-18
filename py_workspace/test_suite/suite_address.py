# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/7 14:16
# @File 	:suite_address.py
# @Software :PyCharm

import unittest
from test_web.RW.Address import TestAddress


def return_address():
    suite = unittest.TestSuite()
    load = unittest.TestLoader().loadTestsFromTestCase(TestAddress)
    suite.addTests(load)

    return suite
