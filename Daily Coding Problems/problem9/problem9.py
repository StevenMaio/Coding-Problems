from sys import argv

def largest_nonconsec(arr):
	memo = []

	for i in arr:
		memo.append(None)
	
	memo[0] = arr[0]

	# This is a divide and conquer algorithm
	for i in range(1, len(arr)):
		if i == 1:
			memo[i] = max(arr[i], memo[i-1])

		else:
			memo[i] = max(arr[i] + memo[i-2], memo[i-1])

	return memo[len(arr)-1]

def main():
	array = []

	for arg in argv[1:]:
		array.append(int(arg))

	solution = largest_nonconsec(array)
	
	print('{}'.format(solution))

if __name__ == '__main__':
	main()
