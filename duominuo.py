# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 21:47:41 2018

@author: Administrator
"""


#include<cstdio>
#include<iostream>
#include<algorithm>
#define p1 id<<1
#define p2 id<<1^1
using namespace std;
int n;
int ans[100005];
int tree[450000];
struct ty
{
    int x,h,id,to;
}d[100005];
bool cmp(ty a,ty b)
{
    return a.x<b.x;
}
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        scanf("%d%d",&d[i].x,&d[i].h);
        d[i].id=i;
        d[i].to=d[i].x+d[i].h-1;
    }
    sort(d+1,d+n+1,cmp);
    ans[d[n].id]=1;
    for(int i=n-1;i>=1;i--) 
    {
        int last=d[i].to;
        int q=i+1;
        ans[d[i].id]=1;
        while(0==0)
        {
            if(q>n) break;
            if(d[q].x<=last) ans[d[i].id]+=ans[d[q].id];  //为什么不用更新last，因为我在当前点能到的范围之外的点，要是能推倒的话，肯定已经包括在当前范围里的某个点中
            else break;
            q=q+ans[d[q].id];
        }
    }   
    for(int i=1;i<n;i++) cout<<ans[i]<<' ';
    cout<<ans[n]<<endl;
    return 0;
}