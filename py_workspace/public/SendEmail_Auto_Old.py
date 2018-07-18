# 这是老版本HTML生成的测试报告，测试通过OK

# coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from test_case import TestReport


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
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    print('=====AutoTest Start======')
    # 1.执行测试用例，生成最新的测试用例
    # 指定测试用例为当前文件夹下的test_case目录
    # 如果用/可以不用r
    #    test_dir='./test_case'
    # Windows的cmd执行：python "D:\system files\workspace\selenium\test_project\runtest_htmltestrunner_autosendemail.py"
    # 不用绝对路径会报：ImportError: Start directory is not importable: './test_case'
    # report_path = 'D:\\system files\\workspace\\selenium\\test_project\\test_case'
    # 知道测试报告的路径

    test_report_dir = 'D:\\java\\Python\\py_workspace\\report'
    suite = unittest.TestSuite()
    suite.addTests([TestReport("test_a"), TestReport("test_b"), TestReport("test_c"), TestReport("test_d")])

    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(suite)
    fp.close()

    # 2.生成的测试报告存放于这个路径，遍历集合取最新测试报告
    test_report_dir = "D:\\java\\Python\\py_workspace\\report\\"
    new_report = new_file(test_report_dir)
    # print(new_report) 调试用的
    # 调试用的

    # 3.发送邮件，发送最新测试报告html
    send_email(str(new_report))
    print('=====AutoTest Over======')
