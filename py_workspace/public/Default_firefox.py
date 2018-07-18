# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/11 15:10
# @File 	:Default_firefox.py
# @Software :PyCharm

from selenium import webdriver
import time


class Default_ff():
    def default_firefox(self):
        # 在 Firefox 地址栏输入 about:profiles 并选择下列选项：copy根目录就行
        file_path = r"C:\Users\chenjingjian\AppData\Roaming\Mozilla\Firefox\Profiles\jzf6o3ct.default-1524801335999"
        profile = webdriver.FirefoxProfile(file_path)
        self.driver = webdriver.Firefox(profile)



