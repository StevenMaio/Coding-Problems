from sys import argv
from algorithm import backtrack

'''
This solution uses a template I created for backtracking. This is just the
code from the other solution changed so that it fits the template
'''

def count_queens(n):

	def generate_candidates(queens):
		board = data['board']

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

	def make_move(queens, candidate):
		board = data['board']
		n = data['n']

		queens.append(candidate)
		q = queens[-1]

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

	def unmake_move(queens, candidate):
		board = data['board']
		n = data['n']

		q = queens[-1]
		queens.remove(candidate)

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

	def check_solution(queens):
		n = data['n']

		if len(queens) == n:
			return True
		else:
			return False

	def process_solution(queens):
		data['count'] += 1
	
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

	data = {
		'n': n,
		'board': board,
		'count': 0
	}

	functions = {
		'check_solution' : check_solution,
		'process_solution' : process_solution,
		'generate_candidates' : generate_candidates,
		'do_move' : make_move,
		'undo_move' : unmake_move,
	}

	# Perform backtracking
	backtrack(a, data, functions)

	return data['count']

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
