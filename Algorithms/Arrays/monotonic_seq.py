from sys import argv

def is_inc_helper(arr, start, end):
	# If the arr is only of length 1, then yes
	if start == end:
		return (True, arr[start], arr[start])

	# If it has two elements, determine if they're ordered
	elif start == end + 1:
		if arr[start] > arr[end]:
			return (False, None, None)
		else:
			return (True, arr[start], arr[end])

	# Split the array in two and determine if either or the subarrays are
	# montonic
	mid = int( (start+end)/2 )
	left = is_inc_helper(arr, start, mid)
	right = is_inc_helper(arr, mid + 1, end)

	if not left[0] or not left[1]:
		return (False, None, None)

	# If the left half's max is greater than the right half's min, then they
	# will not form an increasing sequence
	if left[2] > right[1]:
		return (False, None, None)

	return (True, left[1], right[2])

# I think this can be handled with a divide and conquer method
# Divid 
def is_inc(arr):
	return is_inc_helper(arr,  0, len(arr) - 1)[0]

def main():
	arr = []

	for x in argv[1:]:
		arr.append(int(x))

	solution = is_inc(arr)
	print(solution)

if __name__  == '__main__':
	main()
