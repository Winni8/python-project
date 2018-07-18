# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 9:14
# @File 	:runfuben.py
# @Software :PyCharm

import unittest
from test_suite import suite_Test_report
from test_case.tests_report.Test_report import TestReport
import HTMLReport.HTMLReport
from public.SendEmail_Auto_Old import new_file,send_email
from public.SendEmail_Auto_New import new_file, send_email

if __name__ == '__main__':
    print("======start======")
    suite = unittest.TestSuite()
    # 方式一：不使用return函数
    suite.addTests([TestReport("test_d"), TestReport("test_b"), TestReport("test_a"), TestReport("test_c")])

    # 方式二：使用return函数
    # suite.addTest(suite_Test_report.return_suite())

    # 注意一点使用新版的测试形式发送邮件，由于在运行是就默认生成了测试报告，同时也会生成log日志，这里有个坑，就是要将
    # 两者分开，不然在使用jenkins中跑脚本的时候，发送的邮件会默认发送的是log文件，而不是html文件格式；
    # （目前不知道为啥在jenkins跑，发送的是log文件；只能避开；将测试报告与log文件分在两层目录中；）
    Log_path = "D:\\java\\Python\\py_workspace\\Log\\report"
    # report_paeh = "D:\\java\\Python\\py_workspace\\report\\report"
    HTMLReport.TestRunner(log_file_name=Log_path,
                          title="test_report",
                          description="用例情况",
                          thread_count=5).run(suite)

    # TODO 方式三： 使用老版的测试报告形式
    # 老版本测试报告也通过测试OK；
    # file_path = r"./report\\test_report.html"
    # fp = open(file_path, "wb")
    # runner = HTMLTestRunner1.HTMLTestRunner(stream=fp, title="testreport", description="用例情况").run(suite)
    # fp.close()

    # 发送邮件-测试报告；
    # 获取最新的测试报告，这种方式时发送试试更变的测试报告；
    test_report_dir = "report\\"
    new_repoet_path = new_file(test_report_dir)
    # 发送测试报告
    # new_repoet_path = "D:\\java\\Python\\py_workspace\\report\\report.html" # 这种方式时发送固定的测试报告；
    send_email(new_repoet_path)
    print("======end======")

# 真他妈不容易啊 终于成功发送最新的测试报告了，哈哈哈

