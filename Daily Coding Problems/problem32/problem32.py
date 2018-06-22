from sys import argv
import pdb

has_arbitration = False

def create_matrix(filename):
	matrix_file = open(filename, "r")
	matrix = []

	content = matrix_file.read()
	content = content.split('\n')

	for elem in content:
		elem = elem.split()
		row = []

		for x in elem:
			row.append(float(x))

		if row:
			matrix.append(row)

	# Close the file
	matrix_file.close()
	return matrix

def get_candidates(seq, n):
	if seq == []:
		return [i for i in range(n)]

	candidates = [seq[0]]
	last_n = seq[-1]

	for i in range(last_n + 1, n):
		candidates.append(i)

	return candidates

def calc_cost(seq, m):
	cost = 1.0

	for i in range(1, len(seq)):
		cost *= m[seq[i-1]][seq[i]]

	return cost

def backtrack(seq, m):
	# Determine if we have a circuit, and if it an arbitration
	if len(seq) > 1 and seq[0] == seq[-1]:
		if calc_cost(seq, m) != 1.0:
			global has_arbitration
			has_arbitration = True

		return

	# Candidates	
	n = len(m)
	cand = get_candidates(seq, n)

	# Handle the case of seq being empty
	if len(seq) == 0:
		for v in cand:
			seq.append(v)

			backtrack(seq, m)

			if has_arbitration:
				return
	# Otherwise, proceed normally
	else:
		u = seq[len(seq)-1]

		for v in cand:
			seq.append(v)

			backtrack(seq, m)

			if has_arbitration:
				return

			# Undone the move
			seq.remove(v)

def find_arbitration(m):
	seq = []
	cost = 1.0

	backtrack(seq, m)

def main():
	if len(argv) != 2:
		print('Error : program requires only filename arg')
		return

	filename = argv[1]
	m = create_matrix(filename)

	find_arbitration(m)
	print(has_arbitration)

if __name__ == '__main__':
	main()