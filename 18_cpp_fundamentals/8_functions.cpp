#include <iostream>
using namespace std;

int multiply(int a, int b){
    return a * b;
}

float divide(float a, float b){
    return a/b ;
}


int main(){
    int no1 = 9;
    int no2 = 4;

    cout << "Multiplication: " << multiply(no1, no2) << endl;
    cout << "Division:       " << divide(no1, no2) << endl;
}