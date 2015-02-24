#!/usr/bin/env python

class Merge(object):
    """docstring for Merge: Top-Down & Bottom-Up"""
    def sort(self, a, type="TD"):
        self.aux = []
        if type == "TD":
            self.__sortTD(a, 0, len(a)-1)
        elif type == "BU":
            self.__sortBU(a, 0, len(a)-1)
        else:
            print "Error"

    def __sortTD(self, a, lo, hi):
        if hi <= lo:
            return 0
        mid = lo + (hi - lo)/2
        self.__sortTD(a, lo, mid)
        self.__sortTD(a, mid+1, hi)
        self.__merge(a, lo, mid, hi)

    def __sortBU(self, a, lo, hi):
        N = len(a)
        sz = 1
        while sz < N:
            for lo in range(0, N-sz, sz+sz):
                self.__merge(a, lo, lo+sz-1, min(lo+sz+sz-1, N-1))
            sz = sz + sz

    def __merge(self, a, lo, mid, hi):
        i = lo
        j = mid + 1
        aux = a[:]
        for k in range(lo, hi+1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif self.__less(aux[j], aux[i]):
                a[k] = aux[j]
                j += 1
            else:
                a[k] = aux[i]
                i += 1

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
    s = Merge()
    s.sort(a, "BU")
    print a
    print s.isSorted(a)