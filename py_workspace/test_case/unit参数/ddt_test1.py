# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/12 8:49
# @File 	:ddt_test1.py
# @Software :PyCharm

import unittest
from ddt import ddt, data ,unpack
from public import Read_data
import time

"""ddt是按照文档添加的顺序执行的；不会处理字典形式的，好烦；
 
"""


@ddt
class Test_ddt(unittest.TestCase):

    @data(*Read_data.read_text("D:\java\Python\py_workspace\data\paramunittest"))
    @unpack
    def test_ddt(self, user, pwd, result):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % user)
        print("输入密码：%s" % pwd)
        print("期望结果：%s " % result)
        time.sleep(0.5)
        self.assertTrue(result == "true")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_ddt))
    unittest.TextTestRunner(verbosity=2).run(suite)
