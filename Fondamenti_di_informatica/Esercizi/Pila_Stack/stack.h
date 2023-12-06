// Define the maximum dimension of the stack
#define MAXDIM 100

// Define the structure for the stack
struct _stack {
    int stack_array[MAXDIM];
    int head;
};

// Define a pointer to the stack structure
typedef struct _stack* stack;

// Function prototypes
void init(stack p);
int push(stack p, int i);
int pop(stack p, int* i);
int size(stack p);
int is_empty(stack p);
