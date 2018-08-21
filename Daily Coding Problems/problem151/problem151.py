from sys import argv
from matrix import create_str_matrix

def bucket(matrix, coordinate, color):
	i = coordinate[0]
	j = coordinate[1]

	old_color = matrix[i][j]
	matrix[i][j] = color

	neighbors = [
		(i+1,j),
		(i-1, j),
		(i, j+1),
		(i, j-1)
	]

	n = len(matrix)
	m = len(matrix[0])

	neighbors = filter(lambda x: 0 <= x[0] < n and 0 <= x[1] < m, neighbors)

	for x,y in neighbors:
		if matrix[x][y] == old_color:
			bucket(matrix, (x, y), color)

def main():
	if len(argv) < 4:
		print('Error : not enough arguments')
		return

	try:
		filename = argv[1]
		coordinate = argv[2]
		color = argv[3]

		import pdb; pdb.set_trace()
		# Initialize string matrix
		m = create_str_matrix(filename)

		# get an ordered pair for the coordinates
		coordinate = coordinate.split(',')
		x = int(coordinate[0])
		y = int(coordinate[1])
		coordinate = (x, y)

		# Print the original matrix
		print('Before:')
		for l in m:
			print(l)

		bucket(m, coordinate, color)

		print('After:')
		for l in m:
			print(l)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()