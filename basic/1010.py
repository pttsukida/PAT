import sys

def add(k1,k2,dic,keys):
    k1=int(k1)
    if(dic.has_key(k1)):
        dic[k1]=float(dic[k1])+float(k2)
    else:
        dic[k1]=float(k2)


def bigadd(x,dic,keys):
    i=1
    while(i<len(x)):
        add(x[i],x[i+1],dic,keys)

        i=i+2
x=sys.stdin.readline()
y=sys.stdin.readline()
x=x.split(' ')
y=y.split(' ')
i=1
keys=[]
dic={}
bigadd(x,dic,keys)
bigadd(y,dic,keys)
print len(dic),
for key in sorted(dic.iterkeys(),reverse=True):
    if(float(dic[key])!=0):
        print key, '%.1f'%dic[key],
