#!/usr/bin/env python

class Shell(object):
    """docstring for Shell"""
    def sort(self, a):
        N = len(a)
        h = 1
        while h < N/3:
            h = 3*h + 1
        while h >= 1:
            for i in xrange(h, N):
                for j in xrange(i, h-1, -h):
                    if self.__less(a[j], a[j-h]):
                        self.__exch(a, j, j-h)
                    else:
                        break
            h = h/3


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
    s = Shell()
    s.sort(a)
    print a
    print s.isSorted(a)