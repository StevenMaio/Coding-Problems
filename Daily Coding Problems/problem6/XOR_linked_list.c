#include <stdlib.h>
#include <stdio.h>

typedef struct xor_linked_list {
    int value;
    struct xor_linked_list *both;
};

void add_helper(struct xor_linked_list *node, struct xor_linked_list *reference,
    int value)
{
    unsigned long both, ref, ptr;
    both = (unsigned long) node->both;
    ref = (unsigned long) reference;

    ptr = both ^ ref;
    // if (both XOR reference == prev) is NULL, then we're at the end
    if (!ptr) {
        // Create new node
        struct xor_linked_list *new_node = 
            (struct linked_list*) malloc(sizeof(struct xor_linked_list));

        new_node->value = value;
        new_node->both = node;

        // TODO: Set both of new_node to node, set both of node to reference ^ &new_node
        ptr = (unsigned long) new_node ^ both;
        node->both = (struct xor_linked_list*) ptr;
    }
    else
    {
        // Cast ptr to a pointer to xor_linked_list and then call the helper
        struct xor_linked_list *next = (struct xor_linked_list*) ptr;
        add_helper(next, node, value);
    }
}

void insert(struct xor_linked_list *head, int value) {
    add_helper(head, 0, value);
}

int get_helper(struct xor_linked_list *node, struct xor_linked_list *reference, 
    int index) 
{
    if (index == 0) 
    {
            return node->value;
    }

    // Else
    unsigned long next_int =
        (unsigned long) reference ^ (unsigned long) node->both;
    struct xor_linked_list *next = (struct xor_linked_list*) next_int;
    return get_helper(next, node, index - 1);
}

int get(struct xor_linked_list *head, int index) {
    return get_helper(head, 0, index);
}

// Lazy driver program
int main(void)
{
    struct xor_linked_list *head;
    int length, i, data;

    length = 10;

    head = (struct xor_linked_list*) malloc(sizeof(struct xor_linked_list));
    head->value = 0;
    head->both = NULL;

    for (i = 1; i < length; i ++) {
        insert(head, i);
    }

    for (i = 0; i < length; i++) {
        int data = get(head, i);
        printf("%d\n", data);
    }

    return 0;
}