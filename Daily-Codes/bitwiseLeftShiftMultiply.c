#include<stdio.h>

int main(){
    int a=20;
    printf("%d * 2 %d\n",a,a<<1);
    printf("%d * 4 %d\n",a,a<<2);
    printf("%d * 8 %d\n",a,a<<3);
    printf("%d * 16 %d\n",a,a<<4);
    return 0;
}