from sys import argv

def long_inc_sub(arr):
	# Check to see if the arr is not increasing
	if not arr:
		return None

	memo = [1]
	length = len(arr)

	# Find the longest inc subsequence up to the ith element
	for i in range(1, length):
		a = arr[i]
		y = 1

		for j in range(i):
			# SKip the loop of i < j
			if a < arr[j]:
				continue

			z = memo[j] + 1

			# set y to the max of all sequences including arr[i]
			if z > y:
				y = z

		memo.append(y)

	return max(memo)

def main():
	arr = []

	for arg in argv[1:]:
		arr.append(int(arg))

	solution = long_inc_sub(arr)
	print(solution)

if __name__ == '__main__':
	main()
