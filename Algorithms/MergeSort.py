#!/usr/bin/env python
# -*- coding:utf-8 -*-

from InsertSort import insertSort
import random


# arry[l.....r)进行归并排序
def mergeSort(arry, l, r):
    sortLegth = r - l
    if (sortLegth < 16):
        insertSort(arry, l, r)
        return
    mid = sortLegth // 2 + l
    mergeSort(arry, l, mid)
    mergeSort(arry, mid, r)
    if arry[mid - 1] < arry[mid]:
        return
    merge(arry, l, mid, r)


# 归并过程
def merge(arry, l, mid, r):
    left = 0
    right = mid - l
    list = arry[l:r]
    for i in range(l, r):
        if left > mid - l - 1:
            arry[i] = list[right]
            right += 1
        elif right > len(list) - 1:
            arry[i] = list[left]
            left += 1
        elif list[left] <= list[right]:
            arry[i] = list[left]
            left += 1
        elif list[left] > list[right]:
            arry[i] = list[right]
            right += 1
    return


if __name__ == '__main__':
    max = 10000
    list = [random.randint(-max, max) for x in range(max)]
    mergeSort(list, 0, len(list))
    for index, value in enumerate(list):
        if (index > 1):
            if (list[index] < list[index - 1]):
                raise RuntimeError('sortError')
    print(list[0:max])
