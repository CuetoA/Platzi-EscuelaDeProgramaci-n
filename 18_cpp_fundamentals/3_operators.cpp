#include <iostream>

using namespace std;

int main() {
    const int a = 2;
    int b = 3;

    cout << a + b << endl;
    cout << "Space of a in bites is: ";
    cout << sizeof(a) << endl;

    int numbers[] = {0, 1, 2, 3, 4, 5, 6};

    cout << "Space of bites in numbers list is: ";
    cout << sizeof(numbers) << endl;

    cout << "Number of elements in numbers list is: ";
    cout << sizeof(numbers) / sizeof(numbers[0]) << endl;
}