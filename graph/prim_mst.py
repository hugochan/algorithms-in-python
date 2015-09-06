#!/usr/bin/env python

class PrimMST(object):
    """PrimMST: prim minimal spanning tree algorithm"""
    def __init__(self, G):
        super(PrimMST, self).__init__()
        self.G = G
        self.edgeTo = [None for i in xrange(self.G.Vcount())] # closest edge to the mst for each node out of the tree
        self.distTo = [float('inf') for i in xrange(self.G.Vcount())] # the weights of above edge
        self.marked = [0 for i in xrange(self.G.Vcount())]
        self.pq = IndexMinPQ()

        # init
        self.distTo[0] = 0.0
        self.pq.insert(0, 0.0)

        while self.pq.size() > 0:
            self.visit(self.pq.delMin())

    def visit(self, v):
        self.marked[v] = 1
        for e in self.G.get_adj(v):
            w = e.other(v)
            if self.marked[w]:
                continue
            if e.get_weight() < self.distTo[w]:
                self.edgeTo[w] = e
                self.distTo[w] = e.get_weight()
                if self.pq.constains(w):
                    self.pq.change(w, self.distTo[w])
                else:
                    self.pq.insert(w, self.distTo[w])

    def edges(self):
        mst = []
        for v in range(1, self.G.Vcount()):
            mst.append(self.edgeTo[v])
        return mst

    def total_weight(self):
        totalWeight = 0.0
        for v in range(1, self.G.Vcount()):
            totalWeight += self.distTo[v]
        return totalWeight

class IndexMinPQ(object):
    """docstring for resizing IndexMinPQ:
    does not support repeated indices (k)
    """
    def __init__(self):
        self.__pq = [0] # store indices (k)
        self.__qp = {None:0} # store {index:sequence num}
        self.__keys = {} # store {index:element}

    def isEmpty(self):
        return len(self.__pq) - 1 == 0

    def size(self):
        return len(self.__pq) - 1

    def constains(self, k):
        return k in self.__qp

    def insert(self, k, key):
        self.__pq.append(k)
        N = self.size()
        self.__qp[k] = N
        self.__keys[k] = key
        self.__swim(N)

    def change(self, k, key):
        self.__keys[k] = key
        t = self.__qp.get(k)
        if t is None:
            print "Change Error"
        else:
            self.__swim(t)
            self.__sink(t)

    def delete(self, k):
        t = self.__qp.get(k)
        if t is None:
            print "Change Error"
        else:
            self.__exch(t, self.size())
            del self.__pq[-1]
            del self.__qp[k]
            del self.__keys[k]
            self.__swim(t)
            self.__sink(t)

    def minIndex(self):
        return self.__pq[1]

    def min(self):
        return self.__keys[self.__pq[1]]

    def delMin(self):
        indexOfMin = self.__pq[1]
        self.__exch(1, self.size())
        del self.__pq[-1]
        del self.__qp[indexOfMin]
        del self.__keys[indexOfMin]
        self.__sink(1)
        return indexOfMin

    def show(self):
        for i in range(1, self.size()+1):
            print str(self.__pq[i]) + ":" + str(self.__keys[self.__pq[i]])

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
        return self.__keys[self.__pq[i]] > self.__keys[self.__pq[j]] # to be generalized

    def __exch(self, i, j):
        self.__pq[i], self.__pq[j] = self.__pq[j], self.__pq[i]
        self.__qp[self.__pq[i]], self.__qp[self.__pq[j]] = i, j

if __name__ == '__main__':
    from edge_weighted_graph import EdgeWeightedGraph
    ewg = EdgeWeightedGraph(8)
    ewg.read_file("tinyEWG.txt")
    mst = PrimMST(ewg)
    for each in mst.edges():
        print each.v, each.w, each.weight
    print mst.total_weight()
