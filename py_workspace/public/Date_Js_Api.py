# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/25 15:17
# @File 	:Date_Js_Api.py
# @Software :PyCharm

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://liushilive.github.io/html_example/")
driver.implicitly_wait(30)


# TODO 日期函数（年月日） 直接调用
def select_date(year, month, day):
    today = driver.find_element_by_class_name("today").text

    # js滚动到日历位置
    js = "arguments[0].scrollIntoView();"
    taget = driver.find_element_by_class_name("today")
    driver.execute_script(js, taget)

    # 使用split()方法拆分
    yy, mm, dd = today.split("-")
    print(yy, mm, dd)

    # 年
    yy = int(yy)
    year = int(year)
    if year > yy:
        new = driver.find_element_by_id("nextMonth")
        for c in range(year-yy):
            new.click()
    elif year < yy:
        old = driver.find_element_by_id("prevYear")
        for c in range(yy-year):
            old.click()
    else:
        print("你输入的是今年")

    # 月
    mm = int(mm)
    month = int(month)
    if month > mm:
        new2 = driver.find_element_by_id("nextMonth")
        for c in range(month-mm):
            new2.click()
    elif month < mm:
        old2 = driver.find_element_by_id("prevMonth")
        for c in range(mm-month):
            old2.click()
    else:
        print("你输入的是本月")

    # 日
    xpath = ".//*[@id='schedule-box']/ul[2]/li/span[text()= {}]".format(int(day))
    driver.find_element_by_xpath(xpath).click()

# select_date(2010, 10, 10)
select_date(1500, 12, 12)

# =============================================

# TODO 日期函数（年月日，时分秒）
def testselect_date(year, mouth, day, hour, minutes, second):
    # 将界面移动到日期位置
    date = driver.find_element_by_xpath("//*[@placeholder='点我查看效果']")
    js = "arguments[0].scrollIntoView();"
    driver.execute_script(js, date)

    # 时
    date.click()
    hour = int(hour)
    driver.find_element_by_id("calendarHour").click()
    if int(hour) < 10:
        hour = "0" + str(hour)
    h_path = ".//*[@id='calendarHour']/option[@value='{}']".format(hour)
    driver.find_element_by_xpath(h_path).click()

    # 分钟
    minutes = int(minutes)
    driver.find_element_by_id("calendarMinute").click()
    if int(minutes) < 10:
        minutes = "0" + str(minutes)
    min_path = ".//*[@id='calendarMinute']/option[@value='{}']".format(minutes)
    driver.find_element_by_xpath(min_path).click()

    # 秒
    second = int(second)
    driver.find_element_by_id("calendarSecond").click()
    if int(second) < 10:
        second = "0" + str(second)
    s_path = ".//*[@id='calendarSecond']/option[@value='{}']".format(second)
    driver.find_element_by_xpath(s_path).click()

    # 年
    year = int(year)
    driver.find_element_by_id("calendarYear").click()
    y_path = ".//*[@id='calendarYear']/option[@value='{}']".format(year)
    driver.find_element_by_xpath(y_path).click()

    # 月
    mouth = int(mouth)
    driver.find_element_by_id("calendarMonth").click()
    m_path = ".//*[@id='calendarMonth']/option[@value='{}']".format(int(mouth-1))
    driver.find_element_by_xpath(m_path).click()

    # 日
    d_path = ".//*[@id='calendarTable']//td[text()={}]".format(int(day))
    driver.find_element_by_xpath(d_path).click()
# testselect_date(2000, 10, 20, 20, 20, 20)
testselect_date(1968, 10, 10, 10, 10, 10)

# TODO 屌炸天的拖拽
##
# from selenium.webdriver.common.action_chains import ActionChains
#
# # 将元素移到拖拽的位置：
# lelement = driver.find_element_by_xpath("//*[@data-dad-position='4']")
# js = "arguments[0].scrollIntoView();"
# driver.execute_script(js, lelement)
# lelement6 = driver.find_element_by_xpath("//*[@data-dad-position='6']")
# lelement5 = driver.find_element_by_xpath("//*[@data-dad-position='5']")
# lelement4 = driver.find_element_by_xpath("//*[@data-dad-position='4']")
# lelement3 = driver.find_element_by_xpath("//*[@data-dad-position='3']")
# lelement2 = driver.find_element_by_xpath("//*[@data-dad-position='2']")
# lelement1 = driver.find_element_by_xpath("//*[@data-dad-position='1']")
#
# webdriver.ActionChains(driver).drag_and_drop(lelement1, lelement6).perform()
# webdriver.ActionChains(driver).drag_and_drop(lelement2, lelement6).perform()
# webdriver.ActionChains(driver).drag_and_drop(lelement3, lelement6).perform()
# webdriver.ActionChains(driver).drag_and_drop(lelement4, lelement6).perform()
# webdriver.ActionChains(driver).drag_and_drop(lelement5, lelement6).perform()

# '''======================================================'''
# TODO 表格处理，读取单行或者单列的元素
# 移到表格处：
elemengt = driver.find_element_by_xpath("html/body/form[5]/h2")
js = "arguments[0].scrollIntoView();"
driver.execute_script(js, elemengt)

