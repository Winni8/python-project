# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 14:01
# @File 	:test_thread.py
# @Software :PyCharm

import threading
from time import sleep, ctime
import time


def music(func):
    for i in range(2):
        print("I was listening to music! %s! %s" % (func, ctime()))
        sleep(2)


def move(func):
    for i in range(2):
        print("I was looking at the movies! %s! %s" % (func, ctime()))
        sleep(3)


# 创建线程数组
threads = []

# 创建线程 t1,并添加到线程数组
t1 = threading.Thread(target=music, args=(u'爱情买卖',))
threads.append(t1)

# 创建线程 t2,并添加到线程数组
t2 = threading.Thread(target=move, args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':

    # 启动线程
    start = time.clock()
    for i in threads:
        i.start()
    # 守护线程
    for i in threads:
        i.join()
    end = time.clock()
    print('all end: %s ==> 总共花费时间是%s' % (ctime(), end-start))
