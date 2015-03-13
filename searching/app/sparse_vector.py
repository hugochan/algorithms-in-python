#!/usr/bin/env python

import sys
sys.path.append("../")
from linear_probing_hash_st import LinearProbingHashST as HashST

class SparseVector(object):
    """docstring for SparseVector"""
    def __init__(self):
        self.__st = HashST()

    def size(self):
        return st.size()

    def put(self, i, x):
        self.__st.put(i, x)

    def get(self, i):
        if not self.__st.contains(i):
            return 0.0
        else:
            return self.__st.get(i)

    def dot(self, that):
        _sum = 0.0 
        _type = type(that)
        if _type is type([]): # list
            for i in self.__st.keys:
                if i is not None:
                    _sum += that[i]*self.get(i)
        return _sum

if __name__ == '__main__':
    import random
    a = range(10) # [0,1,2,3,4,5,6,7,8,9]
    b = range(10)
    sv = SparseVector()
    index = range(10)
    index = random.sample(index, 5)
    print index
    for i in index:
        sv.put(i, b[i])
    print sv.dot(a)