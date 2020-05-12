#include<stdio.h>

int getRoot(int arr[],int i){
  while(arr[i] != i){
    i = arr[i];
   i;
  return i;
  }
}

void formUnion(int arr[], int u, int v){
  int rootU = getRoot(arr, u);
  int rootV = getRoot(arr, v);
  arr[rootV] = arr[rootU];
}

int find(int arr[], int u, int v){
  int rootU = getRoot(arr, u);
  int rootV = getRoot(arr,v);
  return rootU == rootV;
}

int main(){
  int arr[10];
  for(int i=0;i<10;i++){
    arr[i] = i;
  }
  formUnion(arr,0,1);
  formUnion(arr,0,5);
  formUnion(arr,5,7);

  for(int i=0;i<10;i++){
    printf("%d ",arr[i]);
  }
  printf("\n%d", find(arr,0,1));
  printf("\n%d", find(arr,0,7));
  return 0;
}