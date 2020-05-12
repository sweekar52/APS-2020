#include<stdio.h>

int main()
{
    unsigned int v=17; // current permutation of bits 
    unsigned int w; // next permutation of bits

    unsigned int t = (v | (v - 1)) + 1;
    w = t | ((((t & -t) / (v & -v)) >> 1) - 1);

    printf("%u",w);
    return 0;
}