texts = driver.find_elements_by_xpath(".//*[@id='t4']//td[4]")
for i in texts[1:]:
    print(i.text)

# ===========================================================
# TODO js处理脚本的几种方式：
# TODO 1、js 处理页面滚动
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("ddt")
driver.find_element_by_id("su").send_keys(Keys.ENTER)
time.sleep(3)
driver.set_window_size(413, 732)
# 找一个中间元素
element00 = driver.find_element_by_partial_link_text("百度百科")
js1 = "window.scrollTo(10000,10000);"           # 左上角过着右下角；
js2 = "window.scrollTo(0,document.body.scrollHeight);"      # 底部
js3 = "arguments[0].scrollIntoView();"
driver.execute_script(js3, element00)
driver.execute_script(js1)
driver.execute_script(js2)
driver.quit()

# =====================================================
# TODO 2、js 处理日期；带有readonly属性的处理方式
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/index/init")
driver.implicitly_wait(30)
start = time.clock()
end = time.clock()
print(end-start)
# js_c1 = "document.getElementById('train_date').removeAttribute('readonly')"  # 1.原生js，移除属性
# js_c2 = "$('input[id=train_date]').removeAttr('readonly')"  # 2.jQuery，移除属性
# js_c3 = "$('input[id=train_date]').attr('readonly',false)"  # 3.jQuery，设置为false
js_value = 'document.getElementById("train_date").value="2018-07-15"'  # 通过value值来进行传值
driver.execute_script(js_value)                                 # 无论哪种情况都要进行js先处理
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2018-07-07")
driver.quit()

# =========================================================
# TODO 3、js 处理句柄，窗口的跳转；带有target="_blank"属性的处理不跳转；
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(30)

js_blank = "document.getElementsByClassName('mnav')[0].target='';"
driver.execute_script(js_blank)

driver.find_element_by_link_text("新闻").click()
print(driver.current_window_handle)
driver.back()
driver.forward()
driver.quit()

# =================================================
# TODO 4、js 处理时效的按钮
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(30)
driver.refresh()
# 鼠标移到设置处
settings = driver.find_element_by_link_text('设置')
webdriver.ActionChains(driver).move_to_element(settings).perform()
time.sleep(3)
driver.find_element_by_link_text("搜索设置").click()

select = Select(driver.find_element_by_id("nr"))
select.select_by_visible_text("每页显示50条")

#  driver.find_element_by_class_name("prefpanelgo").click()  # 不失效时，直接点击即可；

js_click = "document.getElementsByClassName('prefpanelgo')[0].click();"  # 处理时效按钮
driver.execute_script(js_click)
driver.switch_to.alert.accept()
driver.quit()

# ============================================================
# TODO 4、js 处理div的内嵌条,只分Top 和 Left 赋值就可以进行移动了
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("file:///D:/java/Python/py_workspace/data/%E5%86%85%E6%AC%A0%E6%9D%A1.html")
js_div = "document.getElementById('yoyoketang').scrollTop=10000"
js_div2 = "document.getElementById('yoyoketang').scrollLeft=10000"
driver.execute_script(js_div2)

driver.quit()

# =========================================================
# TODO 5、 js处理弹框，很多网站首页都有弹框展示，而有时候不好处理，可以将弹框去掉；
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.rosewholesale.com/")

# 弹框
js = "document.getElementById('xubox_layer1').style.display='none';"
driver.execute_script(js)
# 蒙层
js2 = "document.getElementById('xubox_shade1').style.display='none';"
driver.execute_script(js2)

driver.find_element_by_id("js_topSearch").send_keys("women")
driver.find_element_by_id("js_topSearch").send_keys(Keys.ENTER)
print("ok")
driver.quit()

# ==============================================================
# TODO 6、js打开新窗口，关闭窗口，打开新连接,前进，后退；
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.baidu.com/")

# 新建窗口
js = "window.open();"
driver.execute_script(js)
driver.switch_to.window(driver.window_handles[1])

# 关闭新建的窗口，同时把句柄切回默认的窗口，才能在默认的窗口进行操作
js2 = "window.close();"
driver.execute_script(js2)
driver.switch_to.window(driver.window_handles[0])

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("hh")

# js可用宽度高度，但是不知道怎么打印输出的值,这个不会(=^ ^=)
js = "document.write('可用宽度: ' + screen.availWidth);"
js1 = "document.write('可用高度: ' + screen.availHeight);"
print(driver.get_window_size())  # 这种是通过selenium的api直接来获取这个值

# js返回url, 也是不会打印输出的值
js2 = "document.write(location.href);"
a = driver.execute_script(js2)

# js打开链接，跟get()方法是一样的；
js3 = " window.location.assign('http://www.w3cschool.cc')"
driver.execute_script(js3)
driver.back()

# js 窗口后退前进
js4 = "window.history.back();"
driver.execute_script(js4)

js5 = "window.history.forward();"
driver.execute_script(js5)
driver.quit()

# ================================================================





