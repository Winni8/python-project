# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 9:22
# @File 	:Webdriver_Api.py
# @Software :PyCharm
"""
这些是常见的api,比较简单的那种；碰到了在补充；


"""


from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

# TODO 最基础的界面操作
browser.maximize_window()  # 窗口最大化
browser.minimize_window()  # 窗口最小化
browser.implicitly_wait(10)  # 隐形等待 智能等待
print(browser.title)
print(browser.current_url)
print(browser.page_source)
browser.save_screenshot('sa.png')
c = browser.get_screenshot_as_file('11.png')
a = browser.get_screenshot_as_png()
b = browser.get_screenshot_as_base64()
print(browser.name)

browser = webdriver.Chrome()
browser.get('https://liushilive.github.io/html_example/')

# TODO 简单查找页面元素 ，查找单个元素，多个元素

element = browser.find_element_by_id('i1') # 通过ID
print(element.get_attribute('value'))

element1 = browser.find_element_by_name('t1')
print(element1.get_attribute('value'))

element2 = browser.find_element_by_xpath('//input[@id="i1"]')
print(element2.get_attribute('value'))

element3 = browser.find_element_by_link_text("返回演示官网")
element3 = browser.find_element_by_partial_link_text("官网")
element3.click()
browser.back()

element4 = browser.find_element_by_css_selector('#i1')
print(element4.get_attribute('value'))

element5 = browser.find_element_by_class_name('text')
print(element5.get_attribute('value'))

element6 = browser.find_elements_by_tag_name('')

from selenium.webdriver.common.by import By

element = browser.find_element(By.ID, 'i1')

# 查找多个元素

element = browser.find_elements_by_tag_name('h2') # 返回得是列表
print(type(element), len(element))
print(element[1].text)


# 单击元素
element = browser.find_element_by_xpath('//div[contains(text(), "请单击这里")]')
element.click()

# 清空和输入元素内容
element = browser.find_element_by_id('i1')
element.clear()
element.send_keys('123')
# 拼接等价于"4a"
element.send_keys('4', 'a')

# ===============================================================
# 模拟键盘操作
from selenium.webdriver.common.keys import Keys

element.send_keys(Keys.LEFT * 2, Keys.BACKSPACE)
element.send_keys(Keys.CONTROL, 'a')
element.send_keys(Keys.CONTROL, 'c')
element.send_keys(Keys.END, Keys.CONTROL, 'v')

# 双击操作

element = browser.find_element_by_xpath('//div[contains(text(), "请双击这里")]')
a = webdriver.ActionChains(browser) # 定义一个动作链
a.double_click(element) # 定义动作
a.perform() # 执行动作

# TODO 鼠标事件-悬浮操作

element = browser.find_element_by_xpath('//div[contains(text(), "鼠标")]')
webdriver.ActionChains(browser).move_to_element(element).perform()
webdriver.ActionChains(browser).move_to_element_with_offset()

webdriver.ActionChains(browser).move_by_offset(50, 60).perform() # 以鼠标为原点，向右移动50个像素点，向下移动60个像素点
webdriver.ActionChains(browser).move_by_offset(-40, -70).perform()

# 选择悬浮窗

element1 = browser.find_element_by_link_text('分 类')
webdriver.ActionChains(browser).move_to_element(element1).perform()

element2 = browser.find_element_by_link_text('编程语言')
webdriver.ActionChains(browser).move_to_element(element2).perform()

element3 = browser.find_element_by_link_text('Python')
webdriver.ActionChains(browser).move_to_element(element3).perform()


# 拖曳操作

element1 = browser.find_element_by_xpath('//div[@data-dad-id="1"]')
element2 = browser.find_element_by_xpath('//div[@data-dad-id="2"]')
webdriver.ActionChains(browser).drag_and_drop(element1, element2).perform()

import time
for i in range(1, 6):
    Xpath = '//div[@data-dad-id="%s"]' % i
    element1 = browser.find_element_by_xpath(Xpath)
    Xpath1 = '//div[@data-dad-id="6"]'
    element2 = browser.find_element_by_xpath(Xpath1)
    webdriver.ActionChains(browser).drag_and_drop(element1, element2).perform()
    time.sleep(1)


# 滑块验证

# 定位滑块
element1 = browser.find_element_by_xpath('//div[@id="drag"]/div[3]')
# 定位验证区域
element2 = browser.find_element_by_xpath('//div[@id="drag"]/div[2]')
# 查看element1 element2的size
print(element1.size, element2.size)
# 分别得到element1和element2的宽
w1 = element1.size.get('width')
w2 = element2.size.get('width')
# 计算滑动距离 w2 - w1; w2 - w1/2
w = w2 - w1/2

# 模拟滑动 瞬间移动
webdriver.ActionChains(browser).drag_and_drop_by_offset(element1, w, 0).perform()

