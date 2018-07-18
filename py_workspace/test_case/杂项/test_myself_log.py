# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 16:35
# @File 	:test_myself_log.py
# @Software :PyCharm

import unittest
from HTMLReport import AddImage, logger
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.rosewholesale.com/")
driver.maximize_window()
print(driver.title)
driver.find_element_by_xpath(".//*[@id='xubox_layer1']/div/div/div/a").click()
# 把页面移到又下角点击android按钮
scroll_to_end = 'window.scrollTo(0, document.body.scrollHeight);'
driver.execute_script(scroll_to_end)
time.sleep(3)
# js_blank = "document.getElementsByClassName('icon-box')[1].target='';"
# driver.execute_script(js_blank)
driver.find_element_by_xpath(".//*[@class='app-icon-box clearfix']/a[2]").click()
time.sleep(3)
AddImage(driver.get_screenshot_as_base64())
# 切换句柄
cut_handle = driver.current_window_handle
all_handles = driver.window_handles

for h_andriod in all_handles:
    if h_andriod != cut_handle:
        driver.switch_to.window(h_andriod)
time.sleep(3)
AddImage(driver.get_screenshot_as_base64(), name='跳转安卓截图')
try:
    if "应用" in driver.title:
        logger().info("android 跳转成功")
except AssertionError as e:
        logger().info("点击android跳转失败", e)
driver.back()

print(driver.current_url)
driver.refresh()

# ================================================

import unittest
from HTMLReport import AddImage, logger
# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com/")
# cut_h = driver.current_window_handle
#
# driver.find_element_by_link_text("hao123").click()
# print(driver.title)
# driver.back()
# print(driver.title)

