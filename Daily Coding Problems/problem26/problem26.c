#include <stdlib.h>

struct linked_list {
	int value;
	struct linked_list *next;
};

/*
 * Removes the kth element from a linked list and returns a poitner to 
 * the head of the new linked list.
 */
struct linked_list * remove_kth_element(struct linked_list *head, int k)
{
	struct linked_list *new_head, *cursor, *to_be_deleted;

	// If k is 0, then remove the head from the list, and then return the 
	// pointer the head->next
	if (k == 0)
	{
		new_head = new_head -> next;
		free(head);
		return new_head;
	}

	while (k > 1)
	{
		cursor = cursor->next;
	}

	to_be_deleted = cursor->next;
	cursor->next = to_be_deleted->next;
	free(to_be_deleted);

	return new_head;
}
