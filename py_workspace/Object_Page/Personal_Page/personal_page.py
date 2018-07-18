# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/9 10:21
# @File 	:login_page.py
# @Software :PyCharm

from selenium import webdriver


class PenCenterPage(object):

    def __init__(self, driver):

        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def center_email(self):
        return self.driver.find_element_by_xpath(".//*[@class='email']/span").text

    def center_address(self):
        self.driver.find_element_by_xpath(".//*[@id='js_saderBar']/ul/li[6]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='userMain']/header[2]/a[3]").click()

