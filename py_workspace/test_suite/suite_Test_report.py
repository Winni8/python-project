# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 9:55
# @File 	:suite_Test_report.py
# @Software :PyCharm

import unittest
from test_web.RW.Home_jump import TestTiaozhuan


def return_suite():
    suite = unittest.TestSuite()
    suite.addTests([TestTiaozhuan("test_tip_search"), TestTiaozhuan("test_cart_search"),
                    TestTiaozhuan("test_andriod"), TestTiaozhuan("test_ios"), TestTiaozhuan("test_all_share"),
                    TestTiaozhuan("test_text_link"), TestTiaozhuan("test_user_center_link"),
                    TestTiaozhuan("test_user_bizhong_qiehuan"), TestTiaozhuan("test_language_switching")])

    return suite
    # 不使用加载器
    # 这是测试用的，case
    # suite.addTests([TestReport("test_a"), TestReport("test_b"), TestReport("test_c"), TestReport("test_d")])
    # 使用加载器跟加载器没有关系，仅仅是运行的方式不同
    #loadcase = unittest.TestLoader().loadTestsFromTestCase(TestReport)
    #suite.addTests(loadcase)
