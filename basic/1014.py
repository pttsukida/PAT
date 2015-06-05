import sys
a=sys.stdin.readline().strip('\n')
b=sys.stdin.readline().strip('\n')
c=sys.stdin.readline().strip('\n')
d=sys.stdin.readline().strip('\n')
s=['MON','TUE', 'WED', 'THU', 'FRI' ,'SAT', 'SUN']
l1=len(a)
l2=len(b)
if(l1>l2):
    l1=l2
j=0
for i in range(l1):
    if a[i]==b[i] and a[i]>='A' and a[i]<='Z':
        t1=ord(a[i])-ord('A')
        sys.stdout.write(s[t1]+' ')
        j=i
        break
i=j+1
while(i<l1):
    if a[i]==b[i] and ((a[i]>='0' and a[i]<='9')
                       or (a[i]>='A' and a[i]<='N')):
        if a[i]>='A' and a[i]<='N':
            t2=ord(a[i])-ord('A')+10
            sys.stdout.write(str(t2)+':')
        if a[i]>='0' and a[i]<='9':
            t2=ord(a[i])-ord('0')
            sys.stdout.write('0'+str(t2)+':')
        break
    i+=1     
l1=len(c)
l2=len(d)
if(l1>l2):
    l1=l2
for i in range(l1):
    if c[i]==d[i] and ((c[i]>='A' and c[i]<='Z')or(c[i]>='a' and c[i]<='z')):
        if(i<10):
            sys.stdout.write('0')
        sys.stdout.write(str(i))
        break
