#include <iostream>
#include <stdio.h>
#include <string>


using namespace std;


class Animal{
private:
    static int number_animals;
    string food;

public:
    Animal();
    ~Animal();
    static int getNumberAnimals();

    string getFood(){
        return this->food;
    };

    void eat(){
        cout << "This animal is eating " << this->food << "... ñom ñom " << endl;
    };
};

int Animal::number_animals = 0;

Animal::Animal (){
    cout << "Creating new animal" << endl;
    number_animals += 1;
}

Animal::~Animal (){
    cout << "Deleting new animal" << endl;
    number_animals -= 1;
}

int Animal::getNumberAnimals (){
    return number_animals;
}



int main(){
    Animal *my_new_animal = new Animal();
    cout << "Number of animals is " << Animal::getNumberAnimals() << endl;

    my_new_animal->eat();

    delete my_new_animal;
    cout << "Number of animals is " << Animal::getNumberAnimals() << endl;
}