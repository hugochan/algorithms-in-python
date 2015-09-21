#!/usr/bin/env python

class UF(object):
    """docstring for UF"""
    def __init__(self, N):
        super(UF, self).__init__()
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

if __name__ == '__main__':
    try:
        with open('data/tinyUF.txt', 'r') as f:
            N = f.readline()
            uf = UF(int(N))
            for eachline in f:
                tmp = eachline.split(' ')
                p = int(tmp[0])
                q = int(tmp[1])
                if uf.connected(p, q):
                    continue
                uf.union(p, q)
                print '%s %s'%(p, q)
    except Exception, e:
        print e
        assert False
    f.close()
    print '%s components'%uf.get_count()

