#!/usr/bin/env python
# -*- coding:utf-8 -*-


class LoopDequeu(object):
    def __init__(self):
        self.__Capatity = 2
        self.__data = [self.__Capatity]
        self.__herder = 0
        self.__foot = 0
        self.__size = 0

    def getSize(self):
        return self.__size

    def getCapatity(self):
        return self.__Capatity

    def isEmpty(self):
        return self.__size == 0

    def enDequeu(self, e):
        if ((self.__foot + 1) % self.__Capatity == self.__herder):
            data = []
            herder = self.__herder
            for i in range(0, self.__size):
                data.insert(i, self.__data[herder % self.__Capatity])
                herder += 1
            self.__data = data
            self.__Capatity = 2 * self.__Capatity
            self.__herder = 0
            self.__foot = self.__size

        self.__data.insert(self.__foot, e)
        self.__foot += 1
        self.__size += 1

    def deDequeu(self):
        if ((self.__herder) % self.__Capatity == self.__foot):
            raise RuntimeError("This Dequeue is null!")

        if (self.__size > 0 and (self.__size == (self.__Capatity // 4))):

            date = []
            herder = self.__herder
            for i in range(0, self.__size):
                date.insert(i, self.__data[herder % self.__Capatity])
                herder += 1
            self.__data = date
            self.__Capatity = self.__Capatity // 2
            self.__herder = 0
            self.__foot = self.__size

        self.__data[self.__herder] = -99
        self.__herder += 1
        self.__size -= 1

    def toString(self):
        print("top:", end="")
        herder = self.__herder
        for i in range(self.__size):
            print(self.__data[herder % self.__Capatity], end="")
            if (i < self.__size - 1):
                print("->", end="")
            herder += 1

        print(" end:")


loopdq = LoopDequeu()
for i in range(0, 10000):
    loopdq.enDequeu(i)

loopdq.toString()
print(loopdq.getSize())
print(loopdq.getCapatity())

for i in range(0, 10000):
    loopdq.deDequeu()

loopdq.toString()
print(loopdq.getSize())
print(loopdq.getCapatity())
