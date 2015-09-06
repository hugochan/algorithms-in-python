#!/usr/bin/env python

class Edge(object):
    """docstring for Edge"""
    def __init__(self, v, w, weight):
        super(Edge, self).__init__()
        self.v = v
        self.w = w
        self.weight = weight

    def get_weight(self):
        return self.weight

    def either(self):
        return self.v

    def other(self, vertex):
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise ValueError("Inconsistent edge")

    def compare_to(self, that):
        if self.get_weight() < that.get_weight():
            return -1
        elif self.get_weight() > that.get_weight():
            return 1
        else:
            return 0

    def to_string(self):
        return "%s-%s %s"%(self.v, self.w, self.get_weight())

class EdgeWeightedGraph(object):
    """docstring for EdgeWeightedGraph"""
    def __init__(self, V):
        super(EdgeWeightedGraph, self).__init__()
        self.V = V
        self.E = 0
        self.adj = [[] for i in xrange(self.V)]

    def read_file(self, file_in):
        try:
            with open(file_in, 'r') as f:
                V = f.readline().rstrip('\n').split(' ')[0]
                V = int(V)
                for i in f:
                    tmp = i.rstrip('\n').split(' ')
                    v = int(tmp[0])
                    w = int(tmp[1])
                    weight = float(tmp[2])
                    e = Edge(v, w, weight)
                    self.add_edge(e)
        except Exception, e:
            print e
            assert False
        f.close()

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self.adj[v].append(e)
        self.adj[w].append(e)
        self.E += 1

    def Vcount(self):
        return self.V

    def Ecount(self):
        return self.E

    def get_adj(self, v):
        return self.adj[v]

    def edges(self):
        es = []
        for v in range(self.Vcount()):
            for e in self.get_adj(v):
                if e.other(v) > v:
                    es.append(e)
        return es

if __name__ == '__main__':
    ewg = EdgeWeightedGraph(8)
    ewg.read_file("tinyEWG.txt")
    print [x.weight for x in ewg.edges()]
