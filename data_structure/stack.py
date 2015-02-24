#!/usr/bin/env python

class Stack(object):
    """docstring for Resizing Stack"""
    def __init__(self):
        self.__stack = []

    def isEmpty(self):
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        item = self.__stack[-1]
        del self.__stack[-1]
        return item

    def show(self):
        for i in range(self.size()):
            print self.__stack[i]

if __name__ == '__main__':
    import random
    stack = Stack()
    a = range(10)
    random.shuffle(a)
    print a
    for i in a:
        stack.push(i)
    for i in range(10):
        print stack.pop()
    print stack.isEmpty()
    stack.show()