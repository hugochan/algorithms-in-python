#!/usr/bin/env python

class Quick(object):
    """docstring for Quick: standard & 3way"""
    def sort(self, a, type="standard"):
        random.shuffle(a) # reduce independencies on input
        if type == "standard":
            self.__sort(a, 0, len(a)-1)
        elif type == "3way":
            self.__sort3(a, 0, len(a)-1)
        else:
            print "Error"

    def __sort(self, a, lo, hi):
        if hi <= lo:
            return 0
        j = self.__partition(a, lo, hi)
        self.__sort(a, lo, j-1)
        self.__sort(a, j+1, hi)

    def __sort3(self, a, lo, hi):
        if hi <= lo:
            return 0
        [lt, gt] = self.__partition3(a, lo, hi)
        self.__sort3(a, lo, lt-1)
        self.__sort3(a, gt+1, hi)


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

    def __partition3(self, a, lo, hi):
        lt = lo
        i = lo + 1
        gt = hi
        v = a[lo]
        while i <= gt:
            _cmp = self.__compare(a[i], v)
            if _cmp < 0:
                self.__exch(a, lt, i)
                lt += 1
                i += 1
            elif _cmp > 0:
                self.__exch(a, i, gt)
                gt -= 1
            else:
                i += 1
        return [lt, gt] 

    def __less(self, v, w):
        return v < w # to be generalized

    def __compare(self, v, w):
        if v < w: # to be generalized
            return -1
        elif v > w:
            return 1
        else:
            return 0

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
    s = Quick()
    s.sort(a, "3way")
    print a
    print s.isSorted(a)