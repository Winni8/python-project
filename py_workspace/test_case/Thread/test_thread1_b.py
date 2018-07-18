# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 14:01
# @File 	:test_thread1_b.py
# @Software :PyCharm

from time import sleep,ctime


def music(func):
    for i in range(2):
        print("I was listening to music! %s" % ctime())
        sleep(2)


def move(func):
    for i in range(2):
        print("I was looking at the movies! %s" % ctime())
        sleep(2)


if __name__ == '__main__':
    music("爱情买卖")
    move("阿凡达")
    print("all end :", ctime())
