from sys import argv

def sqrt(x):
	def iter(x_n):
		return 0.5 * (x_n + x/x_n)

	eps = 0.0000001
	a = 1

	while True:
		b = iter(a)

		if abs(a - b) < eps:
			return b

		a = b

def main():
	if len(argv) != 2:
		print('Error : incorrect number of arguments')
		return

	try:
		x = float(argv[1])

		sqrt_x = sqrt(x)
		print(sqrt_x)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()
