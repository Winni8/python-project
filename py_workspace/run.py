# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/3 14:19
# @File 	:runfuben.py
# @Software :PyCharm

"""
这种测试报告形式，属于比较新的那种，下载下来不需要更改什么，可以直接使用；
同时 HTMLReport 这里面自带截图，logger()方法，很实用，唯一的缺点就是生成的数据没有可视化视图；
但是应有数据还是有的，个人比较喜欢这种形式，因为里面的方法，参数比较丰富；
"""

import unittest
import HTMLReport
from public.SendEmail_Auto_New import new_file, send_email
from test_suite import suite_serach
from test_suite import suite_register
from test_suite import suite_login
from test_suite import suite_order_shopping
from test_suite import suite_order_wp
from test_suite import suite_address
from public.Random_longin import main, output
from test_suite.suite_batch_login import return_batchlogin
from test_suite import suite_shunxu
from test_suite import suite_public

if __name__ == '__main__':

    suite = unittest.TestSuite()

    # 搜索用例套件
    # suite.addTest(suite_serach.return_search())

    # 注册用例套件
    # suite.addTests(suite_register.retuen_register())

    # 登陆模块用例套件
    # suite.addTests(suite_login.return_login())

    # 登陆下单pp支付
    # suite.addTests(suite_order_shopping.return_order_shopping())

    # 登陆下单wp支付
    # suite.addTests(suite_order_wp.return_wp())

    # 登陆编辑地址
    # suite.addTests(suite_address.return_address())

    # 批量验证登陆各种提示语
    # suite.addTests(return_batchlogin())

    # 验证unittest的用例执行顺序
    # suite.addTests(suite_shunxu.re_shunxu())

    # 共用的测试用例
    suite.addTests(suite_public.return_public())
    # log_file_name这里面的log的目录也是可以更改，默认情况下是在report的同一层，.log文件
    # 换句话说是可以重新定义他们的路径；个人建议使用的默认，免得出幺蛾子；
    HTMLReport.TestRunner(report_file_name="report",   # 报告文件名，如果未赋值，将采用“test+时间戳”；注意这里与邮件的
                                                        # 发送报告路径要一致
                          output_path='report',        # 保存文件夹名，默认“report”,注意同一级的目录
                          title="测试报告",             # 保存文件夹名，默认“report”
                          description="用例情况",       # 报告描述，默认“无测试描述”
                          thread_count=5,               # 并发线程数量（无序执行测试），默认数量 1
                          sequential_execution=True,    # 是否按照套件添加(addTests)顺序执行，默认是flase
                          thread_start_wait=0,          # 各线程启动延迟，默认 0 s
                          lang='cn'                     # 支持中文与英文，默认中文
                          ).run(suite)

    # 获取最新的测试报告
    # path = 'report/report.html'
    # new_path = new_file(path)

    # 发送测试报告

    new_path = "report/report.html"
    send_email(new_path)

