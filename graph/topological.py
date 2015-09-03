#!/usr/bin/env python

from directed_cycle import DirectedCycle
from depth_first_order import DepthFirstOrder

class Topological(object):
    """docstring for Topological"""
    def __init__(self, G):
        super(Topological, self).__init__()
        cyclefinder = DirectedCycle(G)
        if not cyclefinder.has_cycle():
            dfo = DepthFirstOrder(G)
            self.order = dfo.get_reversePost()
        else:
            self.order = []

    def get_order(self):
        return self.order

    def is_DAG(self):
        return not self.order == []

if __name__ == '__main__':
    from digraph import Digraph
    g = Digraph(5)
    g.read_file('tiny_digraph.txt')
    topo = Topological(g)
    print topo.is_DAG()
    order = topo.get_order()
    while not order == []:
        print order.pop()

