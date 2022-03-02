#include <stdio.h>

enum deck {
    club = 0,
    diamonds = 1,
    hearts = 2,
    spades = 3,
} card;

int main(){

    card = spades;
    printf("\nCard value: %d \n", card);
    printf("Size: %d", sizeof(card));
    return 0;
}