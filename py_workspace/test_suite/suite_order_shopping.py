# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/4 18:12
# @File 	:suite_order_shopping.py
# @Software :PyCharm
import unittest
from test_web.RW.Order_Shopping_PP import GetOrder


def return_order_shopping():
    suite = unittest.TestSuite()
    load = unittest.TestLoader().loadTestsFromTestCase(GetOrder)
    suite.addTests(load)

    return suite

