# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/11 15:27
# @File 	:Default_chrome.py
# @Software :PyCharm
"""目前依旧不会怎么处理"""

class Options(object):

    def __init__(self):
        # 设置 chrome 二进制文件位置
        self._binary_location = ''
        # 添加启动参数
        self._arguments = []
        # 添加扩展应用
        self._extension_files = []
        self._extensions = []
        # 添加实验性质的设置参数
        self._experimental_options = {}
        # 设置调试器地址
        self._debugger_address = None


# 移动设备user-agent表格：http://www.fynas.com/ua
# 通过设置user-agent，用来模拟移动设备
# 比如模拟 android QQ浏览器

