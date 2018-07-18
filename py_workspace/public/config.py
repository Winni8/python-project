# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 14:12
# @File 	:config.py
# @Software :PyCharm

import time

# 获取时间
now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))

# 初始化数据库，用于生成测试需要的数据
datdpath = r".\\data\\test_InitializationData.py"

# 运行用例的路径，用于控制执行哪些用例
caselist = [".\\test_api"]

# 报告的路径，用户指定报告的路径
reportpath = ".\\report\\"+now+"\\"
