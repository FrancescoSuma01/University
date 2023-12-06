// Define the maximum dimension of the stack
#define MAXDIM 10

// Define the structure for the stack
struct stack_node{
	int item;
	struct stack_node* next;
};

// Define a pointer to the stack_node structure
typedef struct stack_node* stack;

// Function prototypes
void init(stack p);
int push(stack p, int i);
int pop(stack p, int* i);
int size(stack p);
int is_empty(stack p);