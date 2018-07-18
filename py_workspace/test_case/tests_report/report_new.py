# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/12 13:52
# @File 	:report_new.py
# @Software :PyCharm


import unittest
from selenium import webdriver
from BeautifulReport import BeautifulReport


class Testaa(unittest.TestCase):
    u'''测试用例a的集合'''
    @classmethod
    def setUpClass(cls):
        file_path = r"C:\Users\chenjingjian\AppData\Roaming\Mozilla\Firefox\Profiles\jzf6o3ct.default-1524801335999"
        profile = webdriver.FirefoxProfile(file_path)
        cls.driver = webdriver.Firefox(profile)
        cls.driver.implicitly_wait(30)

    def setUp(self):
        self.driver.get("https://www.cnblogs.com/Winni8/")

    def test_01(self):
        u'''用例1：用例1的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("Winni8", t)

    def test_02(self):
        u'''用例2：用例2的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("Winni8", t)

    @BeautifulReport.add_test_img('测试报告.png')
    def test_03(self):
        u'''用例3：用例3的操作步骤'''
        t = self.driver.title
        print(t)
        self.assertIn("Winni8", t)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Testaa))
    BeautifulReport(suite).report(filename="report.html", description="测试deafult报告", log_path="report")

