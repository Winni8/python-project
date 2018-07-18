# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/12 9:24
# @File 	:抓取网页元素.py
# @Software :PyCharm

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
# firefox浏览器配置文件地址,启动默认地址
file_path = r"C:\Users\chenjingjian\AppData\Roaming\Mozilla\Firefox\Profiles\jzf6o3ct.default-1524801335999"
profile = webdriver.FirefoxProfile(file_path)
driver = webdriver.Firefox(profile)

driver.get("https://home.cnblogs.com/u/Winni8/relation/following")

time.sleep(3)
cookies = driver.get_cookies()  # 获取浏览器cookies
print(cookies)

s = requests.session()  # 新建session

# 添加cookies到CookieJar
c = requests.cookies.RequestsCookieJar()
for i in cookies:
    c.set(i["name"], i['value'])

s.cookies.update(c)  # 更新session里cookies


# 发请求
r1 = s.get("https://home.cnblogs.com/followers/")

soup = BeautifulSoup(r1.content, "html.parser")

# 抓取我的粉丝数
fensinub = soup.find_all(class_="current_nav")
print(fensinub[0].string)
num = re.findall(u"我的粉丝\((.+?)\)", fensinub[0].string)
print(u"我的粉丝数量：%s"%str(num[0]))

# 计算有多少页，每页45条
ye = int(int(num[0])/45)+1
print(u"总共分页数：%s"%str(ye))

# 抓取第一页的数据
fensi = soup.find_all(class_="avatar_name")
for i in fensi:
    name = i.string.replace("\n", "").replace(" ", "")
    print(name)
    with open("name.txt", "a") as f:  # 追加写入
        f.write(name.encode("utf-8")+"\n")

# 抓第二页后的数据
# for i in range(2, ye+1):
#     r2 = s.get("https://home.cnblogs.com/u/yoyoketang/relation/followers?page=%s"%str(i))
#     soup = BeautifulSoup(r1.content, "html.parser")
#     # 抓取我的粉丝数
#     fensi = soup.find_all(class_="avatar_name")
#
#     for i in fensi:
#         name = i.string.replace("\n", "").replace(" ","")
#         print(name)
#         with open("name.txt", "a") as f:  # 追加写入
#             f.write(name.encode("utf-8")+"\n")







driver.quit()
