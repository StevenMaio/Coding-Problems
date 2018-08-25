from sys import argv

def findMinDis(content, s1, s2):
	tokens = content.split(' ')
	n = len(tokens)

	s1_l = []
	s2_l = []

	for i in range(n):
		t = tokens[i]

		if t == s1:
			s1_l.append(i)
		elif t == s2:
			s2_l.append(i)

	minDis = float('inf')

	for i in s1_l:
		for j in s2_l:
			d = abs(i - j)

			if d < minDis:
				minDis = d

	return minDis - 1

def main():
	if len(argv) < 4:
		print("Error : not enough arguments")
		return

	filename = argv[1]
	s1 = argv[2]
	s2 = argv[3]

	openFile = open(filename, 'r')
	contents = openFile.read()
	openFile.close()

	sol = findMinDis(contents, s1, s2)
	print(sol)

if __name__ == '__main__':
	main()