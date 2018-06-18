from sys import argv
import pdb

def is_sol(queens, n, board):
	if len(queens) == n:
		for q in queens:
			x = q[0]
			y = q[1]

			# If there is only one queen threatening that spot, then we're good
			if board[x][y] != 1:
				return False 
			
		return True

	else:
		return False

def constr_cand(board, n, a):
	x = None
	y = None

	if not a:
		x = 0
		y = 0

	else:
		last_q = a[-1]
		x = last_q[0]
		y = last_q[1]

	candidates = []

	for i in range(x, n):
		for j in range(n):
			if board[i][j] == 0:
				coord = (i, j)
				candidates.append(coord)
			
	return candidates

def make_move(q, board, n):

	# Populate the horizontal
	for i in range(n):
		x_cord = (q[0] + i) % n
		y_cord = q[1]
		board[x_cord][y_cord] += 1 

	# Populate the vertical
	for i in range(n):
		x_cord = q[0]
		y_cord = (q[1] + i) % n
		board[x_cord][y_cord] += 1

	# Top left to bottom right diag
	x_cord = q[0]
	y_cord = q[1]

	# First, shift as far as possible to the top left corner
	while x_cord > 0 and y_cord > 0:
		x_cord -= 1
		y_cord -= 1

	# Now, move as down right as possible
	while x_cord < n and y_cord < n:
		board[x_cord][y_cord] += 1
		x_cord += 1
		y_cord += 1

	# Now handle the bottom left to top right
	x_cord = q[0]
	y_cord = q[1]

	while x_cord < n-1 and y_cord > 0:
		x_cord += 1
		y_cord -= 1

	while x_cord >= 0 and y_cord < n:
		board[x_cord][y_cord] += 1
		x_cord -= 1
		y_cord += 1

	# This is to compensate for adding one 4 times to the queen's piece
	board[q[0]][q[1]] -= 3

def unmake_move(q, board, n):
	# Populate the horizontal
	for i in range(n):
		x_cord = (q[0] + i) % n
		y_cord = q[1]
		board[x_cord][y_cord] -= 1 

	# Populate the vertical
	for i in range(n):
		x_cord = q[0]
		y_cord = (q[1] + i) % n
		board[x_cord][y_cord] -= 1

	# Top left to bottom right diag
	x_cord = q[0]
	y_cord = q[1]

	# First, shift as far as possible to the top left corner
	while x_cord > 0 and y_cord > 0:
		x_cord -= 1
		y_cord -= 1

	# Now, move as down right as possible
	while x_cord < n and y_cord < n:
		board[x_cord][y_cord] -= 1
		x_cord += 1
		y_cord += 1

	# Now handle the bottom left to top right
	x_cord = q[0]
	y_cord = q[1]

	while x_cord < n-1 and y_cord > 0:
		x_cord += 1
		y_cord -= 1

	while x_cord >= 0 and y_cord < n:
		board[x_cord][y_cord] -= 1
		x_cord -= 1
		y_cord += 1

	board[q[0]][q[1]] += 3

def backtrack(a, board, n):
	if len(a) > n:
		return 0

	count = 0

	# pdb.set_trace()
	if is_sol(a, n, board):
		count = 1
		return count

	else:
		candidates = constr_cand(board, n, a)

		for q in candidates:
			a.append(q)
			make_move(q, board, n)
			count += backtrack(a, board, n)
			unmake_move(q, board, n)
			a.remove(q)

		return count


def count_queens(n):
	# Construct the board
	board = []
	candidates = []
	a = []

	for i in range(n):
		row = []

		# Populate each row with n entries
		for j in range(n):
			row.append(0)

			# And all of the initial potential candidates
			candidates.append((i, j))

		board.append(row)

	return backtrack(a, board, n)

def main():
	# Handle user not entering enough input
	if len(argv) != 2:
		print('Error : too few arguments')
		return

	# try:
	n = int(argv[1])
	sol = count_queens(n)
	print(sol)

	# except:
	# 	print('Error : invalid iput')

if __name__ == '__main__':
	main()
