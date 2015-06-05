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
    int n,x;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&x);
        a.push_back(x);
    }
    for(int i=0;i<n;i++)
    {
        scanf("%d",&x);
        b.push_back(x);
    }
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    set_union(a.begin(), a.end(), b.begin(), b.end(), back_inserter(c));
    int l=c.size();
    printf("%d",*(c.begin()+(l-1)/2));
    return 0;
}
