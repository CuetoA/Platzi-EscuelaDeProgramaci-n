#include<stdio.h>

float num;
float ans;

int main(){
    printf("Enter a number: ");
    scanf("%f", &num);

    ans = sqrt(num);
    printf("The answer is: %0.4f", ans);

    return 0;
}