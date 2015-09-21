#!/usr/bin/env python

class TwoColor(object):
    """Two-Color problem"""
    def __init__(self, G):
        super(TwoColor, self).__init__()
        self.marked = [0 for i in xrange(G.Vcount())]
        self.color = [0 for i in xrange(G.Vcount())]
        self.isTwoColorable = 1
        for s in range(G.Vcount()):
            if not self.marked[s]:
                self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = 1
        for w in G.get_adj(v):
            if not self.marked[w]:
                self.color[w] = not self.color[v]
                self.dfs(G, w)
            elif self.color[w] == self.color[v]:
                self.isTwoColorable = 0

    def isBipartite(self):
        return self.isTwoColorable

if __name__ == '__main__':
    from graph import Graph
    g = Graph(5)
    g.read_file('data/mini_graph.txt')
    tc = TwoColor(g)
    print tc.isBipartite()
