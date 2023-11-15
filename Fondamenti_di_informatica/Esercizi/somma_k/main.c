#include <stdio.h>
#include <stdlib.h>

//argomenti a linea di comando:
//n: numero di elementi totali nell'insieme 
//k: raggruppamento

int main(int argc, char const *argv[]) {
    
    int n, k;
    int max;

    //3 poichè nella riga di comando argv contiene 3 celle, k, n e nome dell'eseguibile
    if (argc != 3) {

        printf("Numero errato di parametri\n");        
        printf("%s <n> <k>\n", argv[0]); //questa sintassi viene detta usage, spiega come utilizzare l'applicazione
        printf("\t n: numero totale di elementi\n");
        printf("\t k: raggruppamento\n");
        
        return 1; //restituisce al sistema operativo 1, il quale riconoscerà che l'esecuzione non è andata a buon fine

    }
    
    n = strtol(argv[1], NULL, 10); //converte un carattere in long string -> long
    //argomento da convertire, NULL, base di numerazione

    k = strtol(argv[2], NULL, 10);
    
    if (n <= 0 || k<=0) {
        
        printf("Valori degli argomenti errato\n");
        printf("n: %d, k: %d\n", n, k);
        printf("n e k devono essere numeri positivi");

        return 2;

    }
    
    if(n<k){

        printf("n non puo essere minore di k\n");

        return 0;

    }
    
    int v[n];

    //inizializzare v
    for (int i = 0; i < n; i++) {
        v[i] = rand()%100+1;

        printf("%d: %d\n", i, v[i]);
    }

    printf("\n");

    max = -1; //poichè sappiamo che tutti i valori saranno positivi
    
    for (int i = 0; i <= n-k; i++) {

        int somma = 0;

        for (int j = i; j < i+k; j++) {
            
            somma = somma + v[j];
            printf("%d: %d", j, v[j]);
            printf("\n"); 

        }
   
        printf("Somma = %d", somma);
        printf("\n");
        printf("\n"); 

        if(somma > max){
            max = somma;
        }

    }

    printf("Valore max: %d\n", max);

    return 0;
}