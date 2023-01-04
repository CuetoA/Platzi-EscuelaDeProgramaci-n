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

    ~Persona(){
        /* Destructor
            We use them when we've used dynamic memory
            e.g. pointers 

            They will be invoced either at the end of main function or 
            by triggering it with delete <name_variable>;
        */ 
       cout << "Destroyer" << endl;
    }

    void heloThere(){
        cout << "hello there " << name << endl;
    }
};


int main() {
    
    Persona* person1 = new Persona("Andrés");
    cout << person1->name << endl;
    person1 -> heloThere();

    delete person1;


    Persona* person2 = new Persona("Trujis");
    cout << person2->name << endl;
    person2 -> heloThere();
}