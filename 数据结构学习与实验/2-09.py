import sys

m=map(int,raw_input().split(' '))
n=m[0]
x=sys.stdin.readline().split(' ')
box=[100]
for i in range(n):
    w=int(x[i])
    ok=0
    for j in range(len(box)):
        if(w<=box[j]):
            box[j]=box[j]-w
            print w,j+1
            ok=1
            break
    if(ok==0):
        box.append(100-w)
        print w,len(box)
print len(box)
