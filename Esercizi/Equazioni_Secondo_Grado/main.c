#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

void maggiore(float a, float b, float c){

    float delta = (pow(b, 2) - 4 * a * c);

    printf("delta = %.2f\n", delta);

    printf("\n----------------------------------------------\n");

    if (delta < 0) {
        
        printf("La soluzione non è un numero Reale");

    }else{
        
        float x1 = ( -(b) - sqrt(delta))/(2.0 * a);
        float x2 = ( -(b) + sqrt(delta))/(2.0 * a);

        printf("\n------Result------");
        printf("\n------------------\n\n");

        if (x1==-0.0 || x2==-0.0) {

            printf("x1 = 0.0\n");
            printf("x2 = 0.0");
        
        }else{
        
            printf("x1 = %.2f\n", x1);
            printf("x2 = %.2f\n", x2);
        
        }
        
    }

}

void minore(float b, float c){

    float x = -c/b;

    printf("\n------Result------");
    printf("\n------------------\n\n");

    printf("x = %.2f\n", x);
}


int main(int, char**){

    printf("\n------Solution to second degree equations------");
    printf("\n-----------------------------------------------\n\n");

    float a = 0.0; 
    float b = 0.0;
    float c = 0.0;

    printf("Inserisci il valore di a: ");
    scanf("%f", &a);

    printf("Inserisci il valore di b: ");
    scanf("%f", &b);

    printf("Inserisci il valore di c: ");
    scanf("%f", &c);

    printf("\n");

    printf("a = %.2f\n", a);
    printf("b = %.2f\n", b);
    printf("c = %.2f\n", c);

    if (a==0) {
        
        if (b==0 && c==0){

            printf("L'equazione è indeterminata: infinite soluzioni\n");

        }else if (b==0){
            
            printf("L'equazione è impossibile: nessuna soluzione\n");

        }else {
            
            minore(b, c);

        }

    }else{

        maggiore(a, b, c);        
    
    }
    
    return 0;

}
