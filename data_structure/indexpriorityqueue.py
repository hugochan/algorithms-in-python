#!/usr/bin/env python

class IndexMaxPQ(object):
    """docstring for resizing IndexMaxPQ"""
    def __init__(self):
        self.__pq = [0] # store indices
        # self.__qp = {} # store {index:sequence num}
        self.__keys = {} # store elements

    def isEmpty(self):
        return len(self.__pq) - 1 == 0

    def size(self):
        return len(self.__pq) - 1

    def constains(self, k):
        return k in self.__pq[1:]

    def insert(self, k, key):
        self.__pq.append(k)
        self.__keys[k] = key
        self.__swim(self.size())

    def change(self, k, key):
        self.__keys[k] = key
        try:
            t = self.__pq[1:].index(k) + 1
        except ValueError:
            print "Change error"
        else:
            self.__swim(t)
            self.__sink(t)

    def delete(self, k):
        try:
            t = self.__pq[1:].index(k) + 1
        except ValueError:
            print "Change error"
        else:
            self.__exch(t, self.size())
            del self.__pq[-1]
            del self.__keys[k]
            self.__swim(t)
            self.__sink(t)

    def maxIndex(self):
        return self.__pq[1]

    def max(self):
        return self.__keys[self.__pq[1]]

    def delMax(self):
        indexOfMax = self.__pq[1]
        self.__exch(1, self.size())
        del self.__pq[-1]
        del self.__keys[indexOfMax]
        self.__sink(1)
        return indexOfMax

    def show(self):
        for i in range(1, self.size()+1):
            print str(self.__pq[i]) + ":" + str(self.__keys[self.__pq[i]])

    def __swim(self, k):
        while k > 1 and self.__less(k/2, k):
            self.__exch(k/2, k)
            k = k/2

    def __sink(self, k):
        N = self.size()
        while 2*k <= N:
            j = 2*k
            if j < N and self.__less(j, j+1):
                j += 1
            if not self.__less(k, j):
                break
            self.__exch(k, j)
            k = j

    def __less(self, i, j):
        return self.__keys[self.__pq[i]] < self.__keys[self.__pq[j]] # to be generalized

    def __exch(self, i, j):
        t = self.__pq[i] # to be generalized
        self.__pq[i] = self.__pq[j]
        self.__pq[j] = t

if __name__ == '__main__':
    import random
    k = range(10)
    keys = range(100, 110)
    random.shuffle(k)
    random.shuffle(keys)
    _dict = dict(zip(k, keys))
    print _dict
    impq = IndexMaxPQ()
    for each_k, each_key in _dict.items():
        impq.insert(each_k, each_key)
    impq.show()
    
    impq.change(4, 99)
    impq.show()

    for i in range(5):
        print impq.delMax()
    
    impq.show()
    print impq.constains(9)
    impq.delete(0)
    impq.show()
    print impq.max()
    print impq.maxIndex()