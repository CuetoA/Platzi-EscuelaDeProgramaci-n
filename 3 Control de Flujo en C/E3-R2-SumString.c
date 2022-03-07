#include <stdio.h>
#include <string.h>

char  name[10],  middleName[10],  lastName[10];
int l1, l2, l3, l4;
char destination[30];


int main(){

    printf("Name: \t\t");
    gets(name);
    printf("Middle Name: \t");
    gets(middleName);
    printf("Last Name: \t");
    gets(lastName);

    concatenation( name, middleName, lastName);

    return 0;
}

void concatenation(char* name, char* middleName, char* lastName){
    
    
    strcat(destination, name);
    strcat(destination, " ");
    strcat(destination, middleName);
    strcat(destination, " ");
    strcat(destination, lastName);

    printf("concatening: %s \n", destination);

    return;
}