#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef int numeri[10];

int main(int argc, char const *argv[]) {

    unsigned int seed = time(NULL);
    srand(seed);

    numeri partenza;
    numeri arrivo;
    
    int somma = 0;

    printf("Insieme di partenza: \n");

    for (size_t i = 0; i < 10; i++) {
        
        partenza[i] = rand()%201-100;

        printf("%d: %d \n", i, partenza[i]);

    }

    printf("------------------------------------------------\n");

    printf("Insieme di arrivo: \n");

    for (size_t i = 0; i < 10; i++) {
        
        somma = somma + partenza[i];

        arrivo[i] = somma;

        printf("%d: %d \n", i, arrivo[i]);

    }
    
    return 0;
}
