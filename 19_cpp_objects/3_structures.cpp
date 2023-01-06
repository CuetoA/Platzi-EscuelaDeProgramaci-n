#include <iostream>
using namespace std;

/*
    Like an arry with different datatypes
*/

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


/*
    Create variables in compilation time or dynamic memory:
    - Compilation time:
        it saves the space since the moment we're programming
        Persona p = Persona();

    - Dynamic memory:
        it creates the object and uses memory untill the programm is running
        Persona *p = new Persona(); 

        we use the word new to indicate that we're creating a new object called Persona
    
*/