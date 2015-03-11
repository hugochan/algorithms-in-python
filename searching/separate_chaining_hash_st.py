#!/usr/bin/env python

from sequential_search_st import SequentialSearchST as ssst
from data import array
import math

class SeparateChainingHashST(object):
    """docstring for SeparateChainingHashST"""
    def __init__(self, M=997):
        self.__N = 0
        self.M = M
        self.st = [0]*self.M
        for i in xrange(self.M):
            self.st[i] = ssst()

    def get(self, key):
        return self.st[self.__hash(key)].get(key)

    def put(self, key, val):
        if self.__N >= 2*self.M:
            self.__resize(2*self.M)
        if self.st[self.__hash(key)].put(key, val):
            self.__N += 1

    def delete(self, key):
        if self.st[self.__hash(key)].delete(key):
            self.__N -= 1
        if self.__N > 0 and self.__N <= self.M/8:
            self.__resize(self.M/2)

    def size(self):
        return self.__N

    def show(self):
        for i in xrange(0, self.M):
            x = self.st[i].first
            while x is not None:
                print x.key, x.val
                x = x.next

    def __hash(self, key):
        # return (hash(key) & 0x7fffffff) % self.M
        t = hash(key) & 0x7fffffff
        if math.log(self.M, 2) < 26:
            t = t % array[int(math.log(self.M, 2))+5]
        return t % self.M

    def __resize(self, cap):
        t = SeparateChainingHashST(cap)
        for i in xrange(0, self.M):
            x = self.st[i].first
            while x is not None:
                t.put(x.key, x.val)
                x = x.next
        self.st = t.st
        self.M = t.M

if __name__ == '__main__':
    import random
    keys = range(10)
    vals = range(100, 110)
    random.shuffle(keys)
    random.shuffle(vals)
    print keys, vals
    st = SeparateChainingHashST()
    for i in xrange(10):
        st.put(keys[i], vals[i])
    st.show()
    for i in xrange(9, -1, -1):
        print st.get(keys[i])
    st.delete(keys[0])
    print st.get(keys[0])
    print st.size()