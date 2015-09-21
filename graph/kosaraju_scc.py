#!/usr/bin/env python

from depth_first_order import DepthFirstOrder

class KosarajuSCC(object):
    """a linear time algorithm to find the strongly connected components of a directed graph."""
    def __init__(self, G):
        super(KosarajuSCC, self).__init__()
        self.marked = [0 for i in xrange(G.Vcount())]
        self.id = [-1 for i in xrange(G.Vcount())]
        self.count = 0
        order = DepthFirstOrder(G.reverse())
        for s in order.get_reversePost()[::-1]: # pop the reverse post stack
            if not self.marked[s]:
                self.dfs(G, s)
                self.count += 1

    def dfs(self, G, v):
        self.marked[v] = 1
        self.id[v] = self.count
        for w in G.get_adj(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def get_count(self):
        return self.count

    def strongly_connected(self, v, w):
        return self.id[v] == self.id[w]

    def get_id(self, v):
        return self.id[v]

if __name__ == '__main__':
    from digraph import Digraph
    g = Digraph(5)
    g.read_file('data/mini_graph.txt')
    scc = KosarajuSCC(g)
    print scc.get_count()
    print scc.strongly_connected(2, 1)
