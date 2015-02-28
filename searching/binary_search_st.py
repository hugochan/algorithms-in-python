#!/usr/bin/env python

class BinarySearchST(object):
    """docstring for BinarySearchST"""
    def __init__(self):
        self.__keys = []
        self.__vals = []

    def size(self):
        """get the size of the ST"""
        return len(self.__keys)

    def isEmpty(self):
        return self.size() is 0

    def get(self, key):
        """get a value corresponding to key"""
        if self.isEmpty():
            return None
        i = self.__rank(key)
        if i < self.size() and self.__compare(self.__keys[i], key) is 0:
            return vals[i]
        else:
            return None

    def put(self, key, val):
        """add a key-value"""
        i = self.__rank(key)
        N = self.size()
        if i < N and self.__compare(self.__keys[i], key) is 0:
            self.__vals[i] = val
            return None
        self.__keys.insert(i, key) # computation complexity: O(N)
        self.__vals.insert(i, val)

    def delete(self, key):
        """delete a key-value"""
        if self.isEmpty():
            return None
        i = self.__rank(key)
        if i < self.size() and self.__compare(self.__keys[i], key) is 0:
            del self.__keys[i]
            del self.__vals[i]
        else:
            return None

    def min(self):
        """get the minimal key"""
        if self.isEmpty():
            return None
        return self.__keys[0]

    def max(self):
        """get the maximal key"""
        if self.isEmpty():
            return None
        return self.__keys[-1]

    def select(self, k):
        """select the kth minimal key"""
        if k >= self.size():
            return None
        return self.__keys[k]

    def ceiling(self, key):
        """get the minimal key_m larger than key"""
        if self.isEmpty():
            return None
        return self.__keys[self.__rank(key)]

    def floor(self, key):
        """get the maximal key_m smaller than key"""
        if self.isEmpty():
            return None
        i = self.__rank(key)
        if self.__compare(self.__keys[i], key) is 0:
            return key
        else:
            return self.__keys[i-1]

    def show(self):
        """print the ST"""
        for i in xrange(self.size()):
            print self.__keys[i], self.__vals[i] 

    def __rank(self, key):
        """get the number of keys smaller than key"""
        lo, hi = 0, self.size() - 1
        while lo <= hi:
            mid = lo + (hi - lo)/2
            _cmp = self.__compare(key, self.__keys[mid])
            if _cmp < 0:
                hi = mid - 1
            elif _cmp > 0:
                lo = mid + 1
            else:
                return mid
        return lo

    def __compare(self, v, w):
        if v < w: # to be generalized
            return -1
        elif v > w:
            return 1
        else:
            return 0

if __name__ == '__main__':
    import random
    bs = BinarySearchST()
    keys = range(10)
    vals = range(100, 110)
    random.shuffle(keys)
    random.shuffle(vals)
    print keys, vals
    for i in xrange(10):
        bs.put(keys[i], vals[i])
    bs.show()
    print bs.get(0)
    print bs.ceiling(3.5)
    print bs.floor(3.5)
    bs.delete(3)
    bs.show()