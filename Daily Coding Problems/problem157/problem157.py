from sys import argv

def palinPerm(s):
	chars = {}

	for c in s:
		if chars.get(c):
			chars[c] += 1
		else:
			chars[c] = 1

	hasOddOcc = False

	for c,k in chars.items():
		if k % 2:
			if hasOddOcc:
				return False
			else:
				hasOddOcc = True

	return True

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')
		return

	s = argv[1]
	sol = palinPerm(s)
	print(sol)

if __name__ == '__main__':
	main()