def cons(a, b):
	return lambda f: f(a,b)

def car(pair):
	return pair[0]

def cdr(pair):
	return pair[-1]

def main():

	print((cons(1,1))(1,1))
	
if __name__ == '__name__':
	main()