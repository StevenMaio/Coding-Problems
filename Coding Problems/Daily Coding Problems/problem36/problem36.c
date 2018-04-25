typedef struct tree_node {
	int value;
	struct tree_node *left;
	struct tree_node *rght;
} node;

int second_largest(node *root) {
	// Return NULL if the root is NULL
	if (!root)
		return NULL;

	while ((root->right)->right != NULL)
		root = root->right;

	return root->value;
}
