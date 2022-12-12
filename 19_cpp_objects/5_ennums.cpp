#include <iostream>
using namespace std;

int main(){
    enum days_week {monday, tuesday, wednesday, thursday, friday, saturday, sunday};

    days_week my_day = monday;
    days_week my_other_day = saturday;

    cout << "my day:       " << my_day << endl;
    cout << "my other day: " << my_other_day << endl;




    enum fruits {apple = 3, banana = 5, orange = 1};

    fruits basket = apple;
    fruits another_basket = banana;

    cout << "basket:         " << basket << endl;
    cout << "another_basket: " << another_basket << endl;
}