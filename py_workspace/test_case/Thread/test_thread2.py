# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 14:01
# @File 	:test_thread2.py
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


def look(func):
    for i in range(3):
        print("I was looking at the file that is %s! %s" % (func, ctime()))
        sleep(4)


# 判断文件类型，交给相应的函数执行
def player(name):
    print(name)
    r = name.split('.')[1]
    if r == 'mp3':
        music(name)
    elif r == 'mp4':
        move(name)
    elif r == "txt":
        look(name)
    else:
        print('error: The format is not recognized!')


list = ["爱情买卖.mp3", '阿凡达.mp4', "test.txt"]  # 格式说明

# 创建线程数组
threads = []
files = range(len(list))

for i in files:  # 这是循环的次数
    t = threading.Thread(target=player, args=(list[i],))  # targer是函数名，也就是说的功能模块，arge为函数的参数
    threads.append(t)


if __name__ == '__main__':
    # 启动线程
    start = time.clock()
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()
    # 所有程序结束时间
    end = time.clock()
    print('all end: %s ===> 共用了%s时间' % (ctime(), end-start))
