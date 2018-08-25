from sys import argv

def findFirstOcc(s):
	d = {}

	for c in s:
		if d.get(c):
			return c
		else:
			d[c] = 1

	return None

def main():
	if len(argv) < 2:
		print('Error: not enough arguments')
		return

	s = argv[1]
	x = findFirstOcc(s)
	print(x)

if __name__ == '__main__':
	main()