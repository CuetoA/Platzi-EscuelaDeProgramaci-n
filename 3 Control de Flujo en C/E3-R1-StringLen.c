#include <stdio.h>
#include <string.h>

char str[5];
int len; 

int main(){

    str[20];
    printf("Enter a String: ");
    gets(str);

    len = strlen(str);
    printf("\n\ttest: %s \t and it's len is: %d", str, len);
}