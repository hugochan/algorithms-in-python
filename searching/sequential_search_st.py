#!/usr/bin/env python

class Node(object):
    """docstring for Node"""
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next
        
class SequentialSearchST(object):
    """docstring for SequentialSearchST"""
    def __init__(self):
        self.first = None
        self.__N = 0

    def get(self, key):
        x = self.first
        while x is not None:
            if self.__compare(key, x.key) is 0:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        x = self.first
        while x is not None:
            if self.__compare(key, x.key) is 0:
                x.val = val
                return False # change
            x = x.next
        self.first = Node(key, val, self.first)
        self.__N += 1
        return True # add

    def delete(self, key):
        x = self.first
        tmp = None
        while x is not None:
            if self.__compare(key, x.key) is 0:
                if x is not self.first:
                    tmp.next = x.next
                    x.next = None
                else:
                    self.first = x.next
                    x.next = None
                self.__N -= 1
                return True # delete successfully
            tmp = x
            x = x.next
        return False # fail to delete

    def size(self):
        return self.__N

    def show(self):
        """print the ST"""
        x = self.first
        while x is not None:
            print x.key, x.val
            x = x.next

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
    st = SequentialSearchST()
    for i in xrange(10):
        st.put(keys[i], vals[i])
    st.show()
    for i in xrange(9, -1, -1):
        print keys[i], st.get(keys[i])
    st.delete(keys[9])
    print st.get(keys[9])
    print st.size()