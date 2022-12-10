#include <iostream>
using namespace std;

int multiply(int a, int b){
    return a * b;
}

void divide(float a, float b, string st="holi" ){
    cout << "BTW, your default message is: " << st << endl;
    cout << "Division:       " << a/b << endl;
}


int main(){
    int no1 = 9;
    int no2 = 4;

    cout << "Multiplication: " << multiply(no1, no2) << endl;
    divide(no1, no2);
}
