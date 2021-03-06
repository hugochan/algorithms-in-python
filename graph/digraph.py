#!/usr/bin/env python

class Digraph(object):
    """docstring for Digraph"""
    def __init__(self, V):
        super(Digraph, self).__init__()
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
        self.E += 1

    def Vcount(self):
        return self.V

    def Ecount(self):
        return self.E

    def get_adj(self, v):
        return self.adj[v]

    def reverse(self):
        r = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]:
                r.add_edge(w, v)
        return r

    def to_string(self):
        s = str(self.V) + ' vertices, ' + str(self.E) + ' edges\n'
        for v in range(self.V):
            s += str(v) + ': '
            for w in self.adj[v]:
                s += str(w) + ' '
            s += '\n'
        return s

if __name__ == '__main__':
    g = Digraph(13)
    g.read_file('data/tiny_graph.txt')
    print g.adj
    print g.to_string()
    print g.reverse().to_string()
