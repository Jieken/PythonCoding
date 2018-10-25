#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


# def insertSort(arry):
#     for i in range(1, len(arry)):
#         currentValue = arry[i]
#         position = i
#         while position > 0 and currentValue < arry[position - 1]:
#             arry[position] = arry[position - 1]
#             position -= 1
#         arry[position] = currentValue
#     return arry

# 此函数供其他排序算法调用
def insertSort(arry, l, r):
    for i in range(l + 1, r):
        currentValue = arry[i]
        position = i
        while position > l and currentValue < arry[position - 1]:
            arry[position] = arry[position - 1]
            position -= 1
        arry[position] = currentValue
    return arry


if __name__ == '__main__':
    max = 5000
    list = [random.randint(-max, max) for x in range(max)]
    list = insertSort(list)
    for index, value in enumerate(list):
        if (index > 1):
            if (list[index] < list[index - 1]):
                raise RuntimeError('sortError')
    list2 = [random.randint(-max, max) for x in range(5000)]
    insertSort(list2, 0, 5000)
    for index, value in enumerate(list2):
        if (index > 1):
            if (list2[index] < list2[index - 1]):
                raise RuntimeError('sortError')
    for i in list2:
        print(i)
