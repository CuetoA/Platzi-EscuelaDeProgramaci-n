#include<stdio.h>
#include<time.h>

void exercise1(void);
void exercise2(void);


int main(){

    //exercise1();
    exercise2();
    return 0;
}

void exercise1(){
    time_t seconds;

    seconds = time(NULL);
    printf("The number of hours since Jan 1 1970 00:00 i: %ld \n", seconds/3600);

    return;
}

void exercise2(){

    time_t end, begin;
    long i;

    begin = time( NULL );
    for(i=0 ; i <= 1500000000; i++);
    end = time( NULL );

    float dif = end - begin;
    printf("The time in milliseconds that the for lasted was: %f\n", dif );
    return;
}