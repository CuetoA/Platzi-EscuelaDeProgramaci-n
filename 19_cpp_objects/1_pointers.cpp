#include <iostream>
using namespace std;


int main(){
    string my_str = "hello there";
    string *pointer = &my_str;

    cout << "This is original variable:                         " << my_str << endl;
    cout << "This is my original variable memory address:       " << &my_str << endl;
    cout << "This is my pointer value:                          " << pointer << endl;
    cout << "This the value stored in my pointer value address: " << *pointer << endl;
    cout << "This is my pointer variable memory address:        " << &pointer << endl;

}