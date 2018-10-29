#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import threading
from bs4 import BeautifulSoup
import os

url = "http://pages.cs.wisc.edu/~remzi/OSTEP/"
headers = {
    'Origin':
    'http://192.168.1.102:1999',
    'Accept-Encoding':
    'gzip, deflate',
    'Accept-Language':
    'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type':
    'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept':
    'text/plain, */*; q=0.01',
    'Referer':
    'http://192.168.1.102:1999/Login/Index?isLogin=0.47421094637510164',
    'X-Requested-With':
    'XMLHttpRequest',
    'Connection':
    'keep-alive',
}
dit = []
cond = threading.Condition()
IsStop = False


def mkdir(path):
    folder = os.path.exists(path)
    if folder is False:
        os.makedirs(path)


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.result = requests.get(url, headers=headers)
        self.html = BeautifulSoup(self.result.content, "html.parser")
        self.td = self.html.find_all("td")

    def run(self):
        for i in self.td:
            isTrue = False
            for j in i.children:
                if j.name == 'small' or j.name == 'i':
                    isTrue = True
                    break
            if (isTrue):
                cond.acquire()
                # while len(dit) >= 20:
                #     cond.wait()
                dit.append((i.find("small").string, i.find("a").attrs["href"],
                            i.find("a").string))
                print("生产者,生产了：" + i.find("a").attrs["href"])
                cond.notifyAll()
                cond.release()
        # 生产者线程完成 唤醒所有消费者结束进程
        cond.acquire()
        cond.notifyAll()
        cond.release()


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            cond.acquire()
            while len(dit) <= 0:
                cond.wait()
            result = dit[0]
            del dit[0]
            num = result[0]
            url = "http://pages.cs.wisc.edu/~remzi/OSTEP/" + result[1]
            path = os.getcwd() + "\\Os-tep"
            mkdir(path)
            if os.path.exists(path + "\\" + str(num) + "-" +
                              result[1]) is False:
                ssss = requests.get(url, stream=True)
                with open(path + "\\" + str(num) + "-" + result[1],
                          'wb') as fd:
                    for chunk in ssss.iter_content(1024):
                        fd.write(chunk)
            print("消费者，消费了" + str(result))
            # cond.notify()
            cond.release()


print("开始爬取")
p1 = Producer()
p1.start()
for i in range(5):
    Consumer().start()
p1.join()
print("爬取完成")