#include <iostream>
using namespace std;

struct Person{
    string name;
    int    age; 
};


int main(){
    Person scarlette = Person();    // Saves the memory at compilation
    Person andres;
    Person *boni = new Person();    // Dosnt save memory at compilation but use it dinamically (at excecution)

    scarlette.name = "Scarlette Bello Barron";
    scarlette.age = 45;

    andres.name = "Andrés Cueto Estrada";
    andres.age = 24;

    boni -> name = "Boni Estrada";
    boni -> age = 13;


    cout << "Scar data: " << endl;
    cout << "   complete name: " << scarlette.name << endl;
    cout << "   complete age:  " << scarlette.age  << endl << endl;

    cout << "Andres data: " << endl;
    cout << "   complete name: " << andres.name << endl;
    cout << "   complete age:  " << andres.age  << endl << endl;

    cout << "Boni data: " << endl;
    cout << "   complete name: " << boni -> name << endl;
    cout << "   complete age:  " << boni -> age  << endl << endl;
}