#include<stdio.h>

int main(){

    int ans, base = 2, n = 3;
    
    printf("\n");
    ans = power(base , n);
    printf("ans: %d\n", ans);
    printf("Final value of n: %d\n\n", n);

    return 0;
}


int power(int base, int n){
    
    int i, ans = 1;
    
    for(i = 0; n > 0; n--){
        ans *= base;
        printf("\tValue of n inside function: %d\n", n);
    }

    return ans;
}