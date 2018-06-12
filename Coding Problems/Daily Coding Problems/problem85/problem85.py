from sys import argv

def foo(x, y, b):
	return x * b + (1-b) * y

def main():
	if len(argv) != 4:
		print('Must be in the format of x y z')
		return

	x = int(argv[1])
	y = int(argv[2])
	b = int(argv[3])

	solution = foo(x, y, b)
	print(solution)

if __name__ == '__main__':
	main()
