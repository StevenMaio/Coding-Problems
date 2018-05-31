from sys import argv

def count_appearances(n, x):
	count = 0

	for i in range(1, n+1):
		if x%i == 0:
			quot = x/i

			if quot > n:
				continue

			if i == i:
				count += 1
			else:
				count += 2

	return count

def main():
	n = int(argv[1])
	x = int(argv[2])

	solution = count_appearances(n,x)
	print(solution)

if __name__ == '__main__':
	main()
