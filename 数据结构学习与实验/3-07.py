import sys

x=sys.stdin.readline().strip('\n').split(' ')

op=['+','-','*','/']
k=len(x)-1
s=[]
ok=1

while(k>=0):
    if x[k] not in op:
        x[k]=float(x[k])
    k=k-1
k=len(x)-1
while(k>=0):
    if x[k] in op:
        if(x[k]=='+'):
            if(len(s)==0):
                ok=0
                break
            if(len(s)>=2):
                a=s.pop()
                b=s.pop()
                s.append(a+b)
        if(x[k]=='-'):
            if(len(s)==0):
                ok=0
                break
            if(len(s)>=2):
                a=s.pop()
                b=s.pop()
                s.append(a-b)
        if(x[k]=='*'):
            if(len(s)==0):
                ok=0
                break
            if(len(s)>=2):
                a=s.pop()
                b=s.pop()
                s.append(a*b)
        if(x[k]=='/'):
            if(len(s)==0):
                ok=0
                break
            if(len(s)>=2):
                a=s.pop()
                b=s.pop()
                if(b==0):
                    ok=0
                    break
                s.append(a/b)
    else:
        s.append(x[k])
    k=k-1
if(ok==0 or len(s)!=1):
    print 'ERROR'
else:
    print '%.1f'%s[0]
               
            
            

