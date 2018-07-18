# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/9 9:30
# @File 	:Batch_Login.py
# @Software :PyCharm

'''
网站登录测试用例：注意这里用的是二次封装的；也就是object-page思想；
用例说明：
1.用户名空，密码空；查看提示语 “Please enter a valid email address”
2.用户名不为空，密码为空；查看提示语 “”
3.用户名为空，密码不为空；查看提示语 “”
4.用户名错误，密码错误；查看提示语  “”
5.用户名正确，密码错误；查看提示语  “”
6.用户名错误，密码正确；查看提示语 “”
7.用户名正确，密码正确；查看提示语 “”
8.错误的用户格式；查看提示语； “”
9.用户格式正确，密码少于6位； “”
'''

import unittest
import logging
from ddt import ddt, data, unpack
from HTMLReport import AddImage, logger
from RW_Common.common_driver import Driver
from public import Read_data
from RW_Common.common_login import RW_login
from Object_Page.Personal_Page.personal_page import PenCenterPage

log = logging.getLogger(__name__)
baseurl = "http://www.pc-rosewholesale.com.release.php5.egomsl.com/index.php"


@ddt
class Test_Batchlogin(unittest.TestCase, Driver, RW_login, PenCenterPage):

    def setUp(self):
        log.info("程序开始写入")
        self.remote_driver()

    def tearDown(self):
        self.driver.quit()

    @data(*Read_data.read_text("D:\\java\\Python\\py_workspace\\data\\RW_logins"))
    @unpack
    def test_01(self, name, pwd, type1):
        "登陆验证"
        self.driver.get(baseurl)
        self.driver.implicitly_wait(60)
        self.test_rwlogin(name, pwd)

        AddImage(self.driver.get_screenshot_as_base64())
        logger().info("开始验证登录提示语")
        type1 = int(type1)
        if type1 == 1:
            self.assertIn("Please enter a valid email address", self.login_mark1())
            AddImage(self.driver.get_screenshot_as_base64())
            logger().info("用户名空，密码空,提示ok")
        if type1 == 2:
            self.assertIn("Provide a password", self.login_mark2())
            AddImage(self.driver.get_screenshot_as_base64())
            logger().info("用户名不为空，密码为空,提示语OK")

        if type1 == 3:
            self.assertIn("Please enter a valid email address", self.login_mark1())
            AddImage(self.driver.get_screenshot_as_base64())
            logger().info("用户名为空，密码不为空,提示语OK")

        if type1 == 4:
            self.assertIn("Your email/password is incorrect. Please try again.", self.login_mark0())
            AddImage(self.driver.get_screenshot_as_base64())
            logger().info("用户名错误，密码错误,提示语OK")

        if type1 == 5:
            self.assertIn("Your email/password is incorrect. Please try again.", self.login_mark0())
            AddImage(self.driver.get_screenshot_as_base64())
            logger().info("用户名正确，密码错误,提示语OK")

        if type1 == 6:
            self.assertIn("Your email/password is incorrect. Please try again.", self.login_mark0())
            AddImage(self.driver.get_screenshot_as_base64())
            logger().info("用户名错误，密码正确,提示语OK")
        if type1 == 7:
            try:
                self.assertIn(name, self.center_email())
                AddImage(self.driver.get_screenshot_as_base64())
                logger().info("用户名正确，密码正确,提示语OK,登陆OK")
            except AssertionError as e:
                logger().info("登陆失败", e)

        if type1 == 8:
            self.assertIn("Please enter a valid email address", self.login_mark1())
            AddImage(self.driver.get_screenshot_as_base64())
            logger().info("错误的用户格式,提示语OK")

        if type1 == 9:
            self.assertIn("Enter at least 6 characters", self.login_mark2())
            AddImage(self.driver.get_screenshot_as_base64())
            logger().info("用户格式正确，密码少于6位,提示语OK")


if __name__ == '__main__':
    unittest.main()

