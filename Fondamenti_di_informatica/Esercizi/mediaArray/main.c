#include <stdio.h>

typedef int numeri[10];

int media(int a, numeri num);

int main(int argc, char const *argv[])
{
    numeri num = {10, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    int a = 0;

    a = media(a, num);

    printf("La media dei numeri è: %d\n", a);

    return 0;
}

int media(int a, numeri num) {

    int somma = 0;

    for (int i = 0; i < 10; i++) {
        somma = somma + num[i];
    }

    a = somma / 10;

    return a;
}
