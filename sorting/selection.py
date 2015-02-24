#!/usr/bin/env python

class Selection(object):
    """docstring for Selection"""
    def sort(self, a):
        N = len(a)
        for i in range(N):
            _min = i
            for j in range(i+1, N):
                if self.__less(a[j], a[_min]):
                    _min = j
            self.__exch(a, i, _min)

    def __less(self, v, w):
        return v < w # to be generialized

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
    s = Selection()
    s.sort(a)
    print a
    print s.isSorted(a)