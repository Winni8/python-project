# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 10:07
# @File 	:Multithreading.py
# @Software :PyCharm

from selenium import webdriver

# 测试用例
from time import sleep, ctime
import threading
import time
import thredds


def test_baidu(browser, search):
    print('start:%s' % ctime())
    print('browser:%s,' % browser)

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == 'ff':
        driver = webdriver.Firefox()
    else:
        print("browser 参数有误，只能为ie ，ff，chrome")

    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(search)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()


# ie有问题，可能版本不对；
if __name__ == '__main__':
    start = time.clock()
    # 启动参数（指定浏览器与百度收缩内容）
    dicts = {'chrome': 'threading', 'ff': 'python'}
    threads = []
    files = range(len(dicts))
    print(files)

    # 创建线程
    for browser, search in dicts.items():
        t = threading.Thread(target=test_baidu, args=(browser, search))
        threads.append(t)

    # 启动线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:%s' % ctime())
    print(time.clock()-start)
