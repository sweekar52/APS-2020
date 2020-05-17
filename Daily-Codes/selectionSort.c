#include <stdio.h>
#include <stdlib.h>

void selection(int a[],int n)
{
    int i,j,temp,min;
    for(i=0;i<n-1;i++)
    {
        min=i;
        for(j=i+1;j<n;j++)
        {
            if(a[j]<a[min])
            {
              min=j;
            }
        }
        temp=a[min];
        a[min]=a[i];
        a[i]=temp;
    }

    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}
int main()
{
    int i,j,n,a[100];
    printf("enter the size of the array");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    selection(a,n);
    return 0;
}