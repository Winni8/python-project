# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/9 10:59
# @File 	:common_driver.py
# @Software :PyCharm
from selenium import webdriver
from HTMLReport import AddImage, logger
from selenium.webdriver import DesiredCapabilities


class Driver(object):
    def local_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
        logger().info("窗口最大化")

    def remote_driver(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )  # 若hub就部署在本机上，直接用http://127.0.0.1:4444/wd/hub即可，若非部署在本机上，则需填写hub的IP地址
        logger().info("打开浏览器")  # 在报告中写入流程记录
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()
        logger().info("浏览器最大化")


