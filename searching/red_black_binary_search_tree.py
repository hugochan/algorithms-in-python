#!/usr/bin/env python

RED = True # const
BLACK = False

class Node(object):
    """docstring for Node"""
    def __init__(self, key, val, N, color):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.N = N
        self.color = color

class RedBlackBST(object):
    """docstring for RedBlackBST"""
    def __init__(self):
        self.__root = None

    def get(self, key):
        return self.__get(self.__root, key)

    def __get(self, x, key):
        if x is None:
            return None
        _cmp = self.__compare(key, x.key)
        if _cmp < 0:
            return self.__get(x.left, key)
        elif _cmp > 0:
            return self.__get(x.right, key)
        else:
            return x.val

    def put(self, key, val):
        self.__root = self.__put(self.__root, key, val)
        self.__root.color = BLACK

    def __put(self, h, key, val):
        if h is None:
            return Node(key, val, 1, RED)
        _cmp = self.__compare(key, h.key)
        if _cmp < 0:
            h.left = self.__put(h.left, key, val)
        elif _cmp > 0:
            h.right = self.__put(h.right, key, val)
        else:
            h.val = val

        if self.__isRed(h.right) and not self.__isRed(h.left):
            h = self.__rotateLeft(h)
        if self.__isRed(h.left) and self.__isRed(h.left.left):
            h = self.__rotateRight(h)
        if self.__isRed(h.left)  and self.__isRed(h.right):
            self.__flipColors(h)

        h.N = self.__size(h.left) + self.__size(h.right) + 1
        return h

    def deleteMin(self):
        if not self.__isRed(self.__root.left) and not self.__isRed(self.__root.right):
            self.__root.color = RED
        self.__root = self.__deleteMin(self.__root)
        if not self.isEmpty():
            self.__root.color = BLACK

    def __deleteMin(self, h):
        if h.left is None:
            return None
        if not self.__isRed(h.left) and not self.__isRed(h.left.left):
            h = self.__moveRedLeft(h)
        h.left = self.__deleteMin(h.left)
        return self.__balance(h)

    def deleteMax(self):
        if not self.__isRed(self.__root.left) and not self.__isRed(self.__root.right):
            self.__root.color = RED
        self.__root = self.__deleteMax(self.__root)
        if not self.isEmpty():
            self.__root.color = BLACK

    def __deleteMax(self, h):
        if self.__isRed(h.left):
            h = self.__rotateRight(h)
        if h.right is None:
            return None
        if not self.__isRed(h.right) and not self.__isRed(h.right.left):
            h = self.__moveRedRight(h)
        h.right = self.__deleteMax(h.right)
        return self.__balance(h)

    def delete(self, key):
        if not self.contains(key):
            print str(key) + " does not exist"
            return None
        if not self.__isRed(self.__root.left) and not self.__isRed(self.__root.right):
            self.__root.color = RED
        self.__root = self.__delete(self.__root, key)
        if not self.isEmpty():
            self.__root.color = BLACK

    def __delete(self, h, key):
        if self.__compare(key, h.key) < 0:
            if not self.__isRed(h.left) and not self.__isRed(h.left.left):
                h = self.__moveRedLeft(h)
            h.left = self.__delete(h.left, key)
        else:
            if self.__isRed(h.left):
                h = self.__rotateRight(h)
            if self.__compare(key, h.key) is 0 and h.right is None:
                return None
            if not self.__isRed(h.right) and not self.__isRed(h.right.left):
                h = self.__moveRedRight(h)
            if self.__compare(key, h.key) is 0:
                x = self.__min(h.right)
                h.key = x.key
                h.val = x.val
                h.right = self.__deleteMin(h.right)
            else:
                h.right = self.__delete(h.right, key)
        return self.__balance(h)

    def __isRed(self, x):
        if x is None:
            return False
        return x.color is RED

    def __rotateLeft(self, h):
        assert h is not None and self.__isRed(h.right)
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self.__size(h.left) + self.__size(h.right)
        return x

    def __rotateRight(self, h):
        assert h is not None and self.__isRed(h.left)
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        x.N = h.N
        h.N = 1 + self.__size(h.left) + self.__size(h.right)
        return x

    def __flipColors(self, h):
        """flip colors of a node and its two children"""
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color
    
    def __moveRedLeft(self, h):#???
        """Assume that the node h is RED, h.left and h.left.left are both BLACK,
        then we change either h.left or one of its children to be RED."""
        self.__flipColors(h)
        if self.__isRed(h.right.left):
            h.right = self.__rotateRight(h.right)
            h = self.__rotateLeft(h)
            self.__flipColors(h)#???
        return h

    def __moveRedRight(self, h):#???
        """Assume that the node h is RED, h.right and h.right.left are both BLACK,
        then we change either h.right or one of its children to be RED.
        """
        self.__flipColors(h)
        if self.__isRed(h.left.left):
            h = self.__rotateRight(h)
            self.__flipColors(h)#???
        return h

    def __balance(self, h): #???
        if self.__isRed(h.right):
            h = self.__rotateLeft(h)
        if self.__isRed(h.left) and self.__isRed(h.left.left):
            h = self.__rotateRight(h)
        if self.__isRed(h.left)  and self.__isRed(h.right):
            self.__flipColors(h)

        h.N = self.__size(h.left) + self.__size(h.right) + 1
        return h

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
        if cmplo <= 0 <= cmphi:
            queue.append(x.key)
        if cmphi > 0:
            self.__keys(x.right, queue, lo, hi)

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

    def contains(self, key):
        return self.get(key) is not None

    def isEmpty(self):
        return self.size() is 0

    def size(self):
        return self.__size(self.__root)

    def __size(self, x):
        if x is None:
            return 0
        else:
            return x.N

    def height(self):
        """height of tree (1-node tree has height 0)"""
        return self.__height(self.__root)

    def __height(self, x):
        if x is None: 
            return -1;
        return 1 + max(self.__height(x.left), self.__height(x.right))

    def isBST(self):
        """does this binary tree satisfy symmetric order?
        Note: this test also ensures that data structure is a binary tree since order is strict
        """
        return self.__isBST(self.__root, None, None);

    def __isBST(self, x, _min, _max):
        """is the tree rooted at x a BST with all keys strictly between _min and _max
        (if _min or _max is None, treat as empty constraint)
        Credit: Bob Dondero's elegant solution
        """
        if x is None:
            return True
        if _min is not None and self.__compare(x.key, _min) <= 0:
            return False
        if _max is not None and self.__compare(x.key, _max) >= 0:
            return False
        return self.__isBST(x.left, _min, x.key) and self.__isBST(x.right, x.key, _max)

    def is23Tree(self):
        """Does the tree have no red right links, and at most one (left)
        red links in a row on any path?
        """
        return self.__is23Tree(self.__root)

    def __is23Tree(self, x):
        if x is None:
            return True
        if self.__isRed(x.right):
            return False
        if x is not self.__root and self.__isRed(x) and self.__isRed(x.left):
            return False
        return self.__is23Tree(x.left) and self.__is23Tree(x.right)

    def isBalanced(self):
        """Do all paths from root to leaf have same number of black edges?
        """
        black = 0
        x = self.__root
        while x is not None:
            if not self.__isRed(x):
                black += 1
            x = x.left
        return self.__isBalanced(self.__root, black)

    def __isBalanced(self, x, black):
        """Does every path from the root to a leaf have the given number of black links?
        """
        if x is None:
            return black is 0
        if not self.__isRed(x):
            black -= 1
        return self.__isBalanced(x.left, black) and self.__isBalanced(x.right, black)

    def show(self):
        """print the rbt"""
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
    a = range(500)
    b = range(100, 600)
    random.shuffle(a)
    random.shuffle(b)
    # print dict(zip(a, b))
    rbt = RedBlackBST()
    for i in xrange(500):
        rbt.put(a[i], b[i])
    # rbt.show()
    # print rbt.height()
    # rbt.deleteMin()
    # rbt.show()
    rbt.deleteMax()
    rbt.show()
    for i in xrange(400, 500):
        rbt.delete(i)
    rbt.show()
    # print rbt.min()
    # print rbt.max()
    # print rbt.rank(45)
    # print rbt.select(5)
    # print rbt.keys()
    # print rbt.keys(42, 44)
    # print rbt.ceiling(43)
    # print rbt.floor(43.5)
    print rbt.isBST()
    print rbt.is23Tree()
    print rbt.isBalanced()