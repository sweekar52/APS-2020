#include<stdio.h>

int find(int arr[], int u, int v){
    return arr[u] == arr[v];
}

void funUnion(int arr[], int n, int u, int v){
    int toReplace = arr[u];
    for(int i = 0; i < n; i++){
        if(arr[i]==toReplace) arr[i] = arr[v];
    }
}

void printArr(int arr[], int n){
    for(int i=0;i<n;i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main(){
    int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    funUnion(arr, 10, 2, 1);
    printArr(arr, 10);
}