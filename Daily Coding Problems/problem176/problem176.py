from sys import argv

def mappingExists(s, t):
	'''
	The general idea, is that if s and t share both the same number of
	unique characters, and the occurences of characters are identical,
	then there does exist such a mapping
	'''
	s_occurences = {}
	t_occurences = {}

	for c in s:
		if s_occurences.get(c):
			s_occurences[c] += 1
		else:
			s_occurences[c] = 1

	for c in t:
		if t_occurences.get(c):
			t_occurences[c] += 1
		else:
			t_occurences[c] = 1

	occ = {}

	for x in s_occurences.values():
		if occ.get(x):
			occ[x] += 1
		else:
			occ[x] = 1

	for x in t_occurences.values():
		if occ.get(x):
			occ[x] -=1
		else:
			return False

	for x in occ.keys():
		if occ[x] != 0:
			return False

	return True

def main():
	if len(argv) < 3:
		print('Error : not enough arguments')
		return

	s = argv[1]
	t = argv[2]

	sol = mappingExists(s, t)
	print(sol)

if __name__ == '__main__':
	main()