# coding=utf-8
import unittest
from BeautifulReport import BeautifulReport
import os
from tomorrow import threads

"""
这种测试报告没有成功，不知道什么原因，怎么弄测试报告都没有生成，但是程序是跑完，也是OK的
但是就是没有成功。看来尝试了下，可视化的视图，最终以失败告终;草，不搞了，浪费时间

"""

# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, "test_case/tests_report/")
if not os.path.exists(casepath):
    print("测试用例需放到‘case’文件目录下")
    os.mkdir(casepath)
reportpath = os.path.join(curpath, "report020")
if not os.path.exists(reportpath): os.mkdir(reportpath)


def add_case(case_path=casepath, rule="test*.py"):
    '''加载所有的测试用例'''
    dir = "test_case/tests_report/report_new2.py"
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


@threads(3)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='reportaa.html', description='测试deafult报告', log_path='reportbb')


if __name__ == "__main__":

    # 用例集合
    cases = add_case()

    print(cases)
    for i in cases:
        print(i)
        run(i)