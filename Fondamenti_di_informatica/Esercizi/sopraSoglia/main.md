#include <stdio.h>

int main(int argc, char const *argv[]) {
    
    float rilevazioni[25];
    float soglia = -1.0;

    int cont = 0;

    for (size_t i = 0; i < 25; i++) {
        
        if (rilevazioni[i]>soglia) {
            
            cont++;

        }

    }
    
    printf("Sono presenti %d valori sopra la soglia", cont);

    return 0;
}