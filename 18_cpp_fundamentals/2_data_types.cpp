// Differents compilers -> different data sizes sometimes

#include <iostream>

using namespace std;

int main(){
    int age = 0;
    char letter = 'andres';

    cout << age << endl;
    cout << letter << endl;
    
    
    int age_list[] = {1,2,3,4};
    
    cout << age_list << endl;
    cout << age_list[1] << endl;

}
