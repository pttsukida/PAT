import sys

n=(int)(raw_input())
x=sys.stdin.readline().strip('\n').split()
x=map(int,x)

def maxlist(x):
    if(len(x)==0):
        return 0
    a1=maxlist(x[0:len(x)-1])
    a2=maxrightlist(x[0:len(x)-1])
    if x[-1]>0:
        a2=a2+x[-1]
    return max(a1,a2)

def maxrightlist(x):
    if(len(x)==0):
        return 0
    else:
        q=x[-1]
        a1=maxrightlist(x[0:len(x)-1])
        if a1<0:
            return q
        else:
            return q+a1

def maxlistIter(a):
    m1=0
    m2=0
    for x in a:
        if m2>=0:
            m2=x+m2
        else:
            m2=x
        m1=max(m1,m2)
    return m1

print maxlistIter(x)