import sys

tmp=sys.stdin.readline().strip('\n').split(' ')
a=int(tmp[0])+1
b=int(tmp[1])+1
if(a<b):
    t=a
    a=b
    b=t
now=1
count=0
v=0
s=['A','D','T']
q=[]
x2=sys.stdin.readline().strip('\n').split(' ')

i=0
while(i<len(x2)):
    if(now==1):
        v=min(a,b+1)
    else:
        v=min(a+1,b)
    x=x2[i]
    if x in s:
        if x=='A':
            if count<v:
                q.insert(0,x2[i+1])
                
                count=count+1
            else:
                print 'ERROR:Full'
            i=i+2

        if x=='D':
            if len(q)>0:
                print q.pop()
                now=1-now
                
                count=count-1
            else:
                print 'ERROR:Empty'
            i=i+1
        if x=='T':
            break
    
            
            

