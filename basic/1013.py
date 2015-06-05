import sys
m,n=map(int,raw_input().split())
s=[1]*10001
i=2;
while(i<=5000):
    if(s[i]==1):
        k=i+i
        while(k<=10000):
            s[k]=0
            k+=i
    i+=1
q=[]
for i in range(10001):
    if(s[i]==1):
        q.append(i)
c=0
for i in range(m,n+1):
    sys.stdout.write('%d'%q[i+1])
    c+=1
    if(i!=n):
        if(c==10):
            sys.stdout.write('\n')
            c=0
        else:
            sys.stdout.write(' ')
        
