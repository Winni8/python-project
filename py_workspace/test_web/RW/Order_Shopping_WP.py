# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/4 16:18
# @File 	:Order_Shopping_PP.py
# @Software :PyCharm

"""
@auther:cjj
version:1.1
测试板块：登陆下单
"""

from selenium import webdriver
import unittest
import logging
from HTMLReport import AddImage, logger
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

baseurl = "http://login.pc-rosewholesale.com.release.php5.egomsl.com/m-users-a-sign.htm"
log = logging.getLogger(__name__)  # 写入日志文件，报告中则不包含


class GetOrderWp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        log.info("日志记录")
        self.driver = webdriver.Chrome()
        self.driver.get(baseurl)
        try:
            self.driver.implicitly_wait(60)
        except:
            self.driver.refresh()
            self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        logger().info("窗口最大化")

    def setUp(self):
        pass

    def tearDown(self):
        AddImage(self.driver.get_screenshot_as_base64())

    @classmethod
    def tearDownClass(self):
        print("程序跑完")
        self.driver.quit()

    # 登陆
    def test_01(self):
        """test_login"""
        driver = self.driver
        email = "2694571567@qq.com"
        pwd = "123456"

        # 登陆
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(email)

        driver.find_element_by_id("passwordsign").clear()
        driver.find_element_by_id("passwordsign").send_keys(pwd)
        AddImage(driver.get_screenshot_as_base64())

        driver.find_element_by_id("js_signInBtn").click()

        # 断言是否登陆成功
        ele = driver.find_element_by_xpath(".//*[@class='email']/span")
        ele_text = ele.text

        try:
            self.assertIn(email, ele_text)
            logger().info("登陆成功")
        except AssertionError as e:
            logger().info("登陆失败", e)

    def test_02(self):
        """test_classify"""
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='nav']/div/ul/li[4]/a").click()
        sleep(3)
        AddImage(driver.get_screenshot_as_base64())

        # 悬浮排序
        element_ch = driver.find_element_by_xpath(".//*[@id='js_cateTopBar']/div[2]/div")
        ActionChains(driver).move_to_element(element_ch).perform()
        sleep(3)

        # 从小到大排序
        driver.find_element_by_link_text("Low Price").click()
        sleep(2)

        # 选商品,跳转商品详情页
        driver.find_element_by_xpath(".//*[@id='js_proList']/ul/li[1]/h3/a").click()
        AddImage(driver.get_screenshot_as_base64())

        # 添加购物车
        driver.find_element_by_id("new_addcart").click()
        sleep(3)

        # 断言是否进入购物车
        ele_bag = driver.find_element_by_xpath(".//*[@id='cart_list']/div[2]/section/h4")
        ele_bag_text = ele_bag.text
        try:
            self.assertIn("SHOPPING BAG", ele_bag_text)
            logger().info("商品添加购物车OK")
        except AssertionError as e:
            logger().info("添加失败", e)

    def test_03(self):
        """test_cart"""
        driver = self.driver
        cart_price = driver.find_element_by_id("price_total").text
        logger().info("购物车的价格：" + cart_price)

        # 进入结算页
        driver.find_element_by_id("js_checkoutBtn").click()
        AddImage(driver.get_screenshot_as_base64())

        # 选择物流
        driver.find_element_by_id("shipping4").click()

        # 取消运输费
        driver.find_element_by_id("insurance_checked").click()

        # 点击结算按钮进入支付平台：
        driver.find_element_by_xpath(".//*[@id='js_upFormBtn']").click()
        sleep(3)

    def test_04(self):
        """test_WP"""
        # 选择WP支付：

        name = "dsfs"
        card_id = "4444333322221111"
        driver = self.driver
        driver.find_element_by_xpath(".//*[@class='compCheckbox_label']/em[1]").click()
        AddImage(driver.get_screenshot_as_base64())

        # 输入WP的账号：
        driver.find_element_by_name("cardHolder").clear()
        driver.find_element_by_name("cardHolder").send_keys(name)

        driver.find_element_by_name("cardNumber").clear()
        driver.find_element_by_name("cardNumber").send_keys(card_id)

        # 使用select的方式不知道为什么也是选不中
        # select1_mouth = Select(driver.find_element_by_name("expirationMonth"))
        # select1_mouth.deselect_by_visible_text("10")
        #
        # select1_year = Select(driver.find_element_by_name("expirationYear"))
        # select1_year.deselect_by_visible_text("2020")

        # 只能采用别的方式了，靠
        path1 = ".//*[@id='content_wrap']/div[1]/div[1]/dl[1]/dd/div/div[3]/div/select"
        driver.find_element_by_xpath(path1).click()
        m_path = ".//*[@id='content_wrap']/div[1]/div[1]/dl[1]/dd/div/div[3]/div/select/option[10]"
        driver.find_element_by_xpath(m_path).click()

        path2 = ".//*[@id='content_wrap']/div[1]/div[1]/dl[1]/dd/div/div[4]/div/select"
        driver.find_element_by_xpath(path2).click()
        y_path = ".//*[@id='content_wrap']/div[1]/div[1]/dl[1]/dd/div/div[4]/div/select/option[9]"
        driver.find_element_by_xpath(y_path).click()

        s_path = ".//*[@id='content_wrap']/div[1]/div[1]/dl[1]/dd/div/div[5]/div[1]/input"
        driver.find_element_by_xpath(s_path).send_keys("100")
        AddImage(driver.get_screenshot_as_base64())

        # js处理提交按钮
        js = "document.getElementsByClassName('placeOrder btn block')[0].click()"
        driver.execute_script(js)
        AddImage(driver.get_screenshot_as_base64())

    def test_05(self):
        """test_getorder"""
        driver = self.driver
        order_num = driver.find_element_by_xpath(".//*[@id='mainWrap']/h4/strong").text
        logger().info("下单OK,订单号{}".format(order_num))


if __name__ == '__main__':
    unittest.main()


