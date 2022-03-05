// bdw, while is when you dont know how many times to do something
#include <stdio.h>

condition = 0;

int main(){
    do{
        condition += 1;
        if (condition >= 5) {continue;}
        printf("Conditions value is: %d\n", condition);

    } while (condition >= 1 && condition <= 10);
    
    printf("Conditions value is: %d\n", condition);
    return 0;
}