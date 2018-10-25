#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

from InsertSort import insertSort


def threeQuickSort(arry, l, r):
    if r - l < 16:
        insertSort(arry, l, r + 1)
        return
    randomIndex = random.randint(l, r)
    arry[l], arry[randomIndex] = arry[randomIndex], arry[l]
    v = arry[l]
    lt = l  # arr[l+1...lt] < v
    gt = r + 1  # arr[gt...r] > v
    i = l + 1  # arr[lt+1...i) == v
    while i < gt:
        if arry[i] < v:
            lt += 1
            arry[lt], arry[i] = arry[i], arry[lt]
            i += 1
        elif arry[i] > v:
            gt -= 1
            arry[gt], arry[i] = arry[i], arry[gt]
        else:
            i += 1
    arry[lt], arry[l] = arry[l], arry[lt]
    threeQuickSort(arry, l, lt)
    threeQuickSort(arry, gt, r)


if __name__ == '__main__':
    max = 100000
    list = [random.randint(-max, max) for x in range(max)]
    threeQuickSort(list, 0, len(list) - 1)
    for index, value in enumerate(list):
        if (index > 1):
            if (list[index] < list[index - 1]):
                raise RuntimeError('sortError')
    print(list[0:max])
