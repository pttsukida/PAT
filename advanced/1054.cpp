#include<stdio.h>

using namespace std;
int a[480000];
int main()
{
    int x,y,i;
    scanf("%d%d",&x,&y);
    int l=x*y;
    for(i=0;i<l;i++)
        scanf("%d",&a[i]);
    int num=1,val=a[0];
    for(i=1;i<l;i++){
        if(num==0)
        {
            val=a[i];
            num=1;
            continue;
        }
        if(a[i]!=val)
            num--;
        else
            num++;
    }
    printf("%d",val);
    return 0;
}