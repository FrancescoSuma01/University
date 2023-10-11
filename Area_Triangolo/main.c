#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int, char**){
    
/*  
    float base = 0;
    float altezza = 0;

    printf("Inserisci la dimensione della base: ");
    scanf("%f", &base);

    printf("Inserisci la dimensione dell'altezza: ");
    scanf("%f", &altezza);
    
    float area = (base * altezza) / 2.0;

    printf("L'area del triangolo di base %.2f e altezza %.2f è: %.2f\n", base, altezza, area);

    printf("-----------------------------------------------"); 
*/

    //il seed viene preso dall'orario per selezionare una tabella pseudo-casuale
    unsigned int seed = time(NULL);
    srand(seed);

    float base = rand()%100+1;
    float altezza = rand()%100+1;

    printf("La dimensione della base e: %f\n", base);

    printf("La dimensione della base e: %f\n", altezza);
    
    float area = (base * altezza) / 2.0;

    printf("L'area del triangolo è: %f\n", area);

    return 0;

}