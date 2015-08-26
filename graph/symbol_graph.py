#!/usr/bin/env python

from graph import Graph

class SymbolGraph(object):
    """docstring for SymbolGraph"""
    def __init__(self, file_in, sp):
        super(SymbolGraph, self).__init__()
        self.st = dict()

        try:
            with open(file_in, 'r') as f:
                for eachline in f:
                    tmp = eachline.rstrip('\n').split(sp)
                    for each in tmp:
                        if not self.st.has_key(each):
                            self.st[each] = len(self.st)

                self.keys = dict(zip(self.st.values(), self.st.keys()))
                # self.keys = ['' for i in xrange(len(self.st))]
                # for k, v in self.st.items():
                #     self.keys[v] = k

                self.g = Graph(len(self.st))
                f.seek(0)
                for eachline in f:
                    tmp = eachline.rstrip('\n').split(sp)
                    for i in tmp[1:]:
                        self.g.add_edge(self.st[tmp[0]], self.st[i])

        except Exception, e:
            print e
            assert False
        f.close()

    def contains(self, s):
        return self.st.has_key(s)

    def index(self, s):
        return self.st.get(s)

    def name(self, index):
        return self.keys[index]

    def G(self):
        return self.g

if __name__ == '__main__':
    sg = SymbolGraph('symbol_graph.txt', ' ')
    print sg.contains('JFK')
    print sg.index('JFK')
    print sg.st
    print sg.keys
    g = sg.G()
    source = raw_input('Enter the source: ')
    for each in g.get_adj(sg.st[source]):
        print '  %s'%sg.keys[each]
