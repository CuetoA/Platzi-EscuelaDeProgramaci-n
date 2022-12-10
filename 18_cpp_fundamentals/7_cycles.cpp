#include <iostream>
using namespace std;


int main(){

    int mylst[] = {1,2,3,10,20,30,100,200,300};
    const int elem_size = sizeof( mylst[0] );
    const int list_size = sizeof(mylst) / elem_size;
    
    for(int i=0; i < list_size; i++ ){
        cout << mylst[i] << endl;
    }



    int number = 0;
    int target = 1000;
    int counter = -1;
    
    while( number != target ){    
        counter++;        
        if( counter > list_size - 1){break;}

        number = mylst[counter];
        cout << "My number is: " << number << endl;
    }

}