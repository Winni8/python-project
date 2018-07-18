# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 14:01
# @File 	:test_thread1_a.py
# @Software :PyCharm

from time import sleep, ctime


def music():
    print("I was listening to music! %s" % ctime())
    sleep(2)


def move():
    print("I was looking at the movies! %s" % ctime())
    sleep(3)


if __name__ == '__main__':
    music()
    move()
    print("all end:", ctime())
