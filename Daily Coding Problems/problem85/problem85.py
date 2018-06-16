from sys import argv

def foo(x, y, b):
	# If b == 0, then the express will evault to y, and if it is 1,
	# then the express will evaluate to x
	return x * b + (1-b) * y

def main():
	if len(argv) != 4:
		print('Error : Must be in the format of x y z')
		return

	try:
		x = int(argv[1])
		y = int(argv[2])
		b = int(argv[3])

		solution = foo(x, y, b)
		print(solution)

	except:
		print('Error : Invalid input')

if __name__ == '__main__':
	main()