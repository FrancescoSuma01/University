#include <stdio.h>
#include <string.h>
#include <ctype.h>

//convertire la lettera iniziale di ogni parola in una lettera maiuscola
int main(int argc, char const *argv[]) {
    
    char frase[128]; // ci saranno al massimo 127 valori
    char *s = "Inserisci una frase da convertire\n";
    char *delim = " ";
    char *token;

    printf(s);

    //gets(frase);
    fgets(frase, sizeof(frase), stdin);
    int len = strlen(frase);
    printf("\n");

    //il delimitatore sarà lo spazio
    for(token = strtok(frase, delim); token!=NULL; token = strtok(NULL, delim)){
        token[0] = toupper(token[0]);
        printf("Token corrente: %s\n\n", token);

        int len = strlen(token);

        if(token != frase){
            token[-1] = ' ';
        }
        
    }
    
    frase[len] = '\0';


    printf(frase);

    return 0;
}