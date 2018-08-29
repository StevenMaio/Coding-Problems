from sys import argv

def reverse(n):
	'''
	This assumes that n is a 32-bit integer
	'''
	res = 0

	for i in range(32):
		x = n&1
		res = res << 1
		res += x
		n = n >> 1

	return res

def main():
	if len(argv) < 2:
		print('Error: not enough arguments')
		return

	n = int(argv[1])
	sol = reverse(n)
	print('{}\n{}'.format(bin(n)[2:], bin(sol)[2:]))

if __name__ == '__main__':
	main()