# 分段滑动 模拟人的操作
# 模拟在element1上按住鼠标左键操作
webdriver.ActionChains(browser).click_and_hold(element1).perform()
# 分段均匀滑动
for i in range(8):
    webdriver.ActionChains(browser).move_by_offset(w / 8, 0).perform()
    time.sleep(0.2)

webdriver.ActionChains(browser).release(element1).perform()


# TODO 警告弹窗的简单操作

# 定位弹出警告框元素
element1 = browser.find_element_by_name('b1')
# 模拟点击该元素
element1.click()
# 定位警告弹窗
a = browser.switch_to.alert # 不能加（）
# 模拟点击确定
a.accept()
# 模拟点击取消
a.dismiss()
# 查看警告窗内容
print(a.text)

# 定位弹出提问框
element1 = browser.find_element_by_name('b2')
element1.click()
a = browser.switch_to.alert
a.send_keys('123456')
a.accept()

# TODO Selecet下拉框-3种常用方式：

from selenium.webdriver.support.select import Select

# 定位下拉框元素
element = browser.find_element_by_id('s1Id')
# 赋予下拉框对象
select = Select(element)
# 选择元素
select.select_by_index(0) # 索引的方式 从0开始
select.select_by_value('02') # value
select.select_by_visible_text('3') # 可见文本



element = browser.find_element_by_id('s3Id')
select = Select(element)
# 选择元素
select.select_by_index(0) # 索引的方式 从0开始
select.select_by_value('2') # value
select.select_by_visible_text('03') # 可见文本
select.select_by_visible_text('04')
# 删除元素
select.deselect_by_index(0)
select.deselect_by_value('2')
select.deselect_by_visible_text('03')
select.deselect_all()


# 网页滚动
# 用js脚本来定义 selenium暂时没有现成API来实现这个功能
scroll_to_top = 'window.scrollTo(0, 0);' # 定义网页顶部的脚本
scroll_to_end = 'window.scrollTo(0, document.body.scrollHeight);' # 定义网页的底部
scroll_to_element = 'arguments[0].scrollIntoView();' # 定义网页的某个元素

browser.execute_script(scroll_to_top)
browser.execute_script(scroll_to_end)
browser.execute_script(scroll_to_element, element)



# TODO cookies操作，添加cookies，dict形式

browser.add_cookie({'Name': 'Li', 'Value': '1'}) # 注意key只能小写
browser.add_cookie({'name': 'Li', 'value': '1'})
browser.add_cookie({'name': 'abc', 'value': '1111'})

# 得到浏览器的某一特定cookie
cookie = browser.get_cookie('abc')
print(cookie)
print(cookie['value'])

# 得到浏览器所有的cookies
cookies = browser.get_cookies()
print(cookies)
print(len(cookies))

# 删除某一特定cookies
browser.delete_cookie('abc')
print(browser.get_cookie('abc'))

# 删除所有的cookies
browser.delete_all_cookies()
print(browser.get_cookies())


# TODO 定位iframe,注意进出
frame_element = browser.find_element_by_name('frame1')
# 跳到frame1
browser.switch_to.frame(frame_element)
# 或者直接定位到iframe的id
browser.switch_to.frame('frame1')
browser.switch_to.frame(0)
# 定位国际版
browser.find_element_by_id('est_en').click()
# 定位frame1里的搜索框
element = browser.find_element_by_id('sb_form_q')
webdriver.ActionChains(browser).click(element).perform()
# 输入搜索内容并回车
element.send_keys("Chrome")
time.sleep(0.2)
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.ENTER)

element1 = browser.find_element_by_id('s3Id')
# 生成选择列表对象
ele = Select(element1)


browser.switch_to.default_content()

# <html>
#     <iframe id='frame1'>
#         <iframe id='frame2'/>
#     </iframe>
# <html>

# 1.从主文档切到frame2， 一层层切进去
browser.switch_to.frame('frame1')
browser.switch_to.frame('frame2')

# 2.从frame2退回主文档
# 方法一：
browser.switch_to.parent_frame()
browser.switch_to.parent_frame()
# 方法二：
browser.switch_to.default_content()

# TODO 之前使用过js处理句柄，也可以不用js，采用简单的遍历切换到相应的句柄中；
browser = webdriver.Chrome()
browser.get('http://sahitest.com/demo/index.htm')
browser.maximize_window()
browser.implicitly_wait(10)

current_window = browser.current_window_handle  # 获取当前窗口handle name
browser.find_element_by_link_text('Window Open Test With Title').click()

all_windows = browser.window_handles

for window in all_windows:
    if window != current_window:
        browser.switch_to.window(window)

print(browser.title)

browser.close()
print(browser.title) # 即使关闭了第二个窗口，也无法对第一个窗口的元素进行操作
browser.switch_to.window(current_window) # 必须切回第一个窗口
print(browser.title)
browser.quit()



