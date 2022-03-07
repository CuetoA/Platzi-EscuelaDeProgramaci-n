#include<stdio.h>
#include<string.h>
#include<ctype.h>

char word[20];
int vowel, len, newlen;



void vowelCase(){
    len = strlen(word);
    newlen = len + 3;

    strcat(word, "way");
    printf("salida: %s", word);

}


void consonantCase(){
    char temp = word[0];
    int i, len = strlen(word);

    for(i=1; i<=len; i++){
        word[i-1] = word[i];
    }
    word[len-1] = temp;    

    strcat(word, "ay");
    printf("salida: %s", word);
}


int main(){

    printf("Enter a word:");
    gets(word);

    char c = tolower(word[0]);
    vowel = (c=='a' || c=='e' || c=='i' || c=='o' || c=='u');

    if(vowel){
        vowelCase();
    }
    else
        consonantCase();
    return 0;
}