# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/10 16:23
# @File 	:shunxu.py
# @Software :PyCharm

import unittest


class TestShunxu(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        print("1")

    def test_second(self):
        print("2")

    def test_thred(self):
        print("3")

    def test_four(self):
        print("4")

    def test_five(self):
        print("5")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([TestShunxu("test_one"), TestShunxu("test_five"),
                    TestShunxu("test_four"), TestShunxu("test_thred"),
                     TestShunxu("test_second")])

    runner = unittest.TextTestRunner(verbosity=2).run(suite)