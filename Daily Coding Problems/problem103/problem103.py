from sys import argv
import pdb

start_i = None
end_i = None
length = None

def backtrack(seq, k, n, s, chars, char_occ):
	if n == k:
		s_start = min(seq)
		s_end = max(seq)
		s_length = s_end - s_start

		global start_i, end_i, length

		if not start_i:
			start_i = s_start
			end_i = s_end
			length = s_length

		elif s_length < length:
			length = s_length
			start_i = s_start
			end_i = s_end

		return

	# retrieve the candidates
	c = chars[k]
	cand = [x for x in char_occ[c]]
	k += 1

	for x in cand:
		char_occ[c].remove(x)
		seq.append(x)

		backtrack(seq, k, n, s, chars, char_occ)

		seq.remove(x)
		char_occ[c].append(x)

def find_substring(s, chars):
	# Initialize the map of all character occurences
	char_occ = {c: [] for c in s}

	# Initialize backtrack variables
	n = len(chars)
	k = 0
	seq = []

	for i in range(len(s)):
		c = s[i]
		char_occ[c].append(i)

	# pdb.set_trace()
	backtrack(seq, k, n, s, chars, char_occ)

def main():
	if len(argv) < 3:
		print('Error : not enough arguments')
		return

	s = argv[1]
	chars = argv[2:]

	find_substring(s, chars)
	sol = s[start_i: end_i + 1]

	print(sol)

if __name__ == '__main__':
	main()