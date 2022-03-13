#include <stdio.h>

int n = 21;


int main(){
    if(n < 10)
        printf("El numero es menor a 10");
    else if(n >= 10 && n<20)
        printf("El numero está entre 10 y 20 ");
    else 
        printf("El numero es mayor a 20");
    
    return 0;
}