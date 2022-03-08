#include <stdio.h>

int expression = 3;


int main(){
    switch (expression){
    case 1:
        printf("El caso es el %d", expression);
        break;
    case 2:
        printf("El caso es el %d", expression);
        break;
    default:
        printf("Bis Morgen Bitch!");
        break;
    }
}
