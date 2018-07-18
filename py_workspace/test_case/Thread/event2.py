# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/12 16:30
# @File 	:event2.py
# @Software :PyCharm

import threading
import time

event = threading.Event()


def chiHuoGuo(name):
    # 等待事件，进入等待阻塞状态
    print( '%s 已经启动' % threading.currentThread().getName())
    print ('小伙伴 %s 已经进入就餐状态！'%name)
    time.sleep(1)
    event.wait()
    # 收到事件后进入运行状态
    print ('%s 收到通知了.' % threading.currentThread().getName())
    print('%s 小伙伴 %s 开始吃咯！'%(time.time(), name))


class myThread (threading.Thread):   # 继承父类threading.Thread
    def __init__(self, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)

        self.people = name

    def run(self):   # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''

        chiHuoGuo(self.people)     # 执行任务
        print("qq交流群：226296743")
        print("结束线程: %s" % threading.currentThread().getName())

# 设置线程组
threads = []
# 创建新线程
thread1 = myThread("a")
thread2 = myThread("b")
thread3 = myThread("c")

# 添加到线程组
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

# 开启线程,遍历集合，准备工作
for thread in threads:
    thread.start()

time.sleep(0.1)
# 发送事件通知
print('集合完毕，人员到齐了，开吃咯！')
event.set()
