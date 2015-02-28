#!/usr/bin/env python

class Node(object):
    """docstring for Node"""
    def __init__(self, key, val, N):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.N = N

class BinarySearchTree(object):
    """docstring for BinarySearchTree"""
    def __init__(self):
        self.__root = None
        

    def size(self):
        return self.__size(self.__root)

    def __size(self, x):
        if x is None:
            return 0
        else:
            return x.N

    def get(self, key):
        x = self.__root
        while x is not None:
            _cmp = self.__compare(key, x.key)            
            if _cmp == 0:
                return x.val
            elif _cmp < 0:
                x = x.left
            else:
                x = x.right
        return None

    def put(self, key, val):
        self.__root = self.__put(self.__root, key, val)

    def __put(self, x, key, val):
        if x == None:
            return Node(key, val, 1)
        _cmp = self.__compare(key, x.key)
        if _cmp < 0:
            x.left = self.__put(x.left, key, val)
        elif _cmp > 0:
            x.right = self.__put(x.right, key, val)
        else:
            x.val = val
        x.N = self.__size(x.left) + self.__size(x.right) + 1
        return x

    def max(self):
        return self.__max(self.__root).key

    def __max(self, x):
        if x.right is None:
            return x
        else:
            return self.__max(x.right)

    def min(self):
        return self.__min(self.__root).key

    def __min(self, x):
        if x.left is None:
            return x
        else:
            return self.__min(x.left)

    def floor(self, key):
        x = self.__floor(self.__root, key)
        if x is None:
            return None
        else:
            return x.key

    def __floor(self, x, key):
        if x is None:
            return None
        _cmp = self.__compare(key, x.key)
        if _cmp == 0:
            return x
        elif _cmp < 0:
            return self.__floor(x.left, key)
        t = self.__floor(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def ceiling(self, key):
        x = self.__celling(self.__root, key)
        if x is None:
            return None
        else:
            return x.key

    def __celling(self, x, key):
        if x is None:
            return None
        _cmp = self.__compare(key, x.key)
        if _cmp == 0:
            return x
        elif _cmp > 0:
            return self.__celling(x.right, key)
        t = self.__celling(x.left, key)
        if t is not None:
            return t
        else:
            return x

    def select(self, k):
        return self.__select(self.__root, k).key

    def __select(self, x, k):
        if x is None:
            return None
        t = self.__size(x.left)
        if t > k:
            return self.__select(x.left, k)
        elif t < k:
            return self.__select(x.right, k-t-1)
        else:
            return x

    def rank(self, key):
        return self.__rank(self.__root, key)

    def __rank(self, x, key):
        if x is None:
            return 0
        _cmp = self.__compare(key, x.key)
        if _cmp < 0:
            return self.__rank(x.left, key)
        elif _cmp > 0:
            return 1 + self.__size(x.left) + self.__rank(x.right, key)
        else:
            return self.__size(x.left)

    def delete(self, key):
        self.__root = self.__delete(self.__root, key)

    def __delete(self, x, key):
        if x is None:
            return None
        _cmp = self.__compare(key, x.key)
        if _cmp < 0:
            x.left = self.__delete(x.left, key)
        elif _cmp > 0:
            x.right = self.__delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            elif x.left is None:
                return x.right
            t = x
            x = self.__min(t.right)
            x.right = self.__deleteMin(t.right)
            x.left = t.left
        x.N = self.__size(x.left) + self.__size(x.right) + 1
        return x

    def deleteMin(self):
        self.__root = self.__deleteMin(self.__root)

    def __deleteMin(self, x):
        if x.left is None:
            return x.right
        x.left = self.__deleteMin(x.left)
        x.N = self.__size(x.left) + self.__size(x.right) + 1
        return x

    def deleteMax(self):
        self.__root = self.__deleteMax(self.__root)

    def __deleteMax(self, x):
        if x.right is None:
            return x.left
        x.right = self.__deleteMax(x.right)
        x.N = self.__size(x.left) + self.__size(x.right) + 1
        return x

    def keys(self, lo=None, hi=None):
        if lo is None and hi is None:
            return self.keys(self.min(), self.max())
        else:
            queue = []
            self.__keys(self.__root, queue, lo, hi)
            return queue

    def __keys(self, x, queue, lo, hi):
        if x is None:
            return None
        cmplo = self.__compare(lo, x.key)
        cmphi = self.__compare(hi, x.key)
        if cmplo < 0:
            self.__keys(x.left, queue, lo, hi)
        if cmplo <= 0 and cmphi >= 0:
            queue.append(x.key)
        if cmphi > 0:
            self.__keys(x.right, queue, lo, hi)

    def show(self):
        """print the bst"""
        self.__print(self.__root)

    def __print(self, x):
        if x is None:
            return None
        self.__print(x.left)
        print x.key
        self.__print(x.right)             

    def __compare(self, v, w):
        if v < w: # to be generalized
            return -1
        elif v > w:
            return 1
        else:
            return 0

if __name__ == '__main__':
    import random
    a = range(10)
    b = range(100, 110)
    random.shuffle(a)
    random.shuffle(b)
    print dict(zip(a, b))
    bst = BinarySearchTree()
    for i in xrange(10):
        bst.put(a[i], b[i])
    bst.show()
    bst.deleteMax()
    bst.show()
    print bst.floor(1)
    print bst.ceiling(1.5)
    print bst.rank(2.5)
    print bst.select(3)
    bst.delete(5)
    bst.show()
    print bst.keys()
    print bst.keys(7, 9)
