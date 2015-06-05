import sys


n=(int)(raw_input())
s=range(n+1)
s.remove(0)
s.remove(1)
i=0
while(i<len(s)-1):
    a=s[i]
    t=a
    while(t<n):
        t=t+a
        if(t in s):
            s.remove(t)
    i=i+1
count=0
for i in range(len(s)-1):
    if(s[i+1]-s[i]==2):
        count=count+1
print count
