#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyLists(object):
    def __init__(self, capasity=10):
        self.__data = []
        self.__size = 0
        self.__capasity = capasity

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size < 1

    def __resize(self):
        self.__capasity = 2 * self.__size

    def addElement(self, index, e):
        if self.__size + 1 == self.__capasity:
            self.__resize()
        self.__data.insert(index, e)
        self.__size += 1

    def getCapatity(self):
        return self.__capasity

    def addFitst(self, e):
        self.addElement(0, e)

    def addLast(self, e):
        self.addElement(self.__size - 1, e)

    def find(self, e):
        for index, value in enumerate(self.__data):
            if (value == e):
                return index
        return -1

    def deleteElement(self, index):
        self.__data.pop(index)
        self.__size -= 1

    def deleteLast(self):
        self.__size -= 1
        return self.__data.pop()

    def deleteFirst(self):
        self.__data.pop(0)
        self.__size -= 1

    def setElement(self, index, e):
        self.__data[index] = e

    def toString(self):
        for index, value in enumerate(self.__data):
            print(value, end="")
            if (index != self.__size - 1):
                print(",", end="")


class Dequeu(object):
    def __init__(self):
        self.__data = MyLists()

    def getSize(self):
        return self.__data.getSize()

    def isEmpty(self):
        return self.__data.isEmpty()

    def enDequeu(self, e):
        self.__data.addFitst(e)

    def deDequeu(self):
        self.__data.deleteLast()

    def toString(self):
        print("end:", end="")
        self.__data.toString()
        print(" top:")
