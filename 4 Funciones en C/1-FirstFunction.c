#include<stdio.h>

void hello(char* message);


int main(){

    //char message[10] = "Bola";
    hello("Bola 2");
    return 0;
}

void hello(char* message){
    printf("The message is: %s", message);
}