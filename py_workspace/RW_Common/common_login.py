# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/9 10:58
# @File 	:common_login.py
# @Software :PyCharm
from Object_Page.Login_Page.login_page import Test_Loginpage
from Object_Page.Home_Page.home_page import Home_Operation
from Object_Page.Personal_Page.personal_page import PenCenterPage


def test_rwlogin(name, pwd):
    Home_Operation.click_tankuang()
    Test_Loginpage.login_operation(name, pwd)


def test_rwregiter(self, reg_email, password):
    Home_Operation.click_tankuang(self)
    Test_Loginpage.register_opreation(self, reg_email, password)


def test_cen():
    PenCenterPage.center_email()


