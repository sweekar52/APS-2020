#include <stdio.h>
#include <limits.h>
#define lli long long int

lli segTree[2000000];
lli arr[1000000];

lli min(lli a, lli b)
{
  return a < b ? a : b;
}

void generateTree(lli l, lli r, lli i)
{
  if (l == r)
  {
    segTree[i] = arr[l];
    return;
  }

  lli mid = (l + r) / 2;
  generateTree(l, mid, 2 * i + 1);
  generateTree(mid +1, r, 2 * i + 2);
  segTree[i] = min(segTree[2 * i + 1], segTree[2 * i + 2]);
}

lli query(lli ql, lli qr, lli tl, lli tr, lli ind){
  if(ql<=tl && qr>=tr){ //total overlap
    return segTree[ind];
  }
  if(ql>tr || qr<tl){ //no overlap
    return LLONG_MAX;
  }
  //partial overlap
  lli mid = (tl+tr)/2;
  return min(query(ql,qr,tl,mid,2*ind+1), query(ql,qr,mid+1,tr,2*ind+2));
}

int main()
{
  for (int i = 0; i < 10; i++)
  {
    arr[i] = i;
  }
  generateTree(0, 9, 0);
  for (int i = 0; i < 20; i++)
  {
    printf("%lld ", segTree[i]);
  }
  printf("%lld\n", query(0,9,0,9,0));
  printf("%lld\n", query(4,7,0,9,0));
  return 0;
}