# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 14:09
# @File 	:SendEmail.py
# @Software :PyCharm
# 这是测试报告路径不变的情况下；这种模式基本上用的不多
import unittest
import HTMLReport
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time


class EmailReport(unittest.TestCase):  # 这个仅仅是将生成的测试报告发送给指定用户；

    def setUp(self):
        pass

    def test_sendemail(self):
        smtpserver = 'smtp.163.com'  # 设置smtp服务器

        sender = "c2694571567@163.com"  # 发送人
        receiver = "2694571567@qq.com"  # 接受者

        username = 'c2694571567@163.com'  # 用户登陆名
        password = '123456adc'  # 用户授权码

        current = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        subject = "测试邮件发送" + current

        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')

        # 文章内容
        text_report = open("路径", encoding="utf-8").read()
        msg_text = MIMEText(text_report, "html", "utf-8")
        msg.attach(msg_text)

        msg['From'] = 'Tim<c2694571567@163.com>'
        msg['To'] = "Win7<2694571567@qq.com>"

        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()

    def tearDown(self):
        pass
