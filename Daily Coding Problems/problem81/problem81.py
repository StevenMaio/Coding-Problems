from sys import argv
from util import init_str_map
import pdb

def backtrack(seq, k, n, d_map, num, l):
	if k == n:
		s = ''

		for c in seq:
			s += c

		l.append(s)

		return

	# Generate candidates
	c = num[k]
	cand = [x for x in d_map[c]]
	k += 1

	for x in cand:
		seq.append(x)

		backtrack(seq, k, n, d_map, num, l)

		seq.pop()

def find_possible_comb(d_map, num):
	seq = []
	n = len(num)
	k = 0
	l = []

	backtrack(seq, k, n, d_map, num, l)

	return l


def main():
	if len(argv) != 3:
		print('Error : program requires a filename argument')
		return

	filename = argv[1]
	num = argv[2]
	
	d_map = init_str_map(filename)
	l = find_possible_comb(d_map, num)

	print(l)

if __name__ == '__main__':
	main()