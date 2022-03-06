#include <stdio.h>
#include <string.h>

char str[20];
int len; 

int main(){

    printf("Enter a String: ");
    gets(str);

    len = strlen(str);
    printf("\n\ttest: %s \t and it's len is: %d", str, len);
}