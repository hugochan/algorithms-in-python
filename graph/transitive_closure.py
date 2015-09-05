#!/usr/bin/env python

from directed_dfs import DirectedDFS

class TransitiveClosure(object):
    """a straightforward algorithm to address reachability problem in directed graph"""
    def __init__(self, G):
        super(TransitiveClosure, self).__init__()
        self.reachability = [0 for i in range(G.Vcount())]
        for v in range(G.Vcount()):
            self.reachability[v] = DirectedDFS(G, v)

    def reachable(self, v, w):
        return self.reachability[v].ismarked(w)

if __name__ == '__main__':
    from digraph import Digraph
    g = Digraph(5)
    g.read_file('mini_graph.txt')
    tc = TransitiveClosure(g)
    print tc.reachable(0, 3)
