#include <stdio.h>


void option(int opt){
    switch (opt){
    case 1:
        printf("Today We are going to learn to programm");
        break;
    case 2:
        printf("¿What about a marketing course?");
        break;
    case 3:
        printf("Today is a great day to lear UX/UI");
        break;
    case 4:
        printf("What if we learn about online Business today?");
        break;
    case 5:
        printf("Let's take audio-visual production classes today");
        break;
    case 6:
        printf("It could be good to develop a soft skill in platzi");
        break;
    default:
        printf("Eter a valid input");
        break;
    }

    return;
}

int inputMessage(){
    int option = 0;

    printf("Select an option between 1 to 6: ");
    scanf("%d", &option);

    return option;
}


int main(){

    int selection = inputMessage();
    option(selection);
    
    return 0;
}