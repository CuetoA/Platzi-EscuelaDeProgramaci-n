#include <iostream>
using namespace std;

int main(){

    const char my_chr1 = 'l';
    char   my_chr2     = 'a';
    char   my_str2[]   = "Hola";
    char   my_str1[]   = {'H', 'o', my_chr1, my_chr2};
    string my_str3     = "Hola";

    cout << "Alanysis of MY_STR1 : " << my_str1 << endl;
    cout << "   MY_STR1 starts in memory address: " << &my_str1 << endl;
    cout << "   MY_STR1[0] in memory address:     " << (int *) &my_str1[0] << endl;
    cout << "   MY_STR1[1] in memory address:     " << (int *) &my_str1[1] << endl;
    cout << "   MY_STR1[2] in memory address:     " << (int *) &my_str1[2] << endl;
    cout << "   MY_STR1[3] in memory address:     " << (int *) &my_str1[3] << endl;
    cout << "   MY_CHR1 real address in memory:   " << (int *) &my_chr1     << endl;
    cout << "   MY_CHR2 real address in memory:   " << (int *) &my_chr2     << endl;
    cout << endl;

    cout << "Alanysis of MY_STR2 : " << my_str2 << endl;
    cout << "   MY_STR2 starts in memory address: " << &my_str2 << endl;
    cout << "   MY_STR2[0] in memory address:     " << (int *) &my_str2[0] << endl;
    cout << "   MY_STR2[1] in memory address:     " << (int *) &my_str2[1] << endl;
    cout << "   MY_STR2[2] in memory address:     " << (int *) &my_str2[2] << endl;
    cout << "   MY_STR2[3] in memory address:     " << (int *) &my_str2[3] << endl;
    cout << endl;

    cout << "Alanysis of MY_STR3 : " << my_str3 << endl;
    cout << "   MY_STR3 starts in memory address: " << &my_str3 << endl;
    cout << "   MY_STR3[0] in memory address:     " << (int *) &my_str3[0] << endl;
    cout << "   MY_STR3[1] in memory address:     " << (int *) &my_str3[1] << endl;
    cout << "   MY_STR3[2] in memory address:     " << (int *) &my_str3[2] << endl;
    cout << "   MY_STR3[3] in memory address:     " << (int *) &my_str3[3] << endl;
    cout << endl;

    /* 
        By analyzing the creation order of variables and it's memory alocation we can observ 
            1.- The registers creation in memory is secuantially. First to appear first to save
            2.- The decendant order of the variables show us how they are put in the stack.
            3.- When a variable is created a certian amout of memory is given to it by default

    */
}