# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/12 15:25
# @File 	:report_new2.py
# @Software :PyCharm



"""
这种测试报告没有成功，不知道什么原因，怎么弄测试报告都没有生成，但是程序是跑完，也是OK的
但是就是没有成功。看来尝试了下，可视化的视图，最终以失败告终

"""

import unittest
from BeautifulReport import BeautifulReport
from public.Failrun import Suit
import HTMLTestRunner


class UnittestCaseSecond(unittest.TestCase, Suit):
    """ 测试代码生成与loader 测试数据"""

    def test_equal(self):
        """
            test 1==1
        :return:
        """
        import time
        time.sleep(1)
        self.assertTrue(1 == 1)

    @BeautifulReport.add_test_img('测试报告.png')
    def test_is_none(self):
        """
            test None object
        :return:
        """
        self.assertIsNone(None)

    def test_01(self):
        print("01")

    def test_02(self):
        print("02")

    def test_03(self):
        print("03")


if __name__ == '__main__':
    suit = Suit()

    suit.addtests(unittest.TestLoader().loadTestsFromTestCase(UnittestCaseSecond))

    fp = open("./aa", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,  title='android测试报告', description='用例执行情况:', )
    runner.run(suit)
