#!/usr/bin/env python

import Queue

class DepthFirstOrder(object):
    """docstring for DepthFirstOrder"""
    def __init__(self, G):
        super(DepthFirstOrder, self).__init__()
        self.pre = Queue.Queue() # queue
        self.post = Queue.Queue() # queue
        self.reversePost = [] # stack
        self.marked = [0 for i in xrange(G.Vcount())]
        for v in range(G.Vcount()):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.pre.put(v) # enqueue
        self.marked[v] = 1
        for w in G.get_adj(v):
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.put(v) # enqueue
        self.reversePost.append(v) # push

    def get_pre(self):
        return self.pre

    def get_post(self):
            return self.post

    def get_reversePost(self):
            return self.reversePost

if __name__ == '__main__':
    from digraph import Digraph
    g = Digraph(5)
    g.read_file('data/tiny_digraph.txt')
    DFO = DepthFirstOrder(g)
    pre = DFO.get_pre()
    post = DFO.get_post()
    reversePost = DFO.get_reversePost()
    print 'pre:'
    while not pre.empty():
        print pre.get()
    print 'post:'
    while not post.empty():
        print post.get()
    print 'reverse post:'
    while not reversePost == []:
        print reversePost.pop()
