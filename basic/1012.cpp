#include <iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int x;
    int a1=0;
    int a2=0;int flag=1;int c2=0;
    int a3=0;
    double a4=0;int c4=0;
    int a5=-1;
    for(int i=1;i<=n;i++)
    {
        cin>>x;
        if(x%10==0) a1+=x;
        if(x%5==1) {a2+=flag*x;flag=-flag;c2++;}
        if(x%5==2) a3++;
        if(x%5==3) {a4+=x;c4++;}
        if(x%5==4) {if(x>a5) a5=x;}

    }
    if(a1==0) cout<<"N ";else cout<<a1<<" ";
    if(c2==0) cout<<"N ";else cout<<a2<<" ";
    if(a3==0) cout<<"N ";else cout<<a3<<" ";
    if(c4==0) cout<<"N ";else printf("%.1lf ",a4/c4);
    if(a5==-1) cout<<"N";else cout<<a5;

    return 0;
}