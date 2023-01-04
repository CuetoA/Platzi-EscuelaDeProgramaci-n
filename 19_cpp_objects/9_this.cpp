#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


class Persona{
private:
    string name;
    int age;

public:
    Persona(string name, int age){
        this->name = name;
        this->age = age;
    }

    ~Persona(){
       cout << "Destroyer" << endl;
    }

    string getName(){
        return this->name;
    }

    Persona &setAge(int age){
        this->age = age;
        return *this;
    }

    Persona &setName(string name){
        this->name = name;
        return *this;
    }

    void heloThere(){
        cout << "hello there " << this->name << " of age " << this->age << endl;
    }
};


int main() {
    
    Persona* person1 = new Persona("Andrés", 24);
    person1->setName("Cuetorra").setAge(25);
    cout << person1->getName() << endl;
    person1 -> heloThere();
    delete person1;
    cout << endl;


    Persona* person2 = new Persona("Trujis", 24);
    cout << person2->getName() << endl;
    person2 -> heloThere();
}