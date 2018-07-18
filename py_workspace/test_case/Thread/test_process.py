# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 10:36
# @File 	:test_process.py
# @Software :PyCharm
# -*- coding: utf-8 -*


from multiprocessing import Process
import os
import time


# 子进程fun
def child_projcess_fun(name):
    print('Child process %s with processId %s starts.' % (name, os.getpid()))
    time.sleep(3)
    print('Child process %s with processId %s ends.' % (name, os.getpid()))


# 注意一点进程在window os下只能在main函数下面执行
if __name__ == "__main__":
    print('Parent processId is: %s.' % os.getpid())
    p = Process(target=child_projcess_fun, args=('zni',))
    print('child process starts')
    p.start()  # 开始进程
    p.join()  # 等待子进程结束后父进程再继续执行
    print('Parent Process ends and all ending')
