import sys


n=(int)(raw_input())
s=''
if(n/100!=0):
    a=n/100
    for i in range(a):
        s=s+('B')
    n=n%100
if(n/10!=0):
    b=n/10
    for i in range(b):
        s=s+'S'
    n=n%10
if(n!=0):
    for i in range(n):
        s=s+'%d'%(i+1)
print s

    
