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

baseurl = "http://login.pc-rosewholesale.com.release.php5.egomsl.com/m-users-a-sign.htm"
log = logging.getLogger(__name__)  # 写入日志文件，报告中则不包含


class GetOrder(unittest.TestCase):

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
        AddImage(driver.get_screenshot_as_base64())

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
        AddImage(driver.get_screenshot_as_base64())

        # 点击支付平台的结算按钮，输入账号；次按钮有时候失效，采用js试试：
        driver.find_element_by_xpath(".//*[@class='pc_side_total']/div[2]/i").click()
        js = "document.getElementsByClassName('placeOrder btn block')[0].click()"
        driver.execute_script(js)
        logger().info("跳转至PP账号输入页面")
        AddImage(driver.get_screenshot_as_base64())

    def test_04(self):
        """test_pp"""
        driver = self.driver
        # 切换iframe,通过name 切到iframe中
        ele_ifame = driver.find_element_by_xpath("//*[@title='PayPal - Log In']")
        driver.switch_to.frame(ele_ifame)
        sleep(5)
        logger().info("进入iframeinjectedUl中")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("441817_1310950685_per@qq.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123123123")

        AddImage(driver.get_screenshot_as_base64())
        logger().info("输入pp的账号密码")

        driver.find_element_by_name("btnLogin").click()
        sleep(5)
        driver.switch_to.parent_frame()  # 切回原来默认的ifame中
        AddImage(driver.get_screenshot_as_base64())

        """这之后的都有问题，只能手动推过去，不然页面不会跳转，不知道什么原因；打印那个页面的url是OK的，
        但是点击那个提交按钮就有问题了，同时那个页面也没有iframe，上一成是有的，但是已经切回
        默认框了，反正就是那个按钮没有反应，没有办法跳转至下单成功页面"""
        # 点击结算
        url = driver.current_url
        url_new = url.replace("login", "review")
        driver.get(url_new)
        driver.refresh()
        print(driver.current_url)
        driver.set_window_size(412, 732)
        # 滚动到下方的规则看有没有效===事实证明页面失效的
        js3 = "arguments[0].scrollIntoView();"
        ele_sroll = driver.find_element_by_link_text("规则")
        driver.execute_script(js3, ele_sroll)
        AddImage(driver.get_screenshot_as_base64())
        # 使用js点击提交按钮
        js2 = "document.getElementById('button').click()"
        driver.execute_script(js2)
        AddImage(driver.get_screenshot_as_base64())
        logger().info("跳转成功页")

    def test_05(self):
        """test_getorder"""
        driver = self.driver
        order_num = driver.find_element_by_xpath(".//*[@id='mainWrap']/h4/strong").text
        logger().info("下单OK,订单号{}".format(order_num))

#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTests([GetOrder("test_login"), GetOrder("test_classify"),
#                     GetOrder("test_cart"), GetOrder("test_pp"), GetOrder("test_getorder")])
#
#     runner = unittest.TextTestRunner(verbosity=2).run(suite)

