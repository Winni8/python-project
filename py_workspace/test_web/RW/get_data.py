# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/2 14:29
# @File 	:get_data.py
# @Software :PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.pc-rosewholesale.com.release.php5.egomsl.com/eload_admin/")
xpath = ""
ele = driver.find_elements_by_xpath(xpath)

file = open("data\\RW_data", "wb", encoding="utf-8")
for i in ele:
    file.write(i.taxt + "1")
    file.write("\n")

file.close()

# ============
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

ele = driver.find_elements_by_xpath(".//*[@id='u_sp']/a")
ele2 = driver.find_elements_by_css_selector(".mnav")
print(len(ele2))

# ======================
import unittest
from selenium import webdriver
import ddt
import time
import logging
from HTMLReport import AddImage, logger
from public.Read_data import read_text

baseurl = "http://login.pc-rosewholesale.com.v0621.php5.egomsl.com/m-users-a-sign.htm"
reg_email = "_o5hLT5L2@live.com"
password = "w7aTj4He"
driver = webdriver.Chrome()
driver.get(baseurl)
driver.implicitly_wait(30)

url11 = driver.current_url
print(url11)

driver.find_element_by_id("reg_email").send_keys(reg_email)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("password_confirm").send_keys(password)

driver.find_element_by_id("js_registBtn").click()
time.sleep(3)

url = driver.current_url
print(url)
