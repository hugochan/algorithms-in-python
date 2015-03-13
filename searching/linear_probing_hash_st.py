#!/usr/bin/env python

from data import array
import math

class LinearProbingHashST(object):
    """docstring for LinearProbingHashST"""
    def __init__(self, M=16):
        self.__N = 0 # number of key-vals
        self.M = M # size of linear probing table
        self.keys = [None]*self.M
        self.vals = [None]*self.M

    def put(self, key, val):
        if self.__N >= self.M/2:
            self.__resize(2*self.M)
        i = self.__hash(key)
        while self.keys[i] is not None:
            if self.__compare(self.keys[i], key) is 0:
                self.vals[i] = val
                return None
            i = (i + 1) % self.M
        self.keys[i] = key
        self.vals[i] = val
        self.__N += 1

    def get(self, key):
        i = self.__hash(key)
        while self.keys[i] is not None:
            if self.__compare(self.keys[i], key) is 0:
                return  self.vals[i]
            i = (i + 1) % self.M
        return None

    def delete(self, key):
        if not self.contains(key):
            return None
        i = self.__hash(key)
        while self.__compare(key, self.keys[i]) is not 0:
            i = (i + 1) % self.M
        self.keys[i] = None
        self.vals[i] = None
        i = (i + 1) % self.M
        while self.keys[i] is not None:
            keyToRedo = self.keys[i]
            valToRedo = self.vals[i]
            self.keys[i] = None
            self.vals[i] = None
            self.__N -= 1
            self.put(keyToRedo, valToRedo)
            i = (i + 1) % self.M
        self.__N -= 1
        if self.__N > 0 and self.__N == self.M/8:
            self.__resize(M/2)

    def contains(self, key):
        return self.get(key) is not None

    def size(self):
        return self.__N

    def show(self):
        for i in self.keys:
            if i is not None:
                print i, self.get(i)

    def __hash(self, key):
        # return (hash(key) & 0x7fffffff) % self.M
        t = hash(key) & 0x7fffffff
        if math.log(self.M, 2) < 26:
            t = t % array[int(math.log(self.M, 2))+5]
        return t % self.M

    def __resize(self, cap):
        t = LinearProbingHashST(cap)
        for i in xrange(0, self.M):
            if self.keys[i] is not None:
                t.put(self.keys[i], self.vals[i])
        self.keys = t.keys
        self.vals = t.vals
        self.M = t.M

    def __compare(self, v, w):
        if v < w: # to be generalized
            return -1
        elif v > w:
            return 1
        else:
            return 0

if __name__ == '__main__':
    import random
    keys = range(10)
    vals = range(100, 110)
    random.shuffle(keys)
    random.shuffle(vals)
    print keys, vals
    st = LinearProbingHashST(7)
    import pdb
    # pdb.set_trace()
    for i in xrange(10):
        st.put(keys[i], vals[i])
    for i in xrange(9, -1, -1):
        print keys[i], st.get(keys[i])
    st.delete(keys[9])
    print st.get(keys[9])
    print st.size()
    st.show()