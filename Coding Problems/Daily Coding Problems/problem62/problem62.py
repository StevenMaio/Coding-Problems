from sys import argv

def num_paths(m, n):
	matrix = []

	for i in range(m):
		row = []

		for j in range(n):
			row.append(0)

		matrix.append(row)

	# Set the last coordinate to 1
	matrix[-1][-1] = 1

	for i in range(m)[::-1]:

		for j in range(n)[::-1]:
			if i != m-1:
				matrix[i][j] = matrix[i+1][j] + matrix[i][j]

			if j != n-1:
				matrix[i][j] = matrix[i][j+1] + matrix[i][j]

	return matrix[0][0]

def main():
	m = int(argv[1])
	n = int(argv[2])

	solution = num_paths(m, n)
	print('{}'.format(solution))

if __name__ == '__main__':
	main()
