from sys import argv
import pdb

def create_matrix(filename):
	matrix_file = open(filename, "r")
	matrix = []

	content = matrix_file.read()
	content = content.split('\n')

	for elem in content:
		elem = elem.split()
		row = []

		for x in elem:
			row.append(int(x))

		if row:
			matrix.append(row)

	# Close the file
	matrix_file.close()
	return matrix

def get_cand(i, j, m, n):
	cand = []

	if 0 < i:
		cand.append((i-1, j))

		if 0 < j:
			cand.append((i-1, j-1))

		if j < n-1:
			cand.append((i-1, j+1))

	if 0 < j:
		cand.append((i, j-1))

	return cand

def count_islands(matrix):
	index = 0

	# create a matrix to hold the isl_i of m
	isl_i = []

	m = len(matrix)
	n = len(matrix[0])

	for i in range(m):
		row = []
		isl_i.append(row)

		for j in range(n):

			# Preemptively append a -1 (not part of island)
			row.append(-1)

			# If (i, j) is land
			if matrix[i][j]:
				cand = get_cand(i, j, m, n)

				for p in cand:
					x = p[0]
					y = p[1]
					e = isl_i[x][y]

					if e >= 0 and e != row[j] and row[j] == -1:
						row[j] = e

					elif e >= 0 and e != row[j]:
						index -= 1

					# Handle the case of two of them being different


				if row[j] == -1:
					row[j] = index
					index += 1

	return index


def main():
	if len(argv) != 2:
		print('Error : program requires only filename argument')
		return

	filename = argv[1]
	m = create_matrix(filename)

	sol = count_islands(m)
	print(sol)

if __name__ == '__main__':
	main()