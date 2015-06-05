import sys

def count_a(s):
    count=0
    for i in range(len(s)):
        if(s[i]=='A'):
            count=count+1
    return count
def all_is_a(s):
    if(count_a(s)==len(s)):
        return True
    else:
        return False
n=(int)(raw_input())
for i in range(n):
    x=sys.stdin.readline().strip('\n')
    x1=x.split('P')
    if(len(x1)!=2):
        print("NO")
        continue
    x2=x1[1].split('T')
    if(len(x2)!=2):
        print('NO')
        continue
    if(all_is_a(x1[0]) and all_is_a(x2[0]) and all_is_a(x2[1])
       and count_a(x1[0])*count_a(x2[0])==count_a(x2[1])
       and count_a(x2[0])>0):
        print("YES")
    else:
        print("NO")
    
