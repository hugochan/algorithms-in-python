#!/usr/bin/env python

from collections import deque

class KruskalMST(object):
    """docstring for KruskalMST"""
    def __init__(self, G):
        super(KruskalMST, self).__init__()
        self.G = G
        self.mst = deque()
        self.pq = MinPQ()
        for e in G.edges():
            self.pq.insert(e)
        self.uf = UF(G.Vcount())

        while not self.pq.isEmpty() and len(self.mst) < G.Vcount() - 1:
            e = self.pq.delMin() # get the minimal weighted edge
            v = e.either()
            w = e.other(v)
            if self.uf.connected(v, w): # ignore invalid edge
                continue
            self.uf.union(v, w) # merge components
            self.mst.append(e) # add to the mst

    def edges(self):
        return self.mst

    def total_weight(self):
        totalWeight = 0.0
        for e in self.edges():
            totalWeight += e.weight
        return totalWeight

class UF(object):
    """docstring for UF"""
    def __init__(self, N):
        super(UF, self).__init__()
        self.N = N
        self.id = range(N)
        self.count = N

    def get_count(self):
        return self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        pID = self.find(p)
        qID = self.find(q)
        if pID == qID:
            return
        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID
        self.count -= 1

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
    ewg.read_file("data/tinyEWG.txt")
    mst = KruskalMST(ewg)
    for each in mst.edges():
        print '%s-%s %s'%(each.v, each.w, each.weight)
    print mst.total_weight()
