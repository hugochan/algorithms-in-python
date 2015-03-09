#!/usr/bin/env python

from sequential_search_st import SequentialSearchST as ssst

class SeparateChainingHashST(object):
    """docstring for SeparateChainingHashST"""
    def __init__(self, M=997):
        self.__M = M
        self.st = [0]*self.__M
        for i in xrange(self.__M):
            self.st[i] = ssst()

    def get(self, key):
        return self.st[self.__hash(key)].get(key)

    def put(self, key, val):
        self.st[self.__hash(key)].put(key, val)

    def __hash(self, key):
        return (hash(key) & 0x7fffffff) % self.__M

if __name__ == '__main__':
    import random
    keys = range(10)
    vals = range(100, 110)
    random.shuffle(keys)
    random.shuffle(vals)
    print keys, vals
    st = SeparateChainingHashST(7)
    for i in xrange(10):
        st.put(keys[i], vals[i])
    for i in xrange(9, -1, -1):
        print keys[i], st.get(keys[i])