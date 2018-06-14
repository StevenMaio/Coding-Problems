from sys import argv
from random import randint

def rand7():
	return randint(0, 7)

def rand5():
	x = 1

	for i in range(4):
		x += int(rand7() / 4)

	return x

def main():
	n = int(argv[1])

	for i in range(n):
		print(rand5())

if __name__ == '__main__':
	main()
