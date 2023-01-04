/*
    Object life-cycle:
    - Set memory space
    - Call constructor
    - Activity period
    - Call destructor 
    - Free memory space
*/


#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


class Persona{
public:
    string name = "Andrés";
    int age = 24;

    void heloThere(string name){
        cout << "hello there " << name << endl;
    }
};


int main() {
    
    Persona* person = new Persona();
    cout << person->name << endl;
    person -> heloThere("Test");
}