# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/2 15:52
# @File 	:RW_search.py
# @Software :PyCharm

import unittest
from selenium import webdriver
from HTMLReport import AddImage, logger
import logging
from ddt import ddt, data, unpack
from public import Read_data
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import time


log = logging.getLogger(__name__)  # 写入日志文件，报告中则不包含


@ddt
class TestSearch(unittest.TestCase):
    def setUp(self):
        log.info("日志记录！！！！！")
        self.driver = webdriver.Remote(
            command_executor='http://10.32.1.191:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )   # 若hub就部署在本机上，直接用http://127.0.0.1:4444/wd/hub即可，若非部署在本机上，则需填写hub的IP地址
        logger().info("打开浏览器")  # 在报告中写入流程记录
        self.driver.implicitly_wait(20)
        # self.driver.maximize_window()
        logger().info("浏览器最大化")

    def tearDown(self):
        AddImage(self.driver.get_screenshot_as_base64())
        logger().info("退出浏览器")
        self.driver.quit()

    path = "D:\\java\\Python\\py_workspace\\data\\RW_data.txt"
    a = Read_data.read_text(path)

    @data(*a)
    @unpack
    def test_search(self, something, type):
        driver = self.driver
        driver.get("http://www.pc-rosewholesale.com.release.php5.egomsl.com/")
        self.assertIn("Wholesale", driver.title)
        driver.find_element_by_xpath(".//*[@id='xubox_layer1']/div/div/div/a").click()
        element = driver.find_element_by_id("js_topSearch")
        element.send_keys(something)
        element.send_keys(Keys.ENTER)
        AddImage(driver.get_screenshot_as_base64())

        if type == "1":
            xpath = './/*[@id="mainWrap"]/section/div[3]/ul/li/h3/a'
            element = self.driver.find_element_by_xpath(xpath)
            something_title = element.text
            self.assertIn(something, something_title)
        elif type == "2":
            xpath = './/*[@class="no_goods"]/div[2]'
            element = self.driver.find_element_by_xpath(xpath)
            self.assertIn("Sorry", element.text)
