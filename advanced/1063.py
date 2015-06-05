import sys
n=int(sys.stdin.readline().strip('\n'))
s=[]
for i in range(n):
    x=(sys.stdin.readline().strip('\n').split(' '))
    d=set(x[1:])
    s.append(d)
n2=int(sys.stdin.readline().strip('\n'))
for i in range(n2):
    x=(sys.stdin.readline().strip('\n').split(' '))
    a=int(x[0])-1
    b=int(x[1])-1
    l1=len(s[a])
    l2=len(s[b])
    l=len(s[a]&s[b])
    l3=l1+l2-l
    ans=float(l)/(l3)
    print '%.1f%%'%(ans*100)
    
