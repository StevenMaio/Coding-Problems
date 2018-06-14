from sys import argv

def div(x, y):
	if x < y:
		return 0
	else:
		return 1 + div(x - y, y)

def main():
	x = int( argv[1] )
	y = int( argv[2] )

	sol = div(x, y)

	print(sol)

if __name__ == '__main__':
	main()
