#!/usr/bin/env python

import random

class SelectKMin(object):
    """docstring for SelectKMin: select the Kth minimal element"""

    def select(self, a, k):
        k = k - 1
        random.shuffle(a)
        lo = 0
        hi = len(a) - 1
        while (hi > lo):
            j = self.__partition(a, lo, hi)
            if j == k:
                return a[k]
            elif j > k:
                hi = j - 1
            elif j < k:
                lo = j + 1
        return a[k]

    def __partition(self, a, lo, hi):
        i = lo
        j = hi + 1
        v = a[lo]# partition element
        while True:
            while self.__less(a[i+1], v):
                i += 1
                if i == hi:
                    break
            i += 1
            while self.__less(v, a[j-1]):
                j -= 1
                if j == lo:
                    break
            j -= 1
            if i >= j:
                break
            self.__exch(a, i, j)
        self.__exch(a, lo, j)
        return j

    def __less(self, v, w):
        return v < w # to be generalized

    def __exch(self, a, i, j):
        t = a[i] # to be generalized
        a[i] = a[j]
        a[j] = t

if __name__ == '__main__':
    a = range(10)
    random.shuffle(a)
    print a
    skm = SelectKMin()
    print skm.select(a, 3)
    