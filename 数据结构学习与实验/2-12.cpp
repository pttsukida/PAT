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
    vector<int> a,b,c;
    vector<int>::iterator it,ia,ib;
    int n;
    while(scanf("%d",&n)&&n!=-1)
    {
        b.push_back(n);
    }
    while(scanf("%d",&n)&&n!=-1)
    {
        a.push_back(n);
    }
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    ia=a.begin();
    ib=b.begin();
    while(ia!=a.end()&&ib!=b.end())
    {
        if(*ia==*ib)
        {
            c.push_back(*ia);
            ia++;
            ib++;
        }
        else
            if(*ia>*ib) ib++;
            else ia++;
    }
    c.clear();
    set_intersection(a.begin(), a.end(), b.begin(), b.end(), back_inserter(c));
    int f=0;
    if(c.size()==0) {printf("NULL");}
    else
        for(it=c.begin();it!=c.end();it++)
        {
            if(f==0)
                printf("%d",*it);
            else
                printf(" %d",*it);
            f++;
        }
    return 0;
}
