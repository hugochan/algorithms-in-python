#!/usr/bin/env python

class CC(object):
    """docstring for CC"""
    def __init__(self, G):
        super(CC, self).__init__()
        self.marked = [0 for i in xrange(G.Vcount())]
        self.id = [-1 for i in xrange(G.Vcount())]
        self.count = 0
        for s in range(G.Vcount()):
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

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def get_id(self, v):
        return self.id[v]

if __name__ == '__main__':
    from graph import Graph
    g = Graph(5)
    g.read_file('mini_graph.txt')
    cc = CC(g)
    print cc.get_count()
    print cc.connected(2, 3)
