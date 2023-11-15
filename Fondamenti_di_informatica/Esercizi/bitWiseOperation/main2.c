#include <stdio.h>

int main(int argc, char const *argv[]) {

    float f = 1.0;
    
    void* p; //è una variabile puntatore che non specifica il tipo della variabile puntata
    
    p = &f;

    int n = *(int *)p;//vado a fare il casting sul tipo contenuto in p

    //effettuando queste operazioni non ci sono shift sui bit, viene inizialmente effettuato il cast e successivamente effettua le operazioni puntatori

    int c;

    for (int i = 0; i < 32; i++) {
        
        c = n & 1;

        printf("%d", c); //%u permette di rappresentare numeri unsigned

        n = n>>1;

    }
    

    return 0;
}