#include<stdio.h>
#include<math.h>

int x;
float result;

int main(){
    printf("Enter a value: ");
    scanf("%d", &x);

    result = cos(x);

    printf("The vauel of x is: %d\n", x);
    printf("The answer is: %f\n", result);
    return 0;
}