#include<stdio.h>

int max(int a,int b,int c)
{
    if(a<b)
    {
        a=b;
    }
    if(a<c)
    {
        a=c;
    }
    return a;
}


int rod_cutting(int n)
{
    int result[n+1],i,j;
    result[0]=0;
    result[0]=0;
    for(i=2;i<=n;i++)
    {
        result[i]=0;
    }
    for(i=2;i<=n;i++)
    {
        for(j=1;j<=i/2;j++)
        {
            result[i]=max(result[i],j*(i-j),j*result[i-j]);
        }
    }
    return result[n];
}


int main()
{
    int n=7;
    int result = rod_cutting(n);
    printf("%d\n",result);
}