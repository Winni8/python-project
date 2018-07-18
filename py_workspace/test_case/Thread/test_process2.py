# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 11:06
# @File 	:test_process2.py
# @Software :PyCharm

from multiprocessing import Pool
import os
from time import ctime
import time
import sys
sys.getdefaultencoding()


def child_process_test(name, sleep_time):
    print('Child process %s with processId %s starts.' % (name, os.getpid()), ctime())
    time.sleep(sleep_time)
    print('Child process %s with processId %s ends.' % (name, os.getpid()), ctime())


if __name__ == "__main__":
    print('Parent processId is start and id is: %s.' % os.getpid())
    # p = Pool()  # 进程池默认大小是cpu的核数,就是本地电脑的核数
    p = Pool(10)  # 生成一个容量为10的进程池，即最大同时执行10个子进程
    for i in range(10):
        # 向进程池提交目标请求.注意参数；这里涉及一个同步和异步的说法；下面的写法是同步；
        p.apply_async(child_process_test, args=('child' + str(i), 3,))
        # 异步写法：
        # p.apply(child_process_test, args=("child"+str('i'), 2,))

    print('Child processes are running.')
    # 下面才是进程真正开始的位置
    # 关闭进程池，使之不能再添加新的进程;已经执行的进程会等待继续执行直到结束。
    p.close()
    p.join()  # 用来等待进程池中的所有子进程结束再向下执行代码，必须在p.close()或者p.terminate()之后执行
    print('All Processes end.')
