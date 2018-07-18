# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/12 9:44
# @File 	:RW网页抓取.py
# @Software :PyCharm

"商品抓取"

from selenium import webdriver
from public import Read_data

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.rosewholesale.com/cheap-online/jewelry-watches-c2/")
webdriver.ActionChains(driver).\
    move_to_element(driver.find_element_by_xpath(".//*[@id='js_cateTopBar']/div[5]/div[3]/div/span"))
driver.find_element_by_link_text("200").click()

eles = driver.find_elements_by_xpath(".//*[@id='js_proList']/ul/li/h3/a")
print(len(eles))
for i in eles:
    print(i.text)
# 包含三个参数，名称 ，颜色 ，参数类型（成功还是失败）
with open("data/rw_spdata1", "w", encoding='utf-8') as lf:
    for i in eles:
        lf.write(i.text+ "\n")


a = Read_data.read_text("data/rw_spdata1")


