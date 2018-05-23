from sys import argv

def break_string(s, k):
	ret = []

	s = s.split()

	count = 0
	curr_line = ''

	while len(s) != 0:
		x = s.pop(0)
		length = len(x)

		if length > k:
			return None

		if (count + length + 1 > k):
			ret.append(curr_line)
			curr_line = x
			count = length + 1

		else:
			curr_line = '{} {}'.format(curr_line, x)
			count = count + length + 1

	if curr_line != '':
		ret.append(curr_line)

	return ret	


def main():
	if len(argv) < 3:
		print('Not enough arguments')
		return

	k = int(argv[1])
	s = argv[2]

	for arg in argv[3:]:
		s += ' {}'.format(arg)

	solution = break_string(s, k)
	print(solution)

if __name__ == '__main__':
	main()
