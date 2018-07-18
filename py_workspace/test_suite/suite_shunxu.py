# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/10 16:29
# @File 	:suite_shunxu.py
# @Software :PyCharm

from test_case.杂项.shunxu import TestShunxu
import unittest


def re_shunxu():
    suite = unittest.TestSuite()
    suite.addTests([TestShunxu("test_four"), TestShunxu("test_five"),
                    TestShunxu("test_one"), TestShunxu("test_thred"),TestShunxu("test_second")])
    return suite
