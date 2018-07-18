# 这是新版本HTML生成的测试报告，测试通过OK
# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/28 9:41
# @File 	:SendEmail_Auto_New.py
# @Software :PyCharm

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from test_case.tests_report.Test_report import TestReport
import HTMLReport


# 2.定义：取最新测试报告
def new_file(report_path):
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(report_path)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(report_path + '\\' + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(report_path, lists[-1])
    #    L=file_path.split('\\')
    #    file_path='\\\\'.join(L)
    return file_path


# 3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):

    # 定义邮件对象
    msg = MIMEMultipart()

    # 定义邮件的主题
    current = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    subject = "测试邮件发送" + current
    msg['Subject'] = Header(subject, 'utf-8')

    # 打开文件,并获取文章内容
    text_report = open(newfile, 'rb').read()
    msg_text = MIMEText(text_report, "html", "utf-8")
    msg.attach(msg_text)

    # 添加邮件附件

    smtpserver = 'smtp.163.com'  # 设置smtp服务器

    sender = "c2694571567@163.com"  # 发送人
    receiver = "2694571567@qq.com"  # 接受者

    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    # receiver=['XXX@126.com','XXX@126.com','XXX@doov.com.cn']

    username = 'c2694571567@163.com'  # 用户登陆名
    password = '123456adc'  # 用户授权码

    # 注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
    #    text = "Dear all!\nThe attachment is new testreport.\nPlease check it."
    # 中文测试ok
    #    text = "Dear all!\n附件是最新的测试报告。\n麻烦下载下来看，用火狐浏览器打开查看。\n请知悉，谢谢。"
    #    msg_plain = MIMEText(text,'plain', 'utf-8')
    #    msg.attach(msg_plain)

    # 要加上msg['From']这句话，否则会报554的错误。
    # 要在163有限设置授权码（即客户端的密码），否则会报535
    msg['From'] = 'Tim<c2694571567@163.com>'
    msg['To'] = "Win7<2694571567@qq.com>"
    # 多个收件人
    # msg['To'] = ";".join(receiver)

    # 连接发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        print("邮件发送success")
    except smtplib.SMTPException as e:
        print("邮件发送failure", e)
    finally:
        smtp.close()


# if __name__ == '__main__':
#     print('=====AutoTest Start======')
#
#     # 1.新版的测试报告执行的时候就已经生成了；不需要再生成，同时只需要获取最想的测试报告发送即可；
#     suite = unittest.TestSuite()
#     suite.addTests([TestReport("test_a"), TestReport("test_b"), TestReport("test_c"), TestReport("test_d")])
#     runner = HTMLReport.TestRunner(report_file_name="report",
#                                    title="test-report",
#                                    description="执行用例的情况")
#     runner.run(suite)
#
#     # # 2.取最新测试报告
#     # test_report_dir = "D:\\java\\Python\\py_workspace\\report\\"
#     # new_report = new_file(test_report_dir)
#     # # print(new_report) 调试用的
#     #
#     # # 3.发送邮件，发送最新测试报告html
#     # send_email(str(new_report))
#     print('=====AutoTest Over======')
