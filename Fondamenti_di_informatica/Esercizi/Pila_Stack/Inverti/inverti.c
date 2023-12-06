#include <stdio.h>
#include "stack.h"

int main() {
    struct stack_node pila;
    int num;

    // Inizializzazione della pila
    init(&pila);

    for (int i = 0; i < 10; i++) {
        printf("Inserisci un numero: ");
        scanf("%d", &num);
        push(&pila, num);
    }

    printf("\n- - - Stampa della pila prima dell'inversione - - -\n");

    // alloca dinamicamente una nuova pila della stessa dimensione della pila originale dove effettua la copia di questa
    stack temp_pila = malloc(sizeof(struct stack_node));
    init(temp_pila); //Inizializzazione della nuova pila

    while (!is_empty(&pila)) { //verifica che la pila originale non sia vuota
        if (pop(&pila, &num) == 0) { //estrae dalla pila originale i valori e verifica che ci sia 0 di ritorno affinche sia andato tutto correttamente
            push(temp_pila, num); //inserisce nella pila temporanea il valore estratto dalla pila originale
            printf("%d ", num);
        } else {
            printf("La pila è vuota.\n"); //si occupa di capire se qualcosa è andato storto
            break;
        }
    }

    printf("\n\n- - - Stampa della pila dopo l'inversione - - -\n");

    // Stampa gli elementi della pila invertita
    while (!is_empty(temp_pila)) {
        if (pop(temp_pila, &num) == 0) {
            printf("%d ", num); //stampa l'elemento estratto
        } else {
            printf("La pila temporanea è vuota.\n");
            break;
        }
    }

    // Libera la memoria allocata per la pila temporanea
    free(temp_pila);

    return 0;
}
