#include <stdio.h>

int fattoriale(int n);

int main(int argc, char const *argv[]) {
    
    int numero;

    printf("Inserisci il numero di cui fare il fattoriale: ");
    scanf("%d", &numero);

    int risultato = fattoriale(numero);

    printf("Il fattoriale di %d e: %d", numero, risultato);

    return 0;
}

int fattoriale(int n) {

    if(n == 0) {

        return 1;
    
    }

    int prodotto = n * fattoriale(n-1);

    return prodotto;

}