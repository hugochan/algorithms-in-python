#!/usr/bin/env python

class Selection(object):
    """docstring for Selection"""
    def sort(self, a):
        N = len(a)
        for i in xrange(N):
            _min = i
            for j in xrange(i+1, N):
                if self.__less(a[j], a[_min]):
                    _min = j
            self.__exch(a, i, _min)

    def __less(self, v, w):
        return v < w # to be generialized

    def __exch(self, a, i, j):
        a[i], a[j] = a[j], a[i]

    def isSorted(self, a):
        for i in xrange(1, len(a)):
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