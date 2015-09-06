#!/usr/bin/env python

from collections import deque

class LazyPrimMST(object):
    """LazyPrimMST: a lazy version of prim minimal spanning tree algorithm"""
    def __init__(self, G):
        super(LazyPrimMST, self).__init__()
        self.G = G
        self.marked = [0 for i in xrange(G.Vcount())] # nodes of mst
        self.mst = deque() # edges of mst
        self.pq = MinPQ() # cross-cutting edge

        self.visit(0)
        while(self.pq.size() > 0):
            if len(self.mst) >= self.G.Vcount() - 1:
                break
            e = self.pq.delMin() # minimal weighted edge
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]: # ignore the invalid edge
                continue
            self.mst.append(e)
            if not self.marked[v]:
                self.visit(v)
            if not self.marked[w]:
                self.visit(w)

    def visit(self, v):
        self.marked[v] = 1
        for e in self.G.get_adj(v):
            if not self.marked[e.other(v)]:
                self.pq.insert(e)

    def edges(self):
        return self.mst

    def total_weight(self):
        total_w = 0.0
        for e in self.edges():
            total_w += e.weight
        return total_w


class MinPQ(object):
    """minimal priority queue"""
    def __init__(self):
        self.__pq = deque([0])

    def isEmpty(self):
        return len(self.__pq) - 1 == 0

    def size(self):
        return len(self.__pq) - 1

    def insert(self, v):
        self.__pq.append(v)
        self.__swim(self.size())

    def delMin(self):
        _min = self.__pq[1]
        self.__exch(1, self.size())
        del self.__pq[-1]
        self.__sink(1)
        return _min

    def show(self):
        for i in xrange(1, self.size()+1):
            print self.__pq[i]

    def __swim(self, k):
        while k > 1 and self.__more(k/2, k):
            self.__exch(k/2, k)
            k = k/2

    def __sink(self, k):
        N = self.size()
        while 2*k <= N:
            j = 2*k
            if j < N and self.__more(j, j+1):
                j += 1
            if not self.__more(k, j):
                break
            self.__exch(k, j)
            k = j

    def __more(self, i, j):
        return self.__pq[i].get_weight() > self.__pq[j].get_weight()

    def __exch(self, i, j):
        self.__pq[i], self.__pq[j] = self.__pq[j], self.__pq[i]

if __name__ == '__main__':
    from edge_weighted_graph import EdgeWeightedGraph
    ewg = EdgeWeightedGraph(8)
    ewg.read_file("tinyEWG.txt")
    mst = LazyPrimMST(ewg)
    for each in mst.edges():
        print each.v, each.w, each.weight
    print mst.total_weight()
