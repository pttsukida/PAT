import sys
l,s=map(int,raw_input().split())
a=map(int,raw_input().split())
dic={}
for x in a:
    if dic.has_key(x):
        dic[x]+=1
    else:
        dic[x]=1
flag=False
p=0
q=0
for x in a:
    y=s-x
    if dic.has_key(y):
        if x!=y or dic[y]>=2:
            flag=True
            if abs(x-y)>abs(p-q):
                p=x
                q=y
if flag:
    if p<=s/2:
        print p,s-p
    else:
        print s-q,q
else:
    print 'No Solution'
    
    
