#include <stdio.h>
#include <stdlib.h>

typedef struct bn {
	struct bn *node1, *node2;
	int data;
} bi_node;

void print_tree(bi_node *root)
{
	if (root == NULL)
	{
		return;
	}

	printf("%d ", root->data);
	print_tree(root->node1);
	print_tree(root->node2);
}

void print_list(bi_node *head)
{
	if (head == NULL)
	{
		return;
	}

	printf("%d ", head->data);
	print_list(head->node2);
}

void add_node(bi_node *root, int data)
{
	// Exit if root is null
	if (root == NULL)
		return;

	if (root->data >= data)
	{
		if (root->node1 == NULL)
		{
			// Initialize new node
			bi_node *node = (bi_node*) malloc(sizeof(bi_node));
			root->node1 = node;
			node->data = data;
			node->node1 = NULL;
			node->node2 = NULL;
		} 
		
		else
		{
			// Recursively call this on the child
			add_node(root->node1, data);
		}
	}

	else
	{
		if (root->node2 == NULL)
		{
			// Initialize the right child
			bi_node *node = (bi_node*) malloc(sizeof(bi_node));
			root->node2 = node;
			node->data = data;
			node->node1 = NULL;
			node->node2 = NULL;
		} 
		
		else
		{
			// Recursively call this on the right child
			add_node(root->node2, data);
		}
	}
}

bi_node **to_linked_list(bi_node *root)
{
	// Return null if root is null
	if (root == NULL)
		return NULL;

	bi_node **left, **right, **return_val;
	bi_node *start, *end;

	left = to_linked_list(root->node1);
	right = to_linked_list(root->node2);

	// Handle if the left list is null
	if (left == NULL)
	{
		start = root;
	} 
	else {
		start = *left;
		root->node1 = *(left + 1);
		(*(left + 1))->node2 = root;
		free(left);
	}

	// Handle if the right list is null
	if (right == NULL)
	{
		end = root;	
	} 
	else
	{
		end = *(right+1);
		root->node2 = *(right);
		(*(right))->node1 = root;
		free(right);
	}

	return_val = (bi_node**) malloc(sizeof(bi_node*) * 2);
	*return_val = start;
	*(return_val + 1) = end;

	return return_val;
}

int main(int argc, char **argv)
{
	if (argc < 2)
	{
		printf("Not enough arguments\n");
		return 0;
	}

	char **cursor = argv + 1;
	int data = atoi(*cursor);
	bi_node *root, **ret;

	root = (bi_node*) malloc(sizeof(bi_node));
	root->data = data;
	root->node1 = NULL;
	root->node2 = NULL;

	// Advance the cursor
	cursor++;

	while (*cursor)
	{
		data = atoi(*cursor);
		add_node(root, data);
		cursor++;
	}

	print_tree(root);
	printf("\n");

	ret = to_linked_list(root);
	root = *(ret);
	free(ret);

	print_list(root);
	printf("\n");
}
