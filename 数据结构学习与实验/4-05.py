import sys

child={}
parent={}
x=sys.stdin.readline().strip('\n').split(' ')
n=int(x[0])
m=int(x[1])
def read():
    queue=[]
    global child,parent,n

    now=0
    for i in range(n):
        y=sys.stdin.readline().strip('\n').split('  ')
        a=y[-1]
        if(now==0):
            queue.append(a)
            now=now+1
            #print child,now,queue
            continue
            
        if(len(y)>now):
            s=queue[-1]
            child[s]=[a]
            parent[a]=s
            queue.append(a)
            now=now+1
            #print child,now,queue
            continue
        if (len(y)==now):
            s=queue[-2]
            child[s].append(a)
            parent[a]=s
            queue[-1]=a
            #print child,now,queue
            continue
        if(len(y)<now):
            for j in range(now-len(y)+1):
                queue.pop()
                now=now-1
            s=queue[-1]
            child[s].append(a)
            parent[a]=s
            queue.append(a)
            now=now+1
            #print child,now,queue
            continue
def ischild(c,p):
    global child
    if child.has_key(p) and (c in child[p]):
        return True
    else:
        return False
def isancestor(a,d):
    global child
    q=[]
    if child.has_key(a):
        for x in child[a]:
            q.append(x)
    #print q
    while(len(q)>0):
        if d in q:
            return True
        else:
            t=q.pop()
            if child.has_key(t):
                q=q+child[t]
        #print q
    return False
def issib(a,b):
    if parent.has_key(a) and parent.has_key(b) and parent[a]==parent[b]:
        return True
    else:
        return False
        
read()
for i in range(m):
    x=sys.stdin.readline().strip('\n').split(' ')
    if(x[3]=='child'):
        print ischild(x[0],x[5])
    if(x[3]=='parent'):
        print ischild(x[5],x[0])
    if(x[3]=='sibling'):
        print issib(x[0],x[5])
    if(x[3]=='descendant'):
        print isancestor(x[5],x[0])
    if(x[3]=='ancestor'):
        print isancestor(x[0],x[5])
    
    


