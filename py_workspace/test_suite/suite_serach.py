# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/3 14:14
# @File 	:suite_serach.py
# @Software :PyCharm

import unittest
from test_web.RW.RW_search import TestSearch


def return_search():
    suite = unittest.TestSuite()
    load = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite.addTests(load)
    return suite

