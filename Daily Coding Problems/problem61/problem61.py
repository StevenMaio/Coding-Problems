from sys import argv
import time
import pdb

def naive_exp(x, y):
	product = 1
	for i in range(y):
		product *= x

	return product

def exp(x, y):
	# I'm assuming we're not dealing with negative integers
	if y == 0:
		return 1
	elif y == 1:
		return x
	
	z = exp(x, int(y/2))
	z = z**2

	if y%2 == 1:
		z *= x

	return z

def main():
	x = int(argv[1])
	y = int(argv[2])

	now = time.time()
	naiv_solution = naive_exp(x, y)
	finish_time = time.time()
	naiv_time = finish_time - now  
#	print(naiv_solution)
	print('Naive method: {}s'.format(naiv_time))

	now = time.time()
	solution = exp(x, y)
	finish_time = time.time()
	run_time = finish_time - now 
#	print(solution)
	print('Recursive method: {}s'.format(run_time))

#	print(naiv_solution == solution)

if __name__ == '__main__':
	main()
