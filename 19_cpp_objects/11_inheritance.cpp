#include <iostream>
#include <stdio.h>
#include <string>


using namespace std;


class Animal{
    protected:
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
};

Animal::~Animal (){
    cout << "Deleting new animal" << endl;
    number_animals -= 1;
};

int Animal::getNumberAnimals (){
    return number_animals;
};





class Herbivorous : public Animal {
    public:
    Herbivorous() : Animal() {
        this->food = "plants";
    }

    void pasture(){
        cout << "This animal is pasting" << endl;
    }
};


class Carnivorois : public Animal {
    public:
    Carnivorois() : Animal(){
        this-> food = "meat";
    }

    void hunt(){
        cout << "This animal is hunting" << endl; 
    }
};



class Omnivorous : public Herbivorous, public Carnivorois {
    public:
    Omnivorous(): Herbivorous(), Carnivorois() {}

    void eat(){
        this->Herbivorous::eat();
        this->Herbivorous::eat();
    }

};



int main(){
    Animal *my_new_animal = new Animal();
    Herbivorous *new_herb = new Herbivorous();
    Carnivorois *new_carb = new Carnivorois();
    Omnivorous *new_omn   = new Omnivorous();

    cout << "Number of animals is " << Animal::getNumberAnimals() << endl;

    my_new_animal->eat();
    cout << endl;

    new_herb->pasture();
    new_herb->eat();
    cout << endl;

    new_carb->hunt();
    new_carb->eat();
    cout << endl;

    // new_omn->Herbivorous::eat();
    new_omn->eat();

    delete my_new_animal;
    cout << "Number of animals is " << Animal::getNumberAnimals() << endl;
}

/*
    Here we learned multiple things:
    1.- We can't leave null elements even if they're static
    2.- When creating an object we have:
        Object <name> = new Object();
          |                    |
          v                    v
        The object type ||  Literally this is the constructur
    3.- how to make inheritance
*/