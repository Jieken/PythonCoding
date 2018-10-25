# !/usr/bin/env python
# -*- coding:utf-8 -*-
from InsertSort import insertSort
import random


# 从 arry[l.....r]区间范围进行快速排序
def quickSort(arry, l, r):
    if r - l < 16:
        insertSort(arry, l, r+1)
        return
    p = partition(arry, l, r)
    quickSort(arry, l, p - 1)
    quickSort(arry, p + 1, r)


# arry[l+1....leftIndex)<=currentValue
# arry(rightIndex....r]>=currentValue
def partition(arry, l, r):
    randomIndex = random.randint(l, r)
    arry[l], arry[randomIndex] = arry[randomIndex], arry[l]
    leftIndex = l + 1
    rightIndex = r
    currentValue = arry[l]
    while True:
        while leftIndex <= r and arry[leftIndex] < currentValue:
            leftIndex += 1
        while rightIndex >= l + 1 and arry[rightIndex] > currentValue:
            rightIndex -= 1
        if leftIndex > rightIndex:
            break
        arry[leftIndex], arry[rightIndex] = arry[rightIndex], arry[leftIndex]
        leftIndex += 1
        rightIndex -= 1
    arry[l], arry[rightIndex] = arry[rightIndex], arry[l]
    return rightIndex


if __name__ == '__main__':
    max = 1000
    list = [random.randint(-max, max) for x in range(max)]
    quickSort(list, 0, len(list) - 1)
    for index, value in enumerate(list):
        if (index > 1):
            if (list[index] < list[index - 1]):
                raise RuntimeError('sortError')
    print(list[0:max])
