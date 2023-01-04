#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


class Persona{
private:
    string name;
    int age;

public:
    Persona(string n, int a): name(n), age(a) {}

    ~Persona(){
       cout << "Destroyer" << endl;
    }

    string getName(){
        return name;
    }

    void heloThere(){
        cout << "hello there " << name << endl;
    }
};


int main() {
    
    Persona* person1 = new Persona("Andrés", 24);
    cout << person1->getName() << endl;
    person1 -> heloThere();
    delete person1;
    cout << endl;


    Persona* person2 = new Persona("Trujis", 24);
    cout << person2->getName() << endl;
    person2 -> heloThere();
}