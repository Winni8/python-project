# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/10 17:07
# @File 	:suite_public.py
# @Software :PyCharm
"""
将测试用例封装与这个public中，只用改这个文件即可；run.py文件将不再不要动
"""
import unittest
from test_web.RW.Batch_seach import TestSearch
from test_case.tests_report.report_new import Testaa


def return_public():
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSearch))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Testaa))
    return suite
