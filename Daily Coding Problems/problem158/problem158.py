from sys import argv
from matrix import create_int_matrix

def count_paths(matr):
	def helper(i, j):
		# If we've made it to the bottom left, then we're done
		if i == n-1 and j == m-1:
			return 1

		# Determine if we can move to the right
		paths = 0
		if j < m-1 and matr[i][j+1] == 0:
			paths += helper(i, j+1)

		if i < n-1 and matr[i+1][j] == 0:
			paths += helper(i+1, j)

		return paths

		

	# Get the dimensions of m
	n = len(matr)
	m = len(matr[0])

	return helper(0, 0)

def main():
	if len(argv) < 2:
		print("Error : not enough arguments")
		return

	try:
		filename = argv[1]
		m = create_int_matrix(filename)
		print(m)

		sol = count_paths(m)
		print(sol)

	except:
		print('Error : invalid argumentss')

if __name__ == '__main__':
	main()