#include<stdio.h>


int main(){

    // a = 5(00000101), b = 9(00001001)
    unsigned char a = 5, b = 9; 
  
    // The result is 0010 0000 push five zeros at the left of this number
    printf("a<<1 = %d\n", 3<<a);
    
    // The result is 18 = 000100100 
    printf("b<<1 = %d\n", b<<2);  
    return 0;
}