
#include<stdio.h>
#include<ctype.h>

int main(){
    char str[100];
    int n;
    int sh;
    scanf("%d", &n);
    scanf("%s",str);
    scanf("%d", &sh);

    for(int i=0;i<n;i++){
        if(islower(str[i])>0){
            str[i] -= 'a';
            str[i] = (str[i] + sh)%26;
            str[i] += 'a';
        }else if(isupper(str[i])>0){
            str[i] -= 'A';
            str[i] = (str[i] + sh)%26;
            str[i] += 'A';
        }
        printf("%c",str[i]);
    }
}