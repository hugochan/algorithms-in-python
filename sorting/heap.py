#!/usr/bin/env python

class Heap(object):
    """docstring for Heap"""
    def sort(self, a):
        N = len(a)
        for i in xrange(N/2, 0, -1):
            self.__sink(a, i, N)
        while N > 1:
            self.__exch(a, 1, N)
            N -= 1
            self.__sink(a, 1, N)

    def __sink(self, a, k, N):
        while 2*k <= N:
            j = 2*k
            if j < N and self.__less(a, j, j+1):
                j += 1
            if not self.__less(a, k, j):
                break
            self.__exch(a, k, j)
            k = j

    def __less(self, a, i, j):
        return a[i-1] < a[j-1] # to be generalized

    def __exch(self, a, i, j):
        a[i-1], a[j-1] = a[j-1], a[i-1]

    def isSorted(self, a):
        for i in xrange(1, len(a)):
            if self.__less(a, i+1, i):
                return False
        return True

if __name__ == '__main__':
    import random
    a = range(10)
    random.shuffle(a)
    print a
    s = Heap()
    s.sort(a)
    print s.isSorted(a)
    print a