# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/13 15:13
# @File 	:爬虫页面源码.py
# @Software :PyCharm

from selenium import webdriver
import re

file_path = r"C:\Users\chenjingjian\AppData\Roaming\Mozilla\Firefox\Profiles\jzf6o3ct.default-1524801335999"
profile = webdriver.FirefoxProfile(file_path)
driver = webdriver.Firefox(profile)
driver.get("http://www.cnblogs.com/Winni8/")
print(driver.page_source)

#  re非贪婪模式刷选可用的；
page = driver.page_source
url_list = re.findall('href=\"(.*?)\"', page, re.S)
url_all = []
for url in url_list:
    if "http and Winni8 " in url:
        print(url)
        url_all.append(url)
print(url_all)

