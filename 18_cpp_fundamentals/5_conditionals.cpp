#include <iostream>

using namespace std;

int main() {

    char mystr[] = "trying";
    string oth_str = "another string";
    cout << mystr << endl << oth_str << endl;

    const int number = 10;
    int in = 0;

    cout << "Original number is: " << number << endl;
    cout << "Introduce a number: ";
    cin >> in;
    cout << endl;

    if(number == in){
        cout << "The numbers are equal" << endl;
    }
    else if (number > in){
        cout << "The original number is GREATER than the input" << endl;
    }
    else{
        cout << "The original number is LOWER than the input" << endl;
    }

}