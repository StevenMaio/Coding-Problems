from sys import argv
import pdb

def add(x, y):
	# pdb.set_trace()
	if y == 0:
		return x

	carry = (x & y) << 1
	x = x ^ y

	return add(x, carry)

def main():
	if len(argv) != 3:
		print('Error : program requires exactly 2 integer args')
		return

	try:
		x = int(argv[1])
		y = int(argv[2])

		sol = add(x, y)

		print(sol)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()