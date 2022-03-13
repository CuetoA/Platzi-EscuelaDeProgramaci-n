#include<stdio.h>
#include<stdlib.h>

int binary[12], n, i;

int main(){

    system("cls");
    system("color 9F");

    printf("Enter a decimal number\n");
    scanf("%d", &n);

    for(i=0 ; n>0 ; i++){

        binary[i] = n % 2;
        n = n / 2;
    }

    printf("The answer of %d in binary is: ", n);
    for(i = i -1 ; i >= 0 ; i--){ printf("%d", binary[i]); }



    return 0;
}