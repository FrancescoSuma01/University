#include <stddef.h>
#include "stack.h"

// Initialize the stack
void init(stack *pila){
	*pila = NULL;
	return;
}

// Push an item onto the stack
int push (stack* pila, int i) {
	stack n;
	n = malloc(sizeof(struct stack_node));
	if (!n) return 1;//verifica che n sia 0
	n->item = i;
	n->next = *pila;
	*pila = n;
	return 0;
}

// Pop an item from the stack
int pop (stack* pila, int* i) {
	stack n;
	if (!pila) return 1;
	n = *pila;
	*i = n->item;
	*pila = n->next;
	free (n);
	return 0;
}

// Check if the stack is empty
int is_empty(struct stack* pila){
	return !pila;
}