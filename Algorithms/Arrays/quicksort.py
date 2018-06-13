from sys import argv
from random import randint

def mergesort(arr):
	if not arr:
		return arr

	rand_int = randint(0, len(arr) - 1)
	pivot = arr[rand_int]
	
	low = [x for x in arr if x < pivot]
	high = [x for x in arr if x > pivot]

	low = mergesort(low)
	high = mergesort(high)

	return low + [pivot] + high

def main():
	arr = []

	for x in argv[1:]:
		arr.append( int(x) )

	arr = mergesort(arr)
	print(arr)

if __name__ == '__main__':
	main()
