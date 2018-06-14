from sys import argv

def encode(s):
	output = ''

	i = 0
	j = 1
	count = 1

	while (j < len(s)):
		if s[i] == s[j]:
			j += 1
			count += 1
		else:
			output += str(count) + s[i]
			i = j
			j += 1
			count = 1

	output += str(count) + s[i]

	return output

def main():
	if (len(argv) != 2):
		printf("Invalid input")
		return

	s = argv[1]
	solution = encode(s)

	print('{}'.format(solution))

if __name__ == '__main__':
	main()
