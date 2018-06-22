from sys import argv
import pdb

def get_cand(seq, c_dict):
	if seq == []:
		return c_dict.keys()

	c = seq[len(seq) - 1]
	cand = []

	for k in c_dict.keys():
		if k != c and c_dict[k] > 0:
			cand.append(k)

	return cand

def backtrack(seq, k, n, c_dict):
	# We are done if our seq is as long as the original string
	if k == n:
		out = ''

		for c in seq:
			out += c

		print(out)
		return

	cand = get_cand(seq, c_dict)

	# iterate over every candidate
	for d in cand:

		# We're going to iterate over the number of occurences available 
		for i in range(1, c_dict[d]+1):

			# Add d to the seq i times
			for j in range(i):
				seq.append(d)

			c_dict[d] -= i
			k += i

			backtrack(seq, k, n, c_dict)

			# Reverse adding the char to the sequences
			for j in range(i):
				seq.pop(-1)

			c_dict[d] += i
			k -= i

def find_perm(s):
	c_dict = {c: s.count(c) for c in s}
	seq = []
	k = 0
	n = len(s)

	backtrack(seq, k, n, c_dict)

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')
		return

	s = argv[1]

	find_perm(s)

if __name__ == '__main__':
	main()