#include <stdio.h>

typedef enum {green, red, yellow, black, white} color;
//                {}

int main(int argc, char const *argv[]) {
    
    enum color c1; // per differenziare i colori il computer utilizza i bit, in questo caso li serviranno 3 bit

    c1 = red; //red non è testo ma è un simbolo che identifica un valore

    enum color c2;

    c2 = 0; //accetta anche numeri interi poichè al livello logico hanno la stessa rappresentazione

    enum color c3;

    c3 = green + red; // il risultato sarà red

    printf("Il valore c3 e: %d", c3);

    return 0;
}