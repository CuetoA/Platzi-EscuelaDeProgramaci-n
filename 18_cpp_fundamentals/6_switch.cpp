#include <iostream>
using namespace std;

int main(){
    int user = 0;
    const int user1 = 700;
    const int user2 = 800;
    const int user3 = 900;

    cout << "Type yout user number: ";
    cin >> user;
    cout << endl;

    switch (user){
        case user1:
            cout << "Welcome Andrés user 700" << endl;
            break;
        case user2:
            cout << "Welcome Scarlette user 800" << endl;
            break;
        case user3:
            cout << "Welcome Boni user 900" << endl;
            break;
        default:
            cout << "No user found" << endl;
            break;
    }

}