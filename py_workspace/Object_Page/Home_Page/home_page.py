# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/9 10:21
# @File 	:login_page.py
# @Software :PyCharm
from selenium import webdriver


class Home_Operation(object):

    def __init__(self, driver):

        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def click_tankuang(self):
        xpath = ".//*[@id='xubox_layer1']/div/div/div/a"
        self.driver.find_element_by_xpath(xpath).click()
        self.driver.find_element_by_xpath(".//*[@class='sign_box']/a[2]").click()
