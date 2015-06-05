import sys

max=-1
min=101
imax=-1
imin=-1
smax=[]
smin=[]
n=(int)(raw_input())
for i in range(n):
    x=sys.stdin.readline().strip('\n')
    x1=x.split(' ')
    grade=int(x1[2])
    if(grade>max):
        imax=i
        max=grade
        smax=x1
    if(grade<min):
        imin=i
        min=grade
        smin=x1
print smax[0],smax[1]
print smin[0],smin[1]
    

    
