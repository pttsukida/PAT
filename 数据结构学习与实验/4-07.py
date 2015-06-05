import sys
import heapq
n=map(int,raw_input())
x=map(int,raw_input().split())
heapq.heapify(x)
s=0
while(len(x)>=2):
    a=heapq.heappop(x)
    b=heapq.heappop(x)
    c=a+b
    heapq.heappush(x,c)
    s=s+c
print s
