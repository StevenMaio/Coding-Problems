from sys import argv
from pdb import set_trace

def spiral_helper(**kwargs):
	matrix = kwargs['matrix']
	row = kwargs['row']
	col = kwargs['col']
	num_rows = kwargs['num_rows']
	num_cols = kwargs['num_cols']

	# Exit if num_rows and num_cols are 0
	if num_rows <= 0 or num_cols <= 0:
		return

	# Print the top row
	for i in range(num_cols - 1):
		print(matrix[row][col+i])

	# print the right column
	col_p = col + num_cols - 1
	for j in range(num_rows - 1):
		print(matrix[row+j][col_p])

	# Print the bottom row
	row_p = row + num_rows - 1
	for i in range(1, num_cols)[::-1]:
		print(matrix[row_p][col+i])

	for j in range(1, num_rows)[::-1]:
		print(matrix[row+j][col])
	
	# Recursively call spiral helper again
	row += 1
	col += 1
	num_rows -= 2
	num_cols -= 2

	spiral_helper(
		matrix= matrix,
		row = row,
		col = col,
		num_rows = num_rows,
		num_cols = num_cols)

def print_spiral(matrix):
	spiral_helper(
		matrix=matrix,
		row=0,
		col=0,
		num_rows=len(matrix),
		num_cols=len(matrix[0]))

def main():

	matrix = [
		[ 1,  2,  3,  4,  5],
		[ 6,  7,  8,  9, 10],
		[11, 12, 13, 14, 15],
		[16, 17, 18, 19, 20]
		]

	print_spiral(matrix)

if __name__ == '__main__':
	main()
