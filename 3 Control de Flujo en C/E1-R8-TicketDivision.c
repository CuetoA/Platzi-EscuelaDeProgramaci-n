#include <stdio.h>

void dividiendoCuenta(){

    int amount, people;

    printf("Amount to pay: ");
    scanf("%d", &amount);
    printf("Number of people: ");
    scanf("%d", &people);

    int sum = amount / people;
    printf("The cost per person is: %d", sum);
}


int main(){
    dividiendoCuenta();
    return 0;
}