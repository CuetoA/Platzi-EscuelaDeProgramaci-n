/*
    Static members allow us to share memory within objects of the same class
    this may help us achieve certain behaviours faster or better in certain 
    use cases.
*/

#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;


class Persona{
private:
    string name;
    int age;

public:
    static int number_people;

    Persona(string name, int age);

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

    void heloThere();
};


int Persona::number_people = 0;
void Persona::heloThere(){
        cout << "hello there " << this->name << " of age " << this->age << endl;
}
Persona::Persona(string name, int age){
        this->name = name;
        this->age = age;
        number_people += 1;
}




int main() {
    
    Persona* person1 = new Persona("Andrés", 24);
    person1->setName("Cuetorra").setAge(25);
    cout << person1->getName() << endl;
    person1 -> heloThere();
    cout << endl;


    Persona* person2 = new Persona("Trujis", 24);
    cout << person2->getName() << endl;
    person2 -> heloThere();
    cout << endl;

    cout << "The number of people in Persona is: " << Persona::number_people << endl;
    cout << "The number of people in person1 is: " << person1->number_people << endl;
    cout << "The number of people in person1 is: " << person2->number_people << endl;
}