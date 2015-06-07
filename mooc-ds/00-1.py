import sys

x=sys.stdin.readline().strip('\n').split()
n=int(x[0])
c=x[1]

i=1
s=1
while True:
    i+=1
    s+=2*(2*i-1)
    if n<=s:
        s-=2*(2*i-1)
        i-=1
        break
j=i-1
q=[]
while j>=0:
    q.append(j)
    j-=1
j=1
while j<i:
    q.append(j)
    j+=1
for j in q:
    line=' '*(i-1-j)+(2*j+1)*c
    print line
print n-s