# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/13 10:27
# @File 	:获取联想词.py
# @Software :PyCharm

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("py")
eles = driver.find_elements_by_xpath(".//*[@id='form']/div/ul/li")
print(len(eles))
# 直接获取文本值
for i in eles:
    print(i.text)
# 通过属性获取值
for j in eles:
    print(j.get_attribute("data-key"))

if len(eles)>1:
    eles[1].click()

driver.back()