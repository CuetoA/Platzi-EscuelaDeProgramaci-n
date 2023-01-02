#include <iostream>
#include <string>
using namespace std;

int main() {

    // References
    //      If you change meal food changes too cs it is a REFERENCE
    cout << "Pointer:" << endl;
    string food = "Pizza";
    string &meal = food;

    cout << food << "\n";
    food = "No pizza now";
    
    cout << meal << "\n";
    meal = "Pizza again";
    cout << food << "\n";
    cout << endl;


    // Pointers
    //      In this example, meal2 won't change value because its type is "pointer" not just reference
    //      in order of changing it, we need to specify it with the * (dereference operator)
    cout << "Pointer:" << endl;
    string food2 = "Pizza";
    string* meal2 = &food2;

    cout << food2 << "\n";
    food2 = "No pizza now";
    
    cout << meal2 << "\n";
    meal2 = "Pizza again";
    cout << food2 << "\n";
    cout << endl;


    /* Finally we concluded:
        Pointers and references are almost the same, so it made not much sense and went to stack overflow,
        There I found that some stylesheets as the googles one finds functionallity almost identical, but 
        when dealing with some cases of null values. Therefore, it comes more as stylish and could be better 
        to use pointers due explicitely. 

        stack overflow: https://stackoverflow.com/questions/7058339/when-to-use-references-vs-pointers
        Google style guide: https://google.github.io/styleguide/cppguide.html
    */

    return 0;
}
