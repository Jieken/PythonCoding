#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


class Node(object):
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1


class AvlTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def getMax(self, root):
        temp = root
        while temp.right is not None:
            temp = temp.right
        return temp.data

    def getMin(self, root):
        temp = root
        while temp.left is not None:
            temp = temp.left
        return temp.data

    def getHeight(self, node):
        if node is not None:
            return node.height
        return 0

    def insert(self, value):
        self.root = self.__insert(self.root, value)
        return

    def __insert(self, root, value):
        if root is None:
            self.size += 1
            return Node(value)
        if root.data > value:
            root.left = self.__insert(root.left, value)
            if self.getHeight(root.left) - self.getHeight(root.right) == 2:
                if value < root.left.data:
                    root = self.leftRotate(root)
                else:
                    root = self.doubleWithLeftChild(root)
        elif root.data < value:
            root.right = self.__insert(root.right, value)
            if self.getHeight(root.right) - self.getHeight(root.left) == 2:
                if value > root.right.data:
                    root = self.rightRotate(root)
                else:
                    root = self.doubleWithRightChild(root)
        root.height = max(
            self.getHeight(root.left), self.getHeight(root.right)) + 1
        return root

    def remove(self, value):
        self.root = self.__remove(self.root, value)

    def __remove(self, root, value):
        if root is None:
            print("The AvlTree Has No " + str(value) + "!")
            return None
        if root.data > value:
            root.left = self.__remove(root.left, value)
            if self.getHeight(root.right) - self.getHeight(root.left) == 2:
                if self.getHeight(root.right.left) > self.getHeight(
                        root.right.right):
                    root = self.doubleWithRightChild(root)
                else:
                    root = self.rightRotate(root)
        elif root.data < value:
            root.right = self.__remove(root.right, value)
            if self.getHeight(root.left) - self.getHeight(root.right) == 2:
                if self.getHeight(root.left.right) > self.getHeight(
                        root.left.left):
                    root = self.doubleWithLeftChild(root)
                else:
                    root = self.leftRotate(root)
        else:
            # 这里处理找到Node节点
            if (root.left is None):
                self.size -= 1
                return root.right
            elif (root.right is None):
                self.size -= 1
                return root.left
            else:
                minvalue = self.getMin(root.right)
                root.data = minvalue
                root.right = self.__remove(root.right, minvalue)
            root.height = max(
                self.getHeight(root.left), self.getHeight(root.right)) + 1
        return root

    def leftRotate(self, root):
        k1 = root.left
        root.left = k1.right
        k1.right = root
        root.height = max(
            self.getHeight(root.left), self.getHeight(root.right)) + 1
        k1.height = max(self.getHeight(k1.left), self.getHeight(k1.right)) + 1
        return k1

    def rightRotate(self, root):
        k1 = root.right
        root.right = k1.left
        k1.left = root
        root.height = max(
            self.getHeight(root.left), self.getHeight(root.right)) + 1
        k1.height = max(self.getHeight(k1.left), self.getHeight(k1.right)) + 1
        return k1

    def doubleWithLeftChild(self, root):
        root.left = self.rightRotate(root.left)
        return self.leftRotate(root)

    def doubleWithRightChild(self, root):
        root.right = self.leftRotate(root.right)
        return self.rightRotate(root)

    # 中序遍历(深度优先遍历)
    def Preorder(self):
        # 中序遍历
        self.__Preorder(self.root, 1)

    def __Preorder(self, root, val):
        if (root is None):
            return
        self.__Preorder(root.left, val + 1)
        print(root.data, end="->")
        print("当前树高:", end="")
        print(root.height, end="|")
        print("当前层数:", end="")
        print(val)
        self.__Preorder(root.right, val + 1)

    def find(self, value):
        node = self.__find(self.root, value)
        if (node is None):
            print(str(value) + " is not Exit in Avl-Tree")
        else:
            print(str(value) + " is Exit in Avl-Tree")

    def __find(self, root, value):
        if (root is None):
            return None
        if (root.data == value):
            return root
        elif (value < root.data):
            return self.__find(root.left, item)
        else:
            return self.__find(root.right, item)


if __name__ == '__main__':
    a = AvlTree()
    for i in range(100):
        item = random.randint(0, 100)
        a.insert(i)

    for i in range(100):
        item = random.randint(0, 100)
        a.find(item)
        a.remove(item)
        a.find(item)

    a.Preorder()
    print(a.getSize())
