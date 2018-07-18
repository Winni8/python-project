# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/7/12 15:57
# @File 	:event1.py
# @Software :PyCharm


import threading
import time

event = threading.Event()


def chihuoguo(name):
    # 等待事件，进入等待阻塞状态
    print('%s 已经启动' % threading.currentThread().getName(), time.ctime())
    print('小伙伴 %s 已经进入就餐状态！' % name)
    time.sleep(1)
    event.wait()  # ===》收到通知后才会有继续往下走
    # 收到事件后进入运行状态
    print('%s 收到通知了.' % threading.currentThread().getName(), time.ctime())
    print('小伙伴 %s 开始吃咯！' % name)

# 设置线程组
threads = []

# 创建新线程
thread1 = threading.Thread(target=chihuoguo, args=("a", ))
thread2 = threading.Thread(target=chihuoguo, args=("b", ))

# 添加到线程组
threads.append(thread1)
threads.append(thread2)

# 开启线程
for thread in threads:
    thread.start()

# for thread in threads:
#     thread.join()

time.sleep(0.1)
# 发送事件通知
print('主线程通知小伙伴开吃咯！')
event.set()  # 若果没有等待事件，程序将一直等待下去；将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。
