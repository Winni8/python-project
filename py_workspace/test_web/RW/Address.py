# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/4 16:18
# @File 	:Order_Shopping_PP.py
# @Software :PyCharm

"""
@auther:cjj
version:1.1
测试板块：编辑地址
"""

from selenium import webdriver
import unittest
import logging
import string
import random
from HTMLReport import AddImage, logger
from public.Random_longin import getemail, getNameOrAddress, getTelNo
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

baseurl = "http://login.pc-rosewholesale.com.release.php5.egomsl.com/m-users-a-sign.htm"
add_url = "http://user.pc-rosewholesale.com.release.php5.egomsl.com/m-users-a-address_list.htm"
log = logging.getLogger(__name__)  # 写入日志文件，报告中则不包含


class TestAddress(unittest.TestCase):

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
        """Address编辑页"""
        # 点击Edit跳转至地址编辑页
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='js_saderBar']//li[6]/a").click()
        driver.find_element_by_xpath(".//*[@id='userMain']/header[2]/a[3]").click()
        try:
            add_text = driver.find_element_by_xpath(".//*[@class='address']/section[2]/h4").text
            self.assertIn("Shipping Address", add_text)
            logger().info("跳转地址页OK")
        except AssertionError as e:
            logger().info("没有到地址页面", e)
        AddImage(driver.get_screenshot_as_base64())

    def test_03(self):
        """编辑地址：1.新增地址"""
        driver = self.driver

        src_uppercase = string.ascii_uppercase  # string_大写字母
        src_lowercase = string.ascii_lowercase  # string_小写字母

        # 生成名字的字符串，random.randint(1, 4)表达个数的范围
        src_uppercase_num = random.randint(1, 4)
        src_lowercase_num = random.randint(3, (10 - src_uppercase_num - 1))

        # 将生成的字符串赋值与名字：sample()生成的会自动放入list中；类似于split（），自动封装与list中；
        Firstname1 = random.sample(src_uppercase, src_uppercase_num) + random.sample(src_lowercase, src_lowercase_num)
        Lastname1 = random.sample(src_uppercase, src_uppercase_num) + random.sample(src_lowercase, src_lowercase_num)
        City1 = random.sample(src_uppercase, src_uppercase_num) + random.sample(src_lowercase, src_lowercase_num)
        State1 = random.sample(src_uppercase, src_uppercase_num) + random.sample(src_lowercase, src_lowercase_num)

        # 然后打乱字符串；
        random.shuffle(Firstname1)
        Firstname2 = "".join(Firstname1)

        random.shuffle(Lastname1)
        Lastname2 = "".join(Lastname1)

        random.shuffle(City1)
        City2 = "".join(City1)

        random.shuffle(State1)
        State2 = "".join(State1)

        # 邮编生成：
        ZIP = ['13134', '36367', '869696', "242-24", "242-567"]

        # 选择国家：将所有的国家抓取出来，然后放进列表中，随机选择其中的一个国家(这块是ok;但是state不会处理，就只能选特定的国家了)
        # country_texts = driver.find_elements_by_xpath(".//*[@id='addressfrom']/ul/li[6]/div/select/option")
        # select_country = []
        # for i in country_texts:
        #     logger().info("遍历国家，添加至国家列表")
        #     select_country.append(i.text)
        # logger().info(select_country)

        # 选择state,有两种情况，一种是有下拉框的，一种是没有下拉框的（不会处理啊，只会处理没有下拉框的）

        # 生成的最终值赋给各个input()框
        Firstname = Firstname2
        Lastname = Lastname2
        E_mailaddress = getemail(1)
        AddressLine1 = getNameOrAddress(0)
        select_state_end = State2
        City = City2
        PhoneNumber = getTelNo()
        ZIP_PostalCode = random.choice(ZIP)     # choice()返回的是str; 而choices()返回的是list

        driver.find_element_by_id("addShipAddr").click()  # 点击新增地址

        # Firstname定位
        driver.find_element_by_id("firstname").clear()
        driver.find_element_by_id("firstname").send_keys(Firstname)

        # Lastname定位
        driver.find_element_by_id("lastname").clear()
        driver.find_element_by_id("lastname").send_keys(Lastname)

        # E_mailaddress定位
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(E_mailaddress)

        # AddressLine1定位
        driver.find_element_by_id("addressline1").clear()
        driver.find_element_by_id("addressline1").send_keys(AddressLine1)

        # select_country_end 定位
        select = Select(driver.find_element_by_xpath(".//*[@id='addressfrom']/ul/li[6]/div/select"))
        select_country = ["Sweden", "Tajikistan", "Thailand", "Togo", "Zimbabwe", "Malta", "Vietnam"]
        select_country_end = random.choice(select_country)
        select.select_by_visible_text(select_country_end)
        sleep(3)

        # select_state_end 定位
        driver.find_element_by_xpath(".//*[@name='province']").clear()
        driver.find_element_by_xpath(".//*[@name='province']").send_keys(select_state_end)

        # City 定位
        driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys(City)

        # PhoneNumber 定位
        driver.find_element_by_xpath(".//*[@id='tel']").clear()
        driver.find_element_by_xpath(".//*[@id='tel']").send_keys(PhoneNumber)

        # ZIP_PostalCode 定位
        driver.find_element_by_id("zipcode").clear()
        driver.find_element_by_id("zipcode").send_keys(ZIP_PostalCode)
        AddImage(driver.get_screenshot_as_base64())
        sleep(5)

        # select_state_end 定位;(不知道什么原因之前的state没有生成，必须要重新定位，才能输入)
        driver.find_element_by_xpath(".//*[@name='province']").clear()
        driver.find_element_by_xpath(".//*[@name='province']").send_keys(select_state_end)

        # 点击保存提交
        # js = "document.getElementByClassName('btn').click();"
        # driver.execute_script(js)
        driver.find_element_by_xpath(".//*[@id='addressfrom']/div/button").click()
        sleep(3)

        try:
            text = driver.find_element_by_xpath(".//*[@id='mainWrap']/section/div/p[1]")
            self.assertIn("Receipt of your address information", text.text)
            logger().info("新增地址OK")
        except AssertionError as e:
            logger().log("新增地址失败", e)



     # @unittest.skip("ceshi")
    def test_04(self):
        """编辑地址：2.删除地址"""
        driver = self.driver
        driver.get(add_url)
        driver.refresh()

        # 把删除地址按钮装与list表中；随机删除其中的元素
        ele_del = driver.find_elements_by_xpath(".//*[@id='ship_addr_list']//div/a[2]")
        lenth = len(ele_del)
        lenth_end = random.randint(1, lenth-1)
        ele_del[lenth_end].click()
        AddImage(driver.get_screenshot_as_base64())
        driver.find_element_by_xpath(".//*[@id='xubox_layer1']/div[1]/span[2]/a[1]").click()
        sleep(3)

        try:
            driver.get(add_url)
            after = driver.find_elements_by_xpath(".//*[@id='ship_addr_list']//div/a[2]")
            after_len = len(after)
            self.assertNotEqual(lenth, after_len)
            logger().info("删除地址成功")
        except AssertionError as e:
            logger().info("删除地址失败", e)

    def test_05(self):
        """编辑地址：3.删除地址，添加限制"""
        pass


if __name__ == '__main__':
    unittest.main()
