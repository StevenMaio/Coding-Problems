/*
 * Given two linked lists which intersect at some point, return the first node
 * where they intersect
 */

struct linked_list {
	int value;
	struct linked_list *next;
}

struct linked_list *find_intersection(struct linked_list *a, 
	struct linked_list *b)
{
	int length_a, length_b;
	struct linked_list *cursor;

	// First, find the length of a
	length_a = 0;
	cursor = a;
	while (!cursor)
	{
		length_a++;
		cursor = cursor->next;	// Advance the cursor
	}

	// Find the length of b
	length_b = 0;
	cursor = b;
	while (!cursor)
	{
		length_b++;
		cursor = cursor->next;	// Advance the cursor
	}

	// Now, offset the two linked lists so that their cursors are the min of
	// length_a, length_b away from their tails -- and keep comparing
	if (length_b < length_a)
	{
		a = a->next;
		length_a--;
	}

	else if (length_a < length_b)
	{
		b = b->next;
		length_b--;
	}

	// Now compare the cursors until we found an intersection point
	while (!a)
	{
		// if a and b are the same, then we've found the first 
		// intersection point
		if (a == b)
			return a;

		a = a->next;
		b = b->next;
	}

	// This shouldn't happen based on the specification of the problem
	return NULL;
}
