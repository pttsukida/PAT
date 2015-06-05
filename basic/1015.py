import sys
a=sys.stdin.readlines()
n,l,h=map(int,a[0].split())
A=[]
B=[]
C=[]
D=[]
count=n
for i in range(n):
    #a=sys.stdin.readline().strip('\n')
    x=map(int,a[i+1].split())
    x.append(x[1]+x[2])
    if x[1]<l or x[2]<l:
        count-=1
        continue
    if x[1]>=h and x[2]>=h:
        A.append(x)
    elif x[1]>=h and x[2]<h:
        B.append(x)
    elif x[1]<h and x[2]<h and x[1]>=x[2]:
        C.append(x)
    else:
        D.append(x)
def mycmp(x1,x2):
    if x1[3]!=x2[3]:
        return -cmp(x1[3],x2[3])
    else:
        if x1[1]!=x2[1]:
            return -cmp(x1[1],x2[1])
        else:
            return cmp(x1[0],x2[0])
A.sort(mycmp)
B.sort(mycmp)
C.sort(mycmp)
D.sort(mycmp)
print count
for x in A:
    print x[0],x[1],x[2]
for x in B:
    print x[0],x[1],x[2]
for x in C:
    print x[0],x[1],x[2]
for x in D:
    print x[0],x[1],x[2]
    
