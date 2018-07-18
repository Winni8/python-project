# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/13 8:58
# @File 	:alert1.py
# @Software :PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("D:\java\Python\py_workspace\data\Various_alert.html")
# alert
driver.find_element_by_id("alert").click()
t = driver.switch_to.alert
print(t.text)
t.accept()
t.dismiss()

# confirm
driver.find_element_by_id("confirm").click()
a = driver.switch_to.alert
print(a.text)
a.dismiss()
a.accept()

# prompt
driver.find_element_by_id("prompt").click()
b = driver.switch_to.alert
print(b.text)
b.accept()
b.dismiss()
b.send_keys("hello cjj")
driver.back()
driver.refresh()




