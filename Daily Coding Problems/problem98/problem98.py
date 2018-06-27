from sys import argv
from matrix import create_str_matrix

def is_adjacent(p1, p2):
	return p1 == (p2[0], p2[1] + 1) or\
			p1 == (p2[0], p2[1] - 1) or\
			p1 == (p2[0] + 1, p2[1]) or\
			p1 == (p2[0] - 1, p2[1])

def get_candidates(seq, c, char_m):
	if len(seq) == 0:
		return [x for x in char_m[c]]

	p = seq[-1]

	return [x for x in char_m[c] if is_adjacent(p, x)]

def backtrack(seq, i, s, n, char_m, board):
	if i == len(s):
		return True

	c = s[i]
	i += 1

	cand = get_candidates(seq, c, char_m)

	for x in cand:
		seq.append(x)
		char_m[c].remove(x)

		yes = backtrack(seq, i, s, n, char_m, board)

		if yes:
			return True

		seq.remove(x)
		char_m[c].append(x)

	return False

def solution(board, s):
	seq = []
	i = 0
	k = len(s)
	m = len(board)
	n = len(board[0])

	char_m = {}

	for a in range(m):
		for b in range(n):
			c = board[a][b]
			p = (a, b)

			try:
				char_m[c].append(p)

			except:
				char_m[c] = [p]

	return backtrack(seq, i, s, k, char_m, board)

def main():
	if len(argv) != 3:
		print('Error : program requires filename argument and a string')
		return

	filename = argv[1]
	s = argv[2]

	m = create_str_matrix(filename)

	sol = solution(m, s)
	print(sol)

if __name__ == '__main__':
	main()