#include <stdio.h>
int L1, L2, X;

void getValues(){
    
    printf("Enter Lower limit: ");
    scanf("%d", &L1);
    printf("Enter Upper limit: ");
    scanf("%d", &L2);

    printf("Enter X: ");
    scanf("%d", &X);
    return;
}

void graphicLine(){
    graph();
    values();
    return;
}

void graph(){
    char c1 = 'X', c2 = '-';
    printf("L1");
    graphInter(c1 , c2);
    printf("L2\n");
    return;
}

void values(){
    char c1 = X , c2 = ' ';
    printf("%d" , L1);
    graphInter(c1 , c2);
    printf("%d" , L2);
    return;
}



void graphInter(char c1, char c2){

    int i;
    for (i = L1; i <= L2; i++){
        if(i == X){
            printf("%c", c1);
            continue;
        }
        printf("%c", c2);
    }
    return;
}
 

int main(){
    getValues();
    graphicLine();
    return 0;
}