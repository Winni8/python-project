# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/13 10:46
# @File 	:去掉弹框.py
# @Software :PyCharm

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://sh.xsjedu.org/")
sleep(3)
js = "document.getElementById('doyoo_monitor').style.display='none';"
driver.execute_script(js)
sleep(3)
driver.quit()
