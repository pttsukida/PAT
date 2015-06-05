import sys

m=map(int,raw_input().split(' '))
n=m[0]
pw={}
resp=['New: OK','ERROR: Exist','Login: OK','ERROR: Not Exist','ERROR: Wrong PW']
for i in range(n):
    x=sys.stdin.readline().split(' ')
    if(x[0]=='L'):
        if(not pw.has_key(x[1])):
            print resp[3]
        else:
            if(pw[x[1]]==x[2]):
                print resp[2]
            else:
                print resp[4]
    if(x[0]=='N'):
        if(pw.has_key(x[1])):
            print resp[1]
        else:
            pw[x[1]]=x[2]
            print resp[0]
