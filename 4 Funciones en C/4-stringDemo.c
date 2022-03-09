#include<stdio.h>
#include<string.h>

int main(){

    //exercise1();
    exercise2();

    return 0;
}

void exercise1(){
    char string[160];

    printf("Escribe una frase:\n");
    gets(string);
    strrev(string);

    printf("The new phras is: \n %s", string);
    return;
}

void exercise2(){
    char string1[160], string2[160];

    printf("Writes a phrase:\n");
    gets(string1);
    printf("Writes a phrase:\n");
    gets(string2);

    if(strcmp(string1 , string2) == 0){
        printf("The prases are EQUAL");
    }else{
        strcat(string1 , string2);
        printf("The prases are DIFFERENT: %s", string1);
    }

    return;
}
