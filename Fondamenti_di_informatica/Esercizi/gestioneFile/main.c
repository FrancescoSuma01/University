#include <stdio.h>

//conta il numero di righe interno ad un file di testo
int main(int argc, char const *argv[]) {

    FILE *fp;
    char buf[1024];
    int count = 0;
    
    if(argc != 2){
        printf("Please specify the input filename\n");
        return 1;
    }

    fp = fopen(argv[1], "r");

    if (!fp){
        printf("File not found: %s\n", argv[1]);
        return 2;
    }

    while (!feof(fp)) {
        fgets(buf, 1023, fp);
        count++;
    }

    fseek(fp, 0, SEEK_SET);

    while (!feof(fp)) {
        fgets(buf, 1023, fp);
        printf(buf);
    }

    printf("/n");

    fclose(fp);
    printf("Numero di righe all'interno del file: %d\n", count);

    return 0;
}