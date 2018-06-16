from sys import argv

def div(x, y):
	if x < y:
		return 0
	else:
		return 1 + div(x - y, y)

def main():
	if len(argv) != 3:
		print('Error : incorrect number of arguments')
		return

	try:
		x = int( argv[1] )
		y = int( argv[2] )

		sol = div(x, y)
		print(sol)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()
