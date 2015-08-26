#!/usr/bin/env python

class DepthFirstSearch(object):
    """docstring for DepthFirstSearch"""
    def __init__(self, G, s):
        super(DepthFirstSearch, self).__init__()
        self.marked = [0 for i in xrange(G.Vcount())]
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = 1
        self.count += 1
        for w in G.get_adj(v):
            if not self.marked[w]:
                self.dfs(G, w)

    def ismarked(self, v):
        return self.marked[v]

    def get_count(self):
        return self.count

if __name__ == '__main__':
    from graph import Graph
    g = Graph(5)
    g.read_file('mini_graph.txt')
    DFS = DepthFirstSearch(g, 0)
    print DFS.marked
    print DFS.count
