#!/usr/bin/env python

from collections import deque

class MaxPQ(object):
    """docstring for resizing MaxPQ"""
    def __init__(self):
        self.__pq = deque([0])

    def isEmpty(self):
        return len(self.__pq) - 1 == 0

    def size(self):
        return len(self.__pq) - 1

    def insert(self, v):
        self.__pq.append(v)
        self.__swim(self.size())

    def delMax(self):
        _max = self.__pq[1]
        self.__exch(1, self.size())
        del self.__pq[-1]
        self.__sink(1)
        return _max

    def show(self):
        for i in xrange(1, self.size()+1):
            print self.__pq[i]

    def __swim(self, k):
        while k > 1 and self.__less(k/2, k):
            self.__exch(k/2, k)
            k = k/2

    def __sink(self, k):
        N = self.size()
        while 2*k <= N:
            j = 2*k
            if j < N and self.__less(j, j+1):
                j += 1
            if not self.__less(k, j):
                break
            self.__exch(k, j)
            k = j

    def __less(self, i, j):
        return self.__pq[i] < self.__pq[j] # to be generalized

    def __exch(self, i, j):
        self.__pq[i], self.__pq[j] = self.__pq[j], self.__pq[i]

if __name__ == '__main__':
    import random
    maxN = 10
    pq = MaxPQ()
    a = range(100)
    random.shuffle(a)
    print a
    for i in a:
        pq.insert(i)
        if pq.size() > maxN:
            pq.delMax()
    print pq.isEmpty()
    pq.show()