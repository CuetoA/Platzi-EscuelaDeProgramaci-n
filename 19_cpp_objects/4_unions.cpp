#include <iostream>
using namespace std;

// Until now we just read that it is to save memory, but I don't get to se the utility yet
// could it be like... for auxiliar variables that may take multiple types? :thinking:

int main(){

    union int_n_char {
        int number;
        char letter;
        float numfl;
        bool mybol;
    };

    int_n_char X = {'a'};
    cout << "int_nchar as a number: " << X.number << endl;
    cout << "int_nchar as a letter: " << X.letter << endl;
    cout << "int_nchar as a float:  " << X.numfl  << endl;
    cout << "int_nchar as a bool:   " << X.mybol  << endl;
    cout << endl;

    int_n_char Y = {};
    cout << "int_nchar as a number: " << Y.number << endl;
    cout << "int_nchar as a letter: " << Y.letter << endl;
    cout << "int_nchar as a float:  " << Y.numfl  << endl;
    cout << "int_nchar as a bool:   " << Y.mybol  << endl;
    cout << endl;

}