#!/usr/bin/env python

class Insertion(object):
    """docstring for Insertion"""
    def sort(self, a):
        N = len(a)
        for i in range(1, N):
            for j in range(i, 0, -1):
                if self.__less(a[j], a[j-1]):
                    self.__exch(a, j, j-1)
                else:
                    break

    def __less(self, v, w):
        return v < w # to be generalized

    def __exch(self, a, i, j):
        t = a[i] # to be generalized
        a[i] = a[j]
        a[j] = t

    def isSorted(self, a):
        for i in range(1, len(a)):
            if self.__less(a[i], a[i-1]):
                return False
        return True

if __name__ == '__main__':
    import random
    a = range(10)
    random.shuffle(a)
    print a
    s = Insertion()
    s.sort(a)
    print a
    print s.isSorted(a)