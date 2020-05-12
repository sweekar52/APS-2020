#include<stdio.h>
int main()
{
    int n,i;
    float x=0,y=0,z=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
        if(a[i]>0)
            x++;
        else if(a[i]<0)
            y++;
        else
            z++;
    }
    printf("%f\n",(x*1.0)/n);
    printf("%f\n",(y*1.0)/n);
    printf("%f\n",(z*1.0)/n);
    
    return 0;
}