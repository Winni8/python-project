# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/2 15:52
# @File 	:RW_search.py
# @Software :PyCharm

import unittest
from HTMLReport import AddImage, logger
import logging
from ddt import ddt, data, unpack
from public import Read_data
from selenium.webdriver.common.keys import Keys
import time
from RW_Common.common_driver import Driver

baseurl = "https://www.rosewholesale.com/"
log = logging.getLogger(__name__)  # 写入日志文件，报告中则不包含


@ddt
class TestSearch(unittest.TestCase, Driver):
    def setUp(self):
        log.info("日志记录！！！！！")
        self.remote_driver()

    def tearDown(self):
        AddImage(self.driver.get_screenshot_as_base64())
        logger().info("退出浏览器")
        self.driver.quit()

    @data(*Read_data.read_text("data/rw_spdata1"))
    @unpack
    def test_search(self, titlt, color, type):
        driver = self.driver
        driver.get(baseurl)
        self.assertIn("Wholesale", driver.title)
        driver.find_element_by_xpath(".//*[@id='xubox_layer1']/div/div/div/a").click()
        element = driver.find_element_by_id("js_topSearch")
        element.send_keys(titlt)
        element.send_keys(Keys.ENTER)
        logger().info(titlt, color)
        AddImage(driver.get_screenshot_as_base64())

        if type == "1":
            try:
                xpath = ".//*[@class='proList clearfix mt40 w1000']//h3/a"
                element = self.driver.find_element_by_xpath(xpath)
                something_title = element.text
                self.assertIn(titlt, something_title)
                logger().info("搜素商品OK")
            except AssertionError as e:
                xpath = './/*[@class="no_goods"]/div[2]'
                element = self.driver.find_element_by_xpath(xpath)
                self.assertIn("Sorry", element.text)
                logger().info("搜素的商品不存在", e)
