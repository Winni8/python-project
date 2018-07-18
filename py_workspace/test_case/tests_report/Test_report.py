# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 9:46
# @File 	:Test_report.py
# @Software :PyCharm

import unittest


class TestReport(unittest.TestCase):

    def setUp(self):
        pass

    def test_a(self):
        a = 2
        b = 4
        self.assertNotEqual(a, b, "a不等于b则OK")

    def test_b(self):
        print("hello report")

    def test_c(self):
        c = "python"
        d = "where is the python ?,I'm here!"
        self.assertIsNot(c, d, "c在b中")

    def test_d(self):
        pass

    def tearDown(self):
        pass

