import sys
class person():
    def __init__(self,t,p):
        self.t=t
        self.p=p
    
class window(object):
    def __init__(self,rank):
        self.customers=[]
        self.rank=rank
        self.num=0
        self.waittime=0
    def __cmp__(self,other):
        assert other
        if not isinstance(other,window):
            raise TypeError
        if self.num!=other.num:
            return cmp(self.num,other.num)
        else:
            return cmp(self.rank,other.rank)
