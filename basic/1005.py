import sys

def check(x,s):
    while(x!=1):
        if(x%2==0):
            x=x/2
        else:
            x=(x*3+1)/2
        if(x in s):
            s.remove(x)
n=(int)(raw_input())
s=[]
x=sys.stdin.readline().strip('\n')
x1=x.split(' ')
for j in range(len(x1)):
    s.append(int(x1[j]))

t=s[:]
for i in range(len(t)):
    check(t[i],s)
g=sorted(s,reverse=True)
for x in g:
    print x,


    
