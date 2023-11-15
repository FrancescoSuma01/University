#include <stdio.h>

typedef enum {green, red, yellow, black, white} color;


typedef struct{
    float x;
    float y;

    color c;
}point;

typedef point set[3];//sto creando un array di tipo set

int main(int argc, char const *argv[]) {
    
    set s;

    s[0].x = 5.8;
    s[0].y = 5.8;
    s[0].c = red;

    //questo posso anche criverlo in questo modo

    s -> x = 5.8;
    s -> y = 5.8;
    s -> c = red;

    s[1] = s[0];

    // anche in questo caso utilizzo la freccia 

    (s+1) -> x = 3.4;

    return 0;
}