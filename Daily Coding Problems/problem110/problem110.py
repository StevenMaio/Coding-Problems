from sys import argv
from graph import deserialize

def paths_to_leaves(root):
	# This function prints the elements of the sequence
	def print_seq(seq):
		out = ''

		for v in seq:
			out += '{} '.format(v.data)

		print(out)

	# Backtracking function
	def backtrack(seq):
		v = seq[-1]

		if not v.left and not v.right:
			print_seq(seq)

		else:
			cand = []

			if v.left:
				cand.append(v.left)

			if v.right:
				cand.append(v.right)

			for u in cand:
				seq.append(u)
				backtrack(seq)
				seq.remove(u)

	seq = [root]
	backtrack(seq)

def main():
	if len(argv) != 2:
		print('Error : program requires filename argument')
		return

	filename = argv[1]

	try:
		root = deserialize(filename)

		paths_to_leaves(root)

	except:
		print('Error : error parsing file')

if __name__ == '__main__':
	main()