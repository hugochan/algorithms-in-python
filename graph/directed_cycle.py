#!/usr/bin/env python

class DirectedCycle(object):
    """docstring for DirectedCycle"""
    def __init__(self, G):
        super(DirectedCycle, self).__init__()
        self.onStack = [0 for i in xrange(G.Vcount())]
        self.edgeTo = [-1 for i in xrange(G.Vcount())]
        self.marked = [0 for i in xrange(G.Vcount())]
        self.cycle = []
        for v in range(G.Vcount()):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.onStack[v] = 1
        self.marked[v] = 1
        for w in G.get_adj(v):
            if self.has_cycle():
                return None
            elif not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)
            elif self.onStack[w]:
                x = v
                while not x == w:
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
                self.cycle.append(v)
        self.onStack[v] = 0

    def has_cycle(self):
        return not self.cycle == []

    def get_cycle(self):
        return self.cycle

if __name__ == '__main__':
    from digraph import Digraph
    g = Digraph(5)
    g.read_file('data/tiny_digraph.txt')
    dc = DirectedCycle(g)
    print dc.has_cycle()
    print dc.cycle
