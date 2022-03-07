#include<stdio.h>
#include<string.h>
#include<ctype.h>

char nombre[30], space = ' ';


void title(){

    int i, len;
    len = strlen(nombre);

    for(i = 0; i <= len; i++){

        if( i == 0){ nombre[i] = toupper(nombre[i]);}
        if( i>0)
            if(nombre[i-1]==space){ nombre[i] = toupper(nombre[i]); }    
    }

    printf("Cadena final: %s", nombre);

}


int main(){

    printf("Ingrese su nombre: ");
    gets(nombre);
    title();

    return 0;
}

