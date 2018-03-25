struct xor_linked_list {
    int value;
    struct xor_linked_list *both;
};

void add_helper(struct xor_linked_list *node, struct xor_linked_list *reference,
    int value)
{
    // if (both XOR reference == prev) is NULL, then we're at the end
    if ((node->both ^ reference) == 0) {
        // TODO: Create new node
        struct xor_linked_list new_node = {value, node};

        // TODO: Set both of new_node to node, set both of node to reference ^ &new_node
        node->both = node->both ^ &new_node;
    }
    else
    {
        // struct xor_linked_list *next = (struct xor_linked_list *) ((long) node->both) ^ ((long) reference);
        struct xor_linked_list *next = node->both ^ reference;
        // add_helper(node->both ^ reference, node, value);
        add_helper(next, node, value);
    }
}

void add(struct xor_linked_list head, int value) {
    add_helper(&head, 0, value);
}

int get_helper(struct xor_linked_list *node, struct xor_linked_list *reference, 
    int index) 
{
    if (index == 0) 
    {
            return node->value;
    }

    // Else
    return get_helper(node->both ^ reference, node, index - 1);
}

int get(struct xor_linked_list head, int index) {
    return get_helper(&head, 0, index);
}