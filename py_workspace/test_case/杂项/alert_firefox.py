# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/11 14:49
# @File 	:alert_chrome.py
# @Software :PyCharm
"chrome OK的， 但是firefox失败，晕死"

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
driver.refresh()
mouse = WebDriverWait(driver, 10).until(lambda x: x.find_element("link text", "设置"))
ActionChains(driver).move_to_element(mouse).perform()
WebDriverWait(driver, 10).until(lambda x: x.find_element("link text", "搜索设置")).click()

# 选择设置项
s = WebDriverWait(driver, 10).until(lambda x: x.find_element("id", "nr"))
Select(s).select_by_visible_text("每页显示50条")

# 点保存按钮
js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)

# 判断弹窗结果
result = EC.alert_is_present()(driver)
if result:
    print(result.text)
    result.accept()
else:
    print("alert 未弹出！")
