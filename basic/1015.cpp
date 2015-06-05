#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;
struct student{
    int id;
    int x;
    int y;
};
int cmp(const student& a,const student& b)
{
    if (a.x+a.y>b.x+b.y) return 1;
    if (a.x+a.y<b.x+b.y) return 0;
    if (a.x>b.x) return 1;
    if (a.x<b.x) return 0;
    if (a.id>b.id) return 0;
    else return 1;
}
void myprint(vector<student>& a){
    vector<student>::iterator it;
    for(it=a.begin();it!=a.end();it++)
    {
        printf("%d %d %d\n",it->id,it->x,it->y);
    }
}
int main()
{
    int n,l,h;
    scanf("%d%d%d",&n,&l,&h);
    int i,num;
    num=n;
    vector<student> a,b,c,d;
    int id,x,y;
    for(i=0;i<n;i++)
    {
        scanf("%d%d%d",&id,&x,&y);
        if (x<l || y<l)
        {
            num--;
            continue;
        }
        student t;
        t.id=id;
        t.x=x;
        t.y=y;
        if(x>=h&&y>=h) a.push_back(t);
        else
            if (x>=h && y<h) b.push_back(t);
            else
                if(x<h &&y<h&&x>=y) c.push_back(t);
                else d.push_back(t);

    }
    sort(a.begin(),a.end(),cmp);
    sort(b.begin(),b.end(),cmp);
    sort(c.begin(),c.end(),cmp);
    sort(d.begin(),d.end(),cmp);
    printf("%d\n",num);
    myprint(a);
    myprint(b);
    myprint(c);
    myprint(d);
    return 0;
}
