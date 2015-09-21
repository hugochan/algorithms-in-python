#!/usr/bin/env python

from symbol_graph import SymbolGraph
from bfp import BreadthFirstPath

def DegreesOfSeparation(file_in, sp, source):
    sg = SymbolGraph(file_in, sp)
    g = sg.G()
    if not sg.contains(source):
        print '%s not in database'%source
        exit()

    s = sg.index(source)
    bfp = BreadthFirstPath(g, s)

    dest = raw_input('Enter a target: ')
    if not sg.contains(dest):
        print 'Not in database'
        exit()
    t = sg.index(dest)
    if bfp.has_path_to(t):
        print '  %s'%source
        for v in bfp.path_to(t)[::-1]:
            print '  %s'%sg.name(v)
    else:
        print 'Not connected'

if __name__ == '__main__':
    DegreesOfSeparation('data/symbol_graph.txt', ' ', 'JFK')
