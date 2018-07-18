# # _*_ coding：utf-8 _*_
# # @Author    :cjj
# # @time		 :2018/6/22 14:21
# # @File 	 :test.py
# # @Software  :PyCharm
# # from selenium import webdriver
# # import time
# # import pdb
# #
# # driver = webdriver.Firefox()
# # pdb.set_trace()
# #
# # driver.get("https://www.baidu.com/")
# # time.sleep(3)
# #
# # print("打开百度链接")
# # # driver.quit()
#
# # ================================================
#
# # import pdb
# # pdb.set_trace()
# # a = "aaa"
# # b = "bbb"
# # c = "ccc"
# # final = a + b + c
# # print(final)
#
# # ==================================================
# # coding:utf-8
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.select import Select
# import time
# import pdb
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com")
# driver.implicitly_wait(30)
# time.sleep(5)
# # .set_trace()
# mouse = driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(mouse).perform()
# time.sleep(3)
# driver.find_element_by_link_text("搜索设置").click()
# time.sleep(3)
# s = driver.find_element_by_id("nr")
# Select(s).select_by_visible_text("每页显示50条")
# # 方法一，先点击父元素
# # driver.find_element_by_id("gxszButton").click()
# # driver.find_element_by_class_name("prefpanelgo").click()
# # 方法二，JS直接点击
# js = 'document.getElementsByClassName("prefpanelgo")[0].click()'
# driver.execute_script(js)
#
# driver.switch_to.alert.accept()
# print("OK")
# driver.quit()

# ======================================
# 数据驱动

# from selenium import webdriver
# import os, time
#
# source = open("D:\\java\\Python\\py_workspace\\test_case\\data1")
# values = source.readlines()
# source.close()
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
#
# for val in values:
#     driver.find_element_by_id("kw").clear()
#     driver.find_element_by_id("kw").send_keys(val)
#     driver.find_element_by_id("su").click()
#     time.sleep(3)
#
# driver.quit()
# =============================================================
import csv
import xlrd

# file1 = xlrd.open_workbook(r"C:\\Users\\chenjingjian\\Desktop\\coupon_template (3).xls")
# data = file1.sheet_by_name("Sheet2")
# print(data.name)
#
# print(data.cell(2, 3).value)
# print(data.cell_value(1, 1))
# #循环输出每一行的内容

def read_xlrd(path,name, row,col):
    file = xlrd.open_workbook(path)
    data = file.sheet_by_name(name)
    print(data.name)

    # 获取行列数据



# =============================================================
# 导入csv包
import csv

# 读取本地csv文件
my_file = r"C:\\Users\\chenjingjian\\Desktop\\coupon_template (3).xls"

data = csv.reader(open(my_file, 'rb'))


# 循环输出每一行的内容
for user in data:
    print(user[0])
    print(user[1])
    print(user[2])
    print(user[3])

# ==========================================
import time
from selenium import webdriver


def UsrPwd():
    d = {'cjj@qq.com': '123456', 'def': '123456'}  # 使用字典
    print("read username and password!")
    return d


for usr, pwd in UsrPwd().items():  # 循环读取字典里的用户名及密码
    driver = webdriver.Chrome()
    driver.get("https://login.rosewholesale.com/m-users-a-sign.htm")
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(usr)
    time.sleep(3)
    driver.find_element_by_id("passwordsign").clear()
    driver.find_element_by_id("passwordsign").send_keys(pwd)
    time.sleep(3)
    driver.find_element_by_id("js_signInBtn").click()
    time.sleep(1)
    driver.close()
# =================================================







