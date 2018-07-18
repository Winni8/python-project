# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/3 18:39
# @File 	:Register.py
# @Software :PyCharm

import unittest
from selenium import webdriver
import ddt
import time
import logging
from HTMLReport import AddImage, logger
from public.Read_data import read_text
from selenium.webdriver import DesiredCapabilities


baseurl = "http://login.pc-rosewholesale.com.release.php5.egomsl.com/m-users-a-sign.htm"
log = logging.getLogger(__name__) # 写入日志文件，报告中则不包含


@ddt.ddt
class Register(unittest.TestCase):

    def setUp(self):

        # 不使用多线程，
        # self.driver = webdriver.Chrome()
        # self.driver.get(baseurl)
        # self.driver.implicitly_wait(30)
        # #self.driver.maximize_window()

        # 使用多线程：
        log.info("日志记录！！！！！")
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )  # 若hub就部署在本机上，直接用http://127.0.0.1:4444/wd/hub即可，若非部署在本机上，则需填写hub的IP地址
        logger().info("打开浏览器")  # 在报告中写入流程记录
        self.driver.get(baseurl)
        self.driver.implicitly_wait(120)
        # self.driver.maximize_window()
        # logger().info("浏览器最大化")

    def tearDown(self):
        AddImage(self.driver.get_screenshot_as_base64())
        self.driver.quit()

    @ddt.data(*read_text("D:\java\Python\py_workspace\data\Register.txt"))
    @ddt.unpack
    def test_02(self, reg_email, password):
        "注册操作"
        # 注册模块：测试用的
        # reg_email = "er229ia707ow@outlook.com"
        # password = "2ITwoZve"
        reg_email = str(reg_email)
        driver = self.driver
        print(driver.current_url)
        driver.find_element_by_id("reg_email").send_keys(reg_email)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("password_confirm").send_keys(password)

        # 勾选协议,此处默认勾选了
        # driver.find_element_by_xpath(".//*[@id='agreement']").click()

        # 点击登录
        driver.find_element_by_id("js_registBtn").click()
        time.sleep(5)
        AddImage(driver.get_screenshot_as_base64())
        time.sleep(3)

        # 进入个人中心
        # action = driver.find_element_by_class_name("nam")
        # ActionChains(driver).move_to_element(action).perform()
        # driver.find_element_by_link_text("My R Points").click()
        # text = driver.find_element_by_xpath(".//*[@class='email']/span")

        try:
            self.assertIn("m-promotion-active-151.html", driver.current_url)
            print(driver.current_url)
            logger().info("注册OK")
        except AssertionError as e:
            logger().info("注册失败", e)


if __name__ == '__main__':
    unittest.main()


