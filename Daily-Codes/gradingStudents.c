#include<stdio.h>
int main()
{
    int n,i,temp;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        if(a[i]<38)
        {
            printf("%d\n",a[i]);
        }
        else 
        {
            temp=a[i]%5;
            if(temp>2)
            {
                a[i]=a[i]+(5-temp);
            }
            printf("%d\n",a[i]);
        }
    }
    return 0;
}