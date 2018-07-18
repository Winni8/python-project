# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/3 18:38
# @File 	:Login.py
# @Software :PyCharm

from selenium import webdriver
import unittest
from HTMLReport import AddImage, logger
import logging
from Object_Page.Login_Page.login_page import Test_Loginpage
from RW_Common.common_driver import Driver
from Object_Page.Personal_Page.personal_page import PenCenterPage

baseurl = "http://login.pc-rosewholesale.com.release.php5.egomsl.com/m-users-a-sign.htm"
log = logging.getLogger(__name__)  # 写入日志文件，报告中则不包含


class LoginTest(unittest.TestCase, Test_Loginpage, Driver, PenCenterPage):

    def setUp(self):
        log.info("日志记录")
        # self.driver = webdriver.Chrome()
        # self.driver.get(baseurl)
        # self.driver.implicitly_wait(30)
        # logger().info("窗口最大化")
        # self.driver.maximize_window()
        self.local_driver()

    def tearDown(self):
        AddImage(self.driver.get_screenshot_as_base64())
        self.driver.quit()

    def test_login(self):
        self.driver.get(baseurl)
        name = "2694571567@qq.com"
        pwd = "123456"
        type1 = 1
        if type1 == 1:
            try:
                self.login_operation(name, pwd)
                self.assertIn(name, self.center_email())
                logger().info("登陆成功")
            except:
                logger().info("登录失败")

        #driver = self.driver
        # email = "2694571567@qq.com"
        # pwd = "123456"
        #
        # # 登陆
        # driver.find_element_by_id("email").clear()
        # driver.find_element_by_id("email").send_keys(email)
        #
        # driver.find_element_by_id("passwordsign").clear()
        # driver.find_element_by_id("passwordsign").send_keys(pwd)
        # AddImage(driver.get_screenshot_as_base64())
        #
        # driver.find_element_by_id("js_signInBtn").click()

        # 断言是否登陆成功
        #
        #
        # ele = driver.find_element_by_xpath(".//*[@class='email']/span")
        # ele_text = ele.text
        #
        # try:
        #     self.assertIn(email, ele_text)
        #     logger().info("登陆成功")
        # except AssertionError as e:
        #     logger().info("登陆失败", e)


if __name__ == '__main__':
    unittest.main()



