# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/11 15:33
# @File 	:asd.py
# @Software :PyCharm

from selenium import webdriver
options = webdriver.ChromeOptions()
# 添加 chrome 启动参数
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--start-maximized")

# 通过设置user-agent，用来模拟移动设备
# 比如模拟 android QQ浏览器
options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')

# 模拟iPhone 6
options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')


# 添加扩展
# extension_path = '/extension/path'
# options.add_extension(extension_path)

# 附赠添加代理方法
PROXY = "proxy_host:proxy:port"
desired_capabilities = options.to_capabilities()
desired_capabilities['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}

# 禁止图片加载
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options, desired_capabilities=desired_capabilities)

driver.get("https://www.baidu.com/")

#driver.quit()