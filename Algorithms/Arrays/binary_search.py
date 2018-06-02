from sys import argv
from array_util import parse_file
from merge_sort import merge_sort

def bin_search_helper(arr, value, start, end):
	# Determine if start and end are the same
	if start == end:
		if arr[start] == value:
			return start
		else:
			return None

	mid = int((start + end)/2)

	# If the midpoint is our key, then return the index
	if arr[mid] == value:
		return mid

	# If our value is greater than our mipdoint, check the second half
	elif arr[mid] < value:
		return bin_search_helper(arr, value, mid + 1, end)

	# Check the first half of the array
	else:
		return bin_search_helper(arr, value, start, mid - 1)

def bin_search(arr, value):
	start = 0
	end = len(arr) - 1

#	arr = merge_sort(arr)
	return bin_search_helper(arr, value, start, end)

def main():
	filename = argv[1]
	value = int(argv[2])

	arr = parse_file(filename)
	arr = merge_sort(arr)
	solution = bin_search(arr, value)

	print(solution)
	print(arr)

if __name__ == '__main__':
	main()
