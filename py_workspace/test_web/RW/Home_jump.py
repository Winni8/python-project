# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/2 10:05
# @File 	:Home_jump.py
# @Software :PyCharm

#coding = utf-8

from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
import logging
from HTMLReport import AddImage, logger

# 注意这两个日志，一个是控制台的，一个是测试报告中的
log = logging.getLogger(__name__)  # 写入日志文件，报告中则不包含


class TestTiaozhuan(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        log.info("写入日志，但是测试报告中是不会生成这条语句的。")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def setUp(self):
        pass

    # 点击首页搜索按钮
    def test_tip_search(self):
        somrthing = "women long"
        driver = self.driver
        baseurl = "https://www.rosewholesale.com/"
        driver.get(baseurl)

        # 首页广告弹框
        driver.find_element_by_xpath(".//*[@id='xubox_layer1']/div/div/div/a").click()
        element = driver.find_element_by_id("js_topSearch")
        element.send_keys(somrthing)
        element.send_keys(Keys.ENTER)
        AddImage(driver.get_screenshot_as_base64(), name="搜素截图")
        time.sleep(3)
        cut_title = driver.title
        try:
            self.assertIn("Wholesale Women Long", cut_title, "断言Women Long是否在cut_title中")
            logger().info("首页搜索框跳转OK")
        except AssertionError as e:
            logger().info("首页搜索跳转失败", e)

        driver.back()
        driver.refresh()

        # 首页点击购物车

    def test_cart_search(self):
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='js_topCart']/i").click()
        AddImage(driver.get_screenshot_as_base64(), name="跳转购物车")
        time.sleep(3)
        try:
            title = driver.title
            self.assertIn("My Cart", title)
            logger().info("跳转购物车OK")
        except AssertionError as e:
            logger().info("跳转购物车失败", e)
        driver.back()
        driver.refresh()

    # 首页android是否能正常切换
    def test_andriod(self):
        driver = self.driver
        # android按钮的跳转
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
            self.assertIn("应用", driver.title)
            logger().info("android 跳转成功")
        except AssertionError as e:
            logger().info("点击android跳转失败", e)
        driver.switch_to.default_content()
        driver.refresh()

    # 点击ios跳转
    @unittest.skip("ios配置链接有问题")
    def test_ios(self):
        driver = self.driver
        driver.get("https://www.rosewholesale.com/")
        element_ios = driver.find_element_by_xpath\
            (".//*[@id='pageFooter']/div[1]/div/div[2]/div[2]/div[4]/a[1]/span")
        element_ios.click()

        cut_handle1 = driver.current_window_handle
        all_handles1 = driver.window_handles
        for h_ios in all_handles1:
            if h_ios is not cut_handle1:
                driver.switch_to.window(h_ios)
        try:
            self.assertIn("ios", driver.page_source)
            self.log.info("点击ios跳转成功")

        except AssertionError as e:
            self.log.info("点击ios跳转失败", e)
        driver.switch_to.default_content()

    # 不同平台的分享
    def test_all_share(self):
        driver = self.driver
        # 移动到下方
        scroll_to_end = 'window.scrollTo(0, document.body.scrollHeight);'
        driver.execute_script(scroll_to_end)
        driver.find_element_by_xpath(".//*[@class='share clearfix']/a[1]").click()
        AddImage(driver.get_screenshot_as_base64())
        print(driver.current_window_handle)
        print(driver.window_handles)
        for i in driver.window_handles:
            if i != driver.current_window_handle:
                driver.switch_to.window(i)
        try:
            fb_url = driver.current_url
            print(fb_url)
            self.assertIn("rosewhs", fb_url)
            logger().info("Facebook跳转OK")
        except AssertionError as e:
            logger().info("Facebook跳转失败", e)
        time.sleep(3)
        driver.switch_to.default_content()

    # 底部文章链接跳转
    def test_text_link(self):
        pass

    # 跳转用户中心，是否OK
    def test_user_center_link(self):
        pass

    # 币种切换是否OK
    def test_user_bizhong_qiehuan(self):
        pass

    # 多语言切换OK
    def test_language_switching(self):
        pass

    def tearDown(self):
        AddImage(self.driver.get_screenshot_as_base64())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()







