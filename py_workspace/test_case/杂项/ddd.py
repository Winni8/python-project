# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/4 17:04
# @File 	:ddd.py
# @Software :PyCharm

import unittest
from selenium import webdriver

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.cnblogs.com/Winni8/")

driver.close()  # close这句报错了