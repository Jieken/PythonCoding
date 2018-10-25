#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import random

product = []
cond = threading.Condition()
producers_state = 0
isStop = False


class Producer(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        global isStop
        global producers_state
        count = 0
        for i in range(10):
            cond.acquire()
            while len(product) >= 5:
                cond.wait()
            num = random.random()
            product.append(num)
            cond.notifyAll()
            cond.release()
            print("生产线程" + str(self.id) + ",生产了：" + str(num))
            count = count + 1
            print("生产线程" + str(self.id) + "生产次数为" + str(count))
        cond.acquire()
        # 更新所有消费者队列数量 检查是否全部完成
        producers_state += 1
        print("生产线程" + str(self.id) + "线程结束")
        if (producers_state == 2):
            isStop = True
            # 全部完成需唤醒所有消费者队列准备退出线程
            cond.notifyAll()
        cond.release()


class Consumer(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        global isStop
        count = 0
        while True:
            cond.acquire()
            while isStop is not True and len(product) <= 0:
                cond.wait()
            if isStop is True and len(product) == 0:
                cond.release()
                break
            num = product[0]
            del product[0]
            print("消费线程" + str(self.id) + "，消费了" + str(num))
            count = count + 1
            print("消费线程" + str(self.id) + "消费次数为" + str(count))
            cond.notifyAll()
            cond.release()
        print("消费线程" + str(self.id) + "线程结束")


print("主线程开始")
p1 = Producer(1)
p2 = Producer(2)
p1.start()
p2.start()
c1 = Consumer(1)
c2 = Consumer(2)
c3 = Consumer(3)
c1.start()
c2.start()
c3.start()
p1.join()
p2.join()
c1.join()
c2.join()
c3.join()
print("主线程结束")
