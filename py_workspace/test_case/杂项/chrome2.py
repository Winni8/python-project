# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/11 15:47
# @File 	:chrome2.py
# @Software :PyCharm

from selenium import webdriver

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()

# 设置好应用扩展
from selenium import webdriver
option = webdriver.ChromeOptions()
# 设置成用户自己的数据目录
option.add_argument('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
driver = webdriver.Chrome(chrome_options=option)

# 启动浏览器
driver.get("https://www.baidu.com/")

