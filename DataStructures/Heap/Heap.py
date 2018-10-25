class Heap:
    def __init__(self):
        self.__data = []
        self.__weight = 0
        self.__size = 0

    def __swap(self, r, l):
        temp = self.__data[r]
        self.__data[r] = self.__data[l]
        self.__data[l] = temp

    def insert(self, item):
        self.__data.append(item)
        self.__shiftUp(self.__size)
        self.__size += 1

    # 索引从0开始
    # 2*i+1  左节点 2*i+2 右节点
    # 父节点 （i-1）//2
    # 最后一个非叶子节点为 (size-2)//2
    # 上浮过程
    def __shiftUp(self, index):
        if index == 0:
            return
        while (index > 0 & self.__data[(index - 1) // 2] < self.__data[index]):
            self.__swap((index - 1) // 2, index)
            index = (index - 1) // 2

    def deleted(self):
        if (self.__size == 0):
            print("the heap is empty")
            return
        self.__swap(0, self.__size - 1)
        self.__shiftdown(0)
        self.__data.pop()
        self.__size -= 1

    def heapprint(self):
        for i in self.__data:
            print(i, end="->")

    def __shiftdown(self, index):
        while (index < (self.__size - 2) // 2):
            child = index * 2 + 1
            if (self.__data[index * 2 + 1] < self.__data[index * 2 + 2]):
                child += 1
            if self.__data[index] < self.__data[child]:
                self.__swap(index, child)
                index = child
            else:
                break


heap = Heap()
for i in range(1, 1001):
    heap.insert(i)

for i in range(1, 1001):
    heap.deleted()

heap.heapprint()
