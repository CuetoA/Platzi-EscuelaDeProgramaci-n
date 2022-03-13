#include <stdio.h>

int maxOfFour(int array[4]){
  int max = array[0];

  for (int i=0; i<4; i++){
    if(array[i] > max){max = array[i];}
  }

  return max;
}

int main(){
  int array[4] = {1, 2, 17, 5};
  int res = maxOfFour(array);
  printf("%d", res);
  printf("");

  return 0;
}