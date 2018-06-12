from sys import argv
import pdb

def subset_sum(arr, upper_bound):
	# Initialize the memo matrix
	memo = []

	for i in range(len(arr)+1):
		row = []
		
		for w in range(upper_bound + 1):
			row.append(0)

		memo.append(row)

	# Calculate the subset sum
	for i in range(1, len(arr) + 1):
		for w in range(upper_bound + 1):
			# Handle case where 
			if arr[i-1] > w:
				memo[i][w] = memo[i-1][w]

			else:
				entry = max(memo[i-1][w], arr[i-1] + memo[i-1][w - arr[i-1]])
				memo[i][w] = entry

	return memo[-1][-1]

def main():
	if len(argv) != 3:
		print('Error: invalid arguments')
		return

	# Initialize the array and get the upperbound
	arr = []
	upper_bound = int(argv[1])

	weights = argv[2].split(',')

	for x in weights:
		arr.append(int(x))


	arr.sort()
	solution = subset_sum(arr, upper_bound)
	print(upper_bound)
	print(arr)
	print(solution)

if __name__ == '__main__':
	main()
