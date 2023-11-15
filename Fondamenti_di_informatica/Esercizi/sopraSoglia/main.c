#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef float rilevazioni[25];

int main(int argc, char const *argv[]) {

    unsigned int seed = time(NULL);
    srand(seed);

    rilevazioni r; //variabile di tipo rilevazioni
    int cnt; //conta il numero dei valori maggiori
    float soglia = rand()%25; //la soglia che i valori non devono superare

    for (size_t i = 0; i < 25; i++) {
        
        r[i] = ((float)rand() / (float)RAND_MAX)*45-5; //genera valori reali tra 5 e 50

    }

    printf("La soglia e: %f\n", soglia);

    printf("-----------------------------------------------\n");

    for (size_t i = 0; i < 25; i++) {
        
        printf("%d: %f \n", i, r[i]);

    }

    printf("-----------------------------------------------\n");
    
    for (size_t i = 0; i < 25; i++) {
        
        if (r[i]>soglia) {
            
            cnt++;
            printf("%d: %f \n", i, r[i]);

        }

    }

    printf("Sono presenti %d valori sopra la soglia", cnt);

    return 0;
}
