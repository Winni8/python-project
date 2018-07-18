# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/12 14:14
# @File 	:run_old.py
# @Software :PyCharm

"""这个旧试的测试报告，里面没有包含截图，同时生成的测试报告，
没有带日志的，若果想生成日志，则只能自己定义一个log模式，文件输出与控制的的输出必须自己定义
这种形式很老了，个人不喜欢使用，同时生成的测试报告巨丑无比；
"""

import unittest
from test_suite.suite_public import return_public
import HTMLTestRunner
from public.SendEmail_Auto_New import new_file, send_email

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(return_public())
    # 测试报告的路径
    file_path = "./report//testreport.html"
    fp = open(file_path, "wb")
    HTMLTestRunner.HTMLTestRunner(stream=fp,
                                  title="repore title",
                                  description="用例情况",
                                  verbosity=2).run(suite)

    # 获取最新的测试报告
    # path = 'report/report.html'
    # new_path = new_file(path)

    # 发送测试报告

    new_path = "report/testreport.html"
    send_email(new_path)


