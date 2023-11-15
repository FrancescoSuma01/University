#include <stdio.h>

typedef struct{
    float x;
    float y;
}point;


int main(int argc, char const *argv[]) {

    point p1; //Definisco una variabile p1 di tipo point

    p1.x = 15.3;
    p1.y = 2.7;

    point p2;

    p2 = p1; //questo punto coinciderà con p1 nel piano cartesiano

    return 0;

}