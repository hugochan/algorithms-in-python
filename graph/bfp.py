#!/usr/bin/env python

import Queue

class BreadthFirstPath(object):
    """docstring for BreadthFirstPath"""
    def __init__(self, G, s):
        super(BreadthFirstPath, self).__init__()
        self.marked = [0 for i in xrange(G.Vcount())]
        self.edgeTo = [-1 for i in xrange(G.Vcount())] # prior node in the path
        self.s = s
        self.bfs(G, s)

    def bfs(self, G, s):
        queue = Queue.Queue()
        self.marked[s] = 1
        queue.put(s)
        while not queue.empty():
            v = queue.get()
            for w in G.get_adj(v):
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.marked[w] = 1
                    queue.put(w)

    def is_marked(self, v):
        return self.marked[v]

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
    g = Graph(6)
    g.read_file('micro_graph.txt')
    BFS = BreadthFirstPath(g, 0)
    print BFS.marked
    print BFS.path_to(4)
