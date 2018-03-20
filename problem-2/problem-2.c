#include <stdio.h>
#include <stdlib.h>

int* get_productless_array(int *array, int size)
{
	int i, j, product;
	int *product_arr = (int *) malloc(sizeof(int) * size);

	// Iterate over each item in the array and set it equal to the product
	// of all elements of the array not equal to it
	for (i = 0; i < size; i++)
	{
		// Initialize product to 1
		product = 1;

		for (j = 0; j < size; j++)
		{
			// Skip the current index if it's equal to i
			if (j == i)
				continue;

			// multiply this into the 
			product *= *(array + j);
		}

		*(product_arr + i) = product;
	}

	return product_arr;
}

int main(int argc, char** argv)
{
	// TODO: Have it select an array from inputs
	int *arr, *input, count, i, temp;

	printf("Enter number of entries in the array: ");
	scanf("%d", &count);

	// Initialize array for input
	input = (int *)malloc(sizeof(int) * count);

	// Ask the user for entries in the array
	for (i = 0; i < count; i++)
	{
		printf("Enter an entry (make sure it's relatively prime): ");
		scanf("%d", input + i);
	}

	arr = get_productless_array(input, count);

	for (i = 0; i < count; i++)
	{
		printf("%d ", *(arr + i));
	}

	// Free input and arr
	free(input);
	free(arr);

	return 0;
}
