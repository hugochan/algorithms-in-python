#!/usr/bin/env python

class DepthFirstPath(object):
    """docstring for DepthFirstPath"""
    def __init__(self, G, s):
        super(DepthFirstPath, self).__init__()
        self.marked = [0 for i in xrange(G.Vcount())]
        self.edgeTo = [-1 for i in xrange(G.Vcount())] # prior node in the path
        self.count = 0
        self.s = s
        self.dfs(G, s)

    def dfs(self, G, v):
        self.marked[v] = 1
        self.count += 1
        for w in G.get_adj(v):
            if not self.marked[w]:
                self.edgeTo[w] = v
                self.dfs(G, w)

    def is_marked(self, v):
        return self.marked[v]

    def get_count(self):
        return self.count

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while not x == self.s:
            path.append(x)
            x = self.edgeTo[x]
        return path

if __name__ == '__main__':
    from graph import Graph
    g = Graph(5)
    g.read_file('mini_graph.txt')
    DFS = DepthFirstPath(g, 0)
    print DFS.marked
    print DFS.count
    print DFS.path_to(2)
