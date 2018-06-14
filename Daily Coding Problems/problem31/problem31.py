from sys import argv

def edit_distance(x, y):
	# Initialize a matrix
	memo = []

	for i in range(len(y) + 1):
		row = [0]

		for j in range(len(x)+1):
			row.append(0)

		memo.append(row)

	for j in range(1, len(y) + 1):
		for i in range(1, len(x) + 1):
			diff = 1

			if x[i-1] == y[j-1]:
				diff = 0
		
			memo[j][i] = min(
				1 + memo[j-1][i],
				1 + memo[j][i-1],
				diff + memo[j-1][i-1])

	return memo[len(y)][len(x)]

	# Now iterate through the array
	return memo

def main():
	x = argv[1]
	y = argv[2]

	solution = edit_distance(x, y)
	print(solution)
#	print('{}\n{}'.format(x,y))

if __name__ == '__main__':
	main()
