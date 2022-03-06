/*
    Variables delacation. 02/03/2022
*/
#include <stdio.h>
#define TEST 27

extern int a, b, c;
float f, g, h;

int main(){
    //Variables
    int a, b, c, g, h, w;
    const int PRICE = 1000;                     //Constants in mayus
    // variable initalization
    a = -1000000000;
    b = 0b1111111111111111111111111111111;      //Creating overflow
    c = a + b;

    h = 1000.123456789;
    g = 1;
    w = h + g;
    printf("Resultado de suma: %d\n", c);
    printf("Resultado de suma: %d", w);         // Using decimals when wrong
    printf("Resultado de suma: %d", TEST);         // Using decimals when wrong
    return 0;
}