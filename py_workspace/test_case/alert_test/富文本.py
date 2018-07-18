# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/13 9:55
# @File 	:富文本.py
# @Software :PyCharm
# 测试OK
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

file_path = r"C:\Users\chenjingjian\AppData\Roaming\Mozilla\Firefox\Profiles\jzf6o3ct.default-1524801335999"
profile = webdriver.FirefoxProfile(file_path)
driver = webdriver.Firefox(profile)
driver.implicitly_wait(30)
driver.get("http://www.cnblogs.com/Winni8/")
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(5)
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys("hello winni8")

driver.switch_to.frame("Editor_Edit_EditorBody_ifr")   # 通过id切过去

# 编辑正文

ele = driver.find_element_by_id("tinymce")
ele.send_keys(Keys.TAB)
ele.send_keys("自动化富文本测试")
driver.switch_to.default_content()
driver.find_element_by_id("Editor_Edit_lkbDraft").click()

driver.quit()

