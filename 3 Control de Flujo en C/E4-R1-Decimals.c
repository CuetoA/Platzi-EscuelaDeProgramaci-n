#include<stdio.h>

float num1, num2, num3;

int main(){

    printf("Enter two numbers: \n");
    printf("Number 1: ");
    scanf("%f", &num1);
    printf("Number 2: ");
    scanf("%f", &num2);


    num3 = num1 + num2;
    printf("Answer: %0.4f", num3);

    return 0;
}