#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import multiprocessing
from bs4 import BeautifulSoup
import os
import sys

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

cond = multiprocessing.Condition()
queue = multiprocessing.Queue()
sys.setrecursionlimit(1000000)


def mkdir(path):
    folder = os.path.exists(path)
    if folder is False:
        os.makedirs(path)


def Jobrun(queue):
    result = requests.get(url, headers=headers)
    html = BeautifulSoup(result.content, "html.parser")
    td = html.find_all("td")
    for i in td:
        isTrue = False
        for j in i.children:
            if j.name == 'small' or j.name == 'i':
                isTrue = True
                break
        if (isTrue):
            # while len(dit) >= 5:
            #     cond.wait()
            queue.put((i.find("small").string, i.find("a").attrs["href"],
                       i.find("a").string))
            print("生产者,生产了：" + i.find("a").attrs["href"])


def Coustomrun(queue):
    while True:
        result = queue.get()
        num = result[0]
        url = "http://pages.cs.wisc.edu/~remzi/OSTEP/" + result[1]
        path = os.getcwd() + "\\Os-tep"
        mkdir(path)
        if os.path.exists(path + "\\" + str(num) + "-" + result[1]) is False:
            ssss = requests.get(url, stream=True)
            with open(path + "\\" + str(num) + "-" + result[1], 'wb') as fd:
                for chunk in ssss.iter_content(1024):
                    fd.write(chunk)
        print("消费者，消费了" + str(result))


if __name__ == '__main__':
    print("开始爬取")
    p1 = multiprocessing.Process(target=Jobrun, args=(queue, ))
    p1.start()
    Couston = []
    for i in range(5):
        Couston.append(multiprocessing.Process(target=Coustomrun, args=(queue, )))
    for i in Couston:
        i.start()
    p1.join()
    for i in Couston:
        i.terminate()
    # c1.join()
    print("爬取完成")
