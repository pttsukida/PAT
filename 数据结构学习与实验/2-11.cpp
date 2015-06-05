#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;
bool cmp(int a,int b)
{
    return a>b;
}

int main()
{
    vector<int> a;
    vector<int>::iterator it;
    int n;
    while(scanf("%d",&n)&&n!=-1)
    {
        a.push_back(n);
    }
    while(scanf("%d",&n)&&n!=-1)
    {
        a.push_back(n);
    }
    sort(a.begin(),a.end());
    int f=0;
    if(a.size()==0) {printf("NULL");}
    else
        for(it=a.begin();it!=a.end();it++)
        {
            if(f==0)
                printf("%d",*it);
            else
                printf(" %d",*it);
            f++;
        }
    return 0;
}
