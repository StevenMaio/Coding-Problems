from sys import argv

def find_maj(l):
	d = {}
	n = len(l)
	half = int(n/2)

	for i in range(n):
		x = l[i]

		if d.get(x):
			d[x] += 1
		else:
			d[x] = 1

		if d[x] >= half:
			return x

	return None

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')
		return

	l = argv[1:]
	sol = find_maj(l)

	print(sol)

if __name__ == '__main__':
	main()