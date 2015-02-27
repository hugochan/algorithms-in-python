#!/usr/bin/env python

import math
class Radix(object):
    """docstring for Radix"""
    def __init__(self):
        self.__bucket = [] # not [[]]*radix

    def sort(self, a, radix=10, type="LSD"):
        """a is a list of integers"""
        _max = self.__max(a)
        K = int(math.ceil(math.log(_max, radix)))
        if type == "LSD":
            self.__sortLSD(a, radix, K)
        elif type == "MSD":
            self.__a = a
            self.__sortMSD(a, radix, K)
        else:
            print "Type error"

    def __sortLSD(self, a, radix, K):
        self.__bucket = [[] for i in xrange(radix)] # not [[]]*radix
        for i in xrange(1, K+1):
            for val in a:
                self.__bucket[val%(radix**i)/(radix**(i-1))].append(val)
            del a[:]
            for each in self.__bucket:
                a.extend(each)
            self.__bucket = [[] for i in xrange(radix)]

    def __sortMSD(self, a, radix, K):# cost much space
        self.__bucket = [[] for i in xrange(radix)] # not [[]]*radix
        if len(a) <= 1:
            self.__a.append(a[0])
            return a
        for val in a:
            self.__bucket[val%(radix**K)/(radix**(K-1))].append(val)
        del a[:]
        for each in self.__bucket:
            if each != []:
                self.__sortMSD(each, radix, K-1)

    def __max(self, a):
        return max(a)

# flat=lambda L: sum(map(flat,L),[]) if isinstance(L,list) else [L] 

if __name__ == '__main__':
    import random
    a = range(108)
    random.shuffle(a)
    print a
    radix = Radix()
    radix.sort(a, 10, "MSD")
    print a[:10]