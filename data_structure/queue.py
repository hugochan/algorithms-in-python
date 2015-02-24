#!/usr/bin/env python

class Queue(object):
    """docstring for Resizing Queue"""
    def __init__(self):
        self.__queue = []

    def isEmpty(self):
        return len(self.__queue) == 0

    def size(self):
        return len(self.__queue)

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        item = self.__queue[0]
        del self.__queue[0]
        return item

    def show(self):
        for i in range(self.size()):
            print self.__queue[i]

if __name__ == '__main__':
    import random
    queue = Queue()
    a = range(10)
    random.shuffle(a)
    print a
    for i in a:
        queue.enqueue(i)
    for i in range(10):
        print queue.dequeue()
    print queue.isEmpty()
    queue.show()