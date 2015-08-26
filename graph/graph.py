#!/usr/bin/env python

class Graph(object):
    """docstring for Graph"""
    def __init__(self, V):
        super(Graph, self).__init__()
        self.V = V
        self.E = 0
        self.adj = [[] for i in xrange(self.V)]

    def read_file(self, file_in):
        try:
            with open(file_in, 'r') as f:
                V = int(f.readline().rstrip('\n'))
                E = int(f.readline().rstrip('\n'))
                for i in f:
                    tmp = i.rstrip('\n').split(' ')
                    v = int(tmp[0])
                    w = int(tmp[1])
                    self.add_edge(v, w)
        except Exception, e:
            print e
            assert False
        f.close()

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def Vcount(self):
        return self.V

    def Ecount(self):
        return self.E

    def get_adj(self, v):
        return self.adj[v]

    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        __max_degree = 0
        for i in range(self.V):
            degree = self.degree(i)
            __max_degree = degree if __max_degree < degree else __max_degree
        return __max_degree

    def avg_degree(self):
        return 2.0*self.E/self.V

    def number_of_selfloops(self):
        count = 0
        for v in range(self.V):
            if v in self.adj[v]:
                count += 1
        return count/2.0

    def to_string(self):
        s = str(self.V) + ' vertices, ' + str(self.E) + ' edges\n'
        for v in range(self.V):
            s += str(v) + ': '
            for w in self.adj[v]:
                s += str(w) + ' '
            s += '\n'
        return s

if __name__ == '__main__':
    g = Graph(13)
    g.read_file('tiny_graph.txt')
    print g.adj
    print g.max_degree()
    print g.avg_degree()
    print g.number_of_selfloops()
    print g.to_string()

