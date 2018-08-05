#include <stdlib.h>

typedef struct b_arr {
	int size;
	int *data;
} BitArray;

BitArray * init(int size) {
	int num_integers, *data;
	BitArray *arr;

	num_integers = (int) (size / sizeof(int)) + 1;
	data = (int*) calloc(sizeof(int), num_integers);

	arr = (BitArray*) malloc(sizeof(BitArray));

	return arr;
}

int get(BitArray *arr, int i) {
	// Return -1, if arr is null
	if (!arr) {
		return -1;
	}

	int size, *data, data_index, integer, r;
	size = arr->size;

	// Return If index is an non valid value
	if (i >= size || i < 0) {
		return -1;
	}

	data = arr->data;
	data_index = (int) i / sizeof(int);
	r = i % sizeof(int);

	integer = *(data + data_index);
	return integer & (1 << r);
}

int set(BitArray *arr, int i, int value) {
	// Return -1, if arr is null
	if (!arr) {
		return -1;
	}

	int size, *data, data_index, integer, r, temp;
	size = arr->size;

	// Return If index is an non valid value
	if (i >= size || i < 0) {
		return -1;
	}

	data = arr->data;
	data_index = (int) i / sizeof(int);
	r = i % sizeof(int);
	integer = *(data + data_index);

	if (value) {
		*(data + data_index) |= (1 << r); 
	} else {
		temp = -1;
		temp ^= (1 << r);
		*(data + data_index) &= temp;
	}
}