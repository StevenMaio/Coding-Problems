#include <stdio.h>
#include <stdlib.h>

typedef struct nd {
	char *value;
	struct nd *next;
} node;

void reverse_helper(node *head, node*next)
{
	if (head == NULL)
		return;

	reverse_helper(head->next, head);
	
	head->next = next;
}

node *reverse(node* head)
{
	// Advanced tail to the actual tail
	node* tail = head;
	while (tail->next)
		tail = tail->next;
	
	reverse_helper(head, NULL);

	return tail;
}

int main(int argc, char **argv)
{
	// Create a linked list from argv
	int i;
	node *head, *cursor, *temp, *tail;

	// Initialize the head node
	head = (node*) malloc(sizeof(node));
	head->value = *(argv + 1);
	head->next = NULL;

	cursor = head;

	for (i = 2; i < argc; i++)
	{
		temp = (node*) malloc(sizeof(node));
		temp->value = *(argv + i);
		temp->next = NULL;

		cursor->next = temp;
		cursor = temp;
	}

	cursor = head;
	while (cursor)
	{
		printf("%s ", cursor->value);
		cursor = cursor->next;
	}
	printf("\n");

	// Reverse the linked list
	tail = reverse(head);
	cursor = tail;
	while (cursor)
	{
		printf("%s ", cursor->value);
		cursor = cursor->next;
	}
	printf("\n");


	return 0;
}
