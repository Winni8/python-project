# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/6 11:58
# @File 	:suite_order_wp.py
# @Software :PyCharm

import unittest
from test_web.RW.Order_Shopping_WP import GetOrderWp


def return_wp():
    suite = unittest.TestSuite()
    load = unittest.TestLoader().loadTestsFromTestCase(GetOrderWp)
    suite.addTests(load)

    return suite
