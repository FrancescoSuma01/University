#include "stack.h"

// Initialize the stack
void init(stack p) {
    p->head = 0;
    return;
}

// Push an item onto the stack
int push(stack p, int item) {
    if (p->head == MAXDIM)
        return 1; // Stack is full
    p->stack_array[p->head] = item;
    p->head++;
    return 0; // Successfully pushed
}

// Pop an item from the stack
int pop(stack p, int* item) {
    if (p->head == 0)
        return 1; // Stack is empty
    p->head--;
    *item = p->stack_array[p->head];
    return 0; // Successfully popped
}

// Get the size of the stack
int size(stack p) {
    return p->head;
}

// Check if the stack is empty
int is_empty(stack p) {
    return !(p->head);
}
