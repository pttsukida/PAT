import sys

n=(int)(raw_input())
for i in range(n):
    a, b, c = map(int, raw_input().split())
    if a+b>c:
        s='true'
    else:
        s='false'
    print 'Case #%d: %s'%(i+1,s)
    
