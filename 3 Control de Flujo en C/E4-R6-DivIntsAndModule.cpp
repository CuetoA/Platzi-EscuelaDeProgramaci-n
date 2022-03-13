#include<stdio.h>
#include<iostream>

using namespace std;

int numerator, denominator, module, total;

int main(){

    printf("Enter numerator: ");
    scanf("%d", &numerator);
    printf("Enter denominator: ");
    scanf("%d", &denominator);

    module = numerator % denominator;
    total =  int(numerator / denominator );
    
    printf("Total: %d \n", total);
    printf("Module: %d\n", module);

    return 0;
}