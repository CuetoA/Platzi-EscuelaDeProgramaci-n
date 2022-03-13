#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

char input[30];
int flag = 0, len, i;

int main(){
    printf("Ingrese una frase: ");
    gets(input);

    len = strlen(input);
    char output[len];

    for(i =0; i <= len; i++){
        if(input[i] == ' ' ){
            output[i] = input[i];
            flag = abs( flag -1 );
            continue;
            }
        if(flag == 0){output[i] = toupper( input[i] );}
        if(flag== 1){output[i] = tolower( input[i] ); }
    }

    printf("Resultado: \n\t%s", output);
    return 0;
}