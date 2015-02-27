#!/usr/bin/env python

from collections import deque

class Queue(object):
    """docstring for Resizing Queue"""
    def __init__(self):
        self.__queue = deque([])

    def isEmpty(self):
        return len(self.__queue) == 0

    def size(self):
        return len(self.__queue)

    def enqueue(self, item):
        self.__queue.append(item)

    def dequeue(self):
        return self.__queue.popleft()

    def show(self):
        for i in xrange(self.size()):
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