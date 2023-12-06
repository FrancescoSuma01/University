#include <stdio.h>

void scambia(int* x, int* y);

int main(){
	int a, b;
	a = 15;
	b = 7;
	scambia(&a, &b);

    printf("A: %d",a);
    printf("B: %d",b);


	return 0;
}

void scambia(int* x, int* y){
	int t;
	t = *x;
	*x = *((int*)y);
    *y = t;
}