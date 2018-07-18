# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 14:11
# @File 	:ScreenShot.py
# @Software :PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.twinkledeals.com/")
#
png_path = r"D:\java\Python\py_workspace\data\picture\\a.png"
driver.save_screenshot(png_path)
#
c = driver.get_screenshot_as_file("D:\java\Python\py_workspace\data\picture\\b.png")

b = driver.get_screenshot_as_png()
print(b)
a = driver.get_screenshot_as_base64()
print(a)
