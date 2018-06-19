# I can't take credit for this
from sys import argv

def cons(a, b):
	return lambda f: f(a,b)

def car(f):
	return f(lambda a, b: a)

def cdr(f):
	return f(lambda a, b: b)

def main():
	if len(argv) != 3:
		print('Error : program requires 3 arguments')
		return

	x = argv[1]
	y = argv[2]

	print(car(cons(x, y)))
	print(cdr(cons(x, y)))
	
if __name__ == '__main__':
	main()