# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 16:46
# @File 	:test_fox_chrome.py
# @Software :PyCharm

from selenium import webdriver
import threading
import time
from time import ctime, sleep
import unittest
from test_suite import suite_Test_report
import HTMLReport
from public.SendEmail_Auto_New import new_file, send_email


# def test_fox(timesout):
#     driver = webdriver.Firefox()
#     driver.get("https://login.rosewholesale.com/m-users-a-sign.htm")
#     driver.implicitly_wait(int(timesout))
#     driver.find_element_by_id("email").send_keys("cjj@qq.com")
#     driver.find_element_by_id("passwordsign").send_keys("123456")
#     driver.find_element_by_id("js_signInBtn").click()
#     print(driver.current_url)
#     sleep(3)
#     driver.quit()
#
#
# def test_chrome():
#     driver = webdriver.Chrome()
#     driver.get("https://loginm.twinkledeals.com/m-users-a-sign.htm?ref=%2Fm-users.html")
#     driver.implicitly_wait(int(20))
#     driver.set_window_size(412, 732)
#     driver.find_element_by_id("sign_email").send_keys("2694571567@qq.com")
#     driver.find_element_by_id("sign_password").send_keys()
#     driver.find_element_by_id("signinbtn").click()
#     sleep(3)
#     driver.quit()


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([suite_Test_report.return_suite()])
    Log_path = "D:\\java\\Python\\py_workspace\\Log\\report"
    runner = HTMLReport.TestRunner(log_file_name=Log_path, title="test_thread", description="用例情况")
    runner.run(suite)


# 创建线程组
threads = []
# t1 = threading.Thread(target=test_chrome, )
# threads.append(t1)

# t2 = threading.Thread(target=test_fox, args=(10,))
# threads.append(t2)
#
t3 = threading.Thread(target=test_suite,)
threads.append(t3)

print(threads)


if __name__ == '__main__':
    start = time.clock()
    for i in threads:
        i.start()

    for j in threads:
        j.join()

    test_report_dir = "D:\\java\\Python\\py_workspace\\report\\"
    new_repoet_path = new_file(test_report_dir)
    send_email(new_repoet_path)
    end = time.clock()
    print("耗时%s" % (end-start))

