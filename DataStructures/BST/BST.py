#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
from queue import Queue


class Node:
    def __init__(self, item):
        self.item = item
        self.Left = None
        self.Right = None
        self.Height = 1
        self.Order = 1


class BST(object):
    def __init__(self):
        self.__root = None
        self.__size = 0

    def GetHeight(self, node):
        if node is None:
            return 0
        return node.Height

    def Add(self, item):
        self.__root = self.__Add(self.__root, item)

    def __Add(self, node, item):
        if (node is None):
            self.__size += 1
            return Node(item)
        if (item < node.item):
            node.Left = self.__Add(node.Left, item)
        elif (item > node.item):
            node.Right = self.__Add(node.Right, item)
        node.Height = 1 + max(
            self.GetHeight(node.Left), self.GetHeight(node.Right))

        return node

    def Delete(self, item):
        self.__root = self.__Delete(self.__root, item)

    # 删除以node为根节点中item的元素。返回根节点
    def __Delete(self, node, item):
        if (node is None):
            print("value is not exit")
            return
        if (item < node.item):
            node.Left = self.__Delete(node.Left, item)
        elif (item > node.item):
            node.Right = self.__Delete(node.Right, item)
        else:
            # 这里处理找到Node节点
            if (node.Left is None):
                self.__size -= 1
                return node.Right
            elif (node.Right is None):
                self.__size -= 1
                return node.Left
            else:
                value = self.__FindMini(node.Right)
                node.item = value
                node.Right = self.__Delete(node.Right, value)
        node.Height = 1 + max(
            self.GetHeight(node.Left), self.GetHeight(node.Right))
        return node

    def Find(self, item):
        node = self.__Find(self.__root, item)
        if (node is None):
            print("value is not exit")
        else:
            print("is exit")

    def __Find(self, node, item):
        if (node is None):
            return None
        if (node.item == item):
            return node
        elif (item < node.item):
            return self.__Find(node.Left, item)
        else:
            return self.__Find(node.Right, item)

    def FindMini(self):
        return self.__FindMini(self.__root)

    def __FindMini(self, node):
        if (node.Left is None):
            return node.item
        return self.__FindMini(node.Left)

    def FindMax(self):
        return self.__FindMax(self.__root)

    def __FindMax(self, node):
        if (node.Right is None):
            return node.item
        return self.__FindMax(node.Right)

    def GetSize(self):
        return self.__size

    # 中序遍历(深度优先遍历)
    def Preorder(self):  # 中序遍历
        self.__Preorder(self.__root, 1)

    def __Preorder(self, node, val):
        if (node is None):
            return
        self.__Preorder(node.Left, val + 1)

        print(node.item, end="->")
        print("当前树高:", end="")
        print(node.Height, end="|")
        print("当前层数:", end="")
        print(val)
        node.Order = val
        self.__Preorder(node.Right, val + 1)

    # 层序遍历(广度优先遍历)
    def BreadthFirstSearch(self):
        dequeu = Queue()
        dequeu.put(self.__root)
        val = self.__root.Order
        while (not dequeu.empty()):
            node = dequeu.get()
            if (node is not None):
                if node.Order == val:
                    print(node.item, end="-")
                else:
                    print("\n", end="")
                    val += 1
                    print(node.item, end="-")
                if (node.Left is not None):
                    dequeu.put(node.Left)
                if (node.Right is not None):
                    dequeu.put(node.Right)


a = BST()
for i in range(10):
    item = random.randint(0, 100)
    a.Add(item)

print(a.GetSize())
print(a.FindMini())
print(a.FindMax())
a.Preorder()
a.BreadthFirstSearch()
print("")
a.Find(15)
a.Delete(15)
print(a.GetSize())
a.Preorder()
print("")
a.BreadthFirstSearch()
