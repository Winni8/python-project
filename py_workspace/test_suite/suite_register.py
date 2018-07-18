# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/4 8:45
# @File 	:suite_register.py
# @Software :PyCharm

import unittest
from test_web.RW.Register import Register


def retuen_register():
    suite = unittest.TestSuite()
    load = unittest.TestLoader().loadTestsFromTestCase(Register)
    suite.addTests(load)
    return suite
