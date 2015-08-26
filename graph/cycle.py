#!/usr/bin/env python

class Cycle(object):
    """test cycles in a graph: ignore self-loops & parallel edges"""
    def __init__(self, G):
        super(Cycle, self).__init__()
        self.marked = [0 for i in xrange(G.Vcount())]
        self.hasCycle = 0
        for s in range(G.Vcount()):
            if not self.marked[s]:
                self.dfs(G, s, s)

    def dfs(self, G, v, u):
        self.marked[v] = 1
        for w in G.get_adj(v):
            if not self.marked[w]:
                self.dfs(G, w, v)
            elif not w == u:
                self.hasCycle = 1

    def has_cycle(self):
        return self.hasCycle

if __name__ == '__main__':
    from graph import Graph
    g = Graph(5)
    g.read_file('mini_graph.txt')
    cycle = Cycle(g)
    print cycle.has_cycle()
