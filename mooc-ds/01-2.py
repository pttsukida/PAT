import sys

n=(int)(raw_input())
x=sys.stdin.readline().strip('\n').split()
x=map(int,x)



def maxlistSum(a):
    m1=-1 #原来m=0，可能在刚好和为0 却有正数下，区间选择不对
    m2=0

    start1=a[0]
    end1=a[-1]
    start2=a[0]
    end2=a[-1]

    for i,x in enumerate(a):
        if m2>=0:
            m2=x+m2
            end2=a[i]
        else:
            m2=x
            start2=a[i]
            end2=a[i]
        if m2>m1:
            m1=m2
            start1=start2
            end1=end2
    if(m1<0):
        m1=0
    return m1,start1,end1

q=maxlistSum(x)
print q[0],q[1],q[2]