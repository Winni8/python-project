# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/9 10:21
# @File 	:login_page.py
# @Software :PyCharm
from selenium import webdriver


class Test_Loginpage(object):

    def __init__(self, driver):

        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def login_operation(self, name, pwd):

        # 用户名
        ele1 = self.driver.find_element_by_id("email")
        ele1.clear()
        ele1.send_keys(name)

        # 密码
        ele2 = self.driver.find_element_by_id("passwordsign")
        ele2.clear()
        ele2.send_keys(pwd)

        # 点击登陆
        self.driver.find_element_by_id("js_signInBtn").click()

    def register_opreation(self, reg_email, password):
        reg_email = str(reg_email)
        self.driver.find_element_by_id("reg_email").send_keys(reg_email)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password_confirm").send_keys(password)
        self.driver.find_element_by_id("js_registBtn").click()  # 点击注册按钮

    def login_mark0(self):
        "用户名或者密码错误提示语"
        ele = self.driver.find_element_by_xpath(".//*[@id='mainWrap']//section[1]/div/p")
        return ele.text

    def login_mark1(self):
        "用户名空的提示语"
        ele = self.driver.find_element_by_xpath(".//*[@id='signinform']/div[1]/div/label")
        return ele.text

    def login_mark2(self):
        "密码小于6位或者名空的提示语"
        ele = self.driver.find_element_by_xpath(".//*[@id='signinform']/div[2]/label[2]")
        return ele.text
