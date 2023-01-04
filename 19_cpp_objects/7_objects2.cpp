#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


class Persona{
public:
    string name;
    int age;

    Persona(string n){
        name = n;
    }

    void heloThere(){
        cout << "hello there " << name << endl;
    }
};


int main() {
    
    Persona* person1 = new Persona("Andrés");
    cout << person1->name << endl;
    person1 -> heloThere();
}