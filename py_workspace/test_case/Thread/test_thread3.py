# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/29 14:55
# @File 	:test_thread3.py
# @Software :PyCharm
# 时刻记住进程是一个任务，一个任务里可以有多个线程; 这个程序无法输出时间也不知道是什么原因；草

import threading
from time import sleep, ctime


# 创建超级播放器
def super_player(file, time):
    for i in range(2):
        print('Start playing： %s! %s' % (file, ctime()))
        sleep(time)
        print("end playing 名字：{}-时间：{}".format(file, ctime()))


dict = {'爱情买卖.mp3': 5, '阿凡达.mp4': 4, '我和你.mp3': 3, "test-thraed": 2}

threads = []
files = range(len(dict))
print(files)

for file, time in dict.items():
    t = threading.Thread(target=super_player, args=(file, time))
    threads.append(t)

if __name__ == '__main__':
    import time
    # 启动线程
    a = time.clock()
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()
    print('all end: %s ' % ctime())
    b = time.clock()
    print(b-a)

