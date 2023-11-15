#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[]) {
    
    int intero = 1 << 31; //numero della quale vogliamo sapere i bit
    //equivale a 2^8

    char car = 'a';
    int n;

    printf("n = %d %c\n", car, car);

    int c;

    n = car;

    for (int i = 0; i < 32; i++) {
        
        c = n & 1;

        printf("%d", c); //%u permette di rappresentare numeri unsigned

        n = n>>1;

    }
    

    return 0;
}