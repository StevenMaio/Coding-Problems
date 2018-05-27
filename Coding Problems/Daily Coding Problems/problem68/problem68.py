from sys import argv
from sets import Set
from math import fabs

def num_bishops_vuln(m, bishops):
	vul_b = []

	num_b = len(bishops)

	for i in range(num_b):
		for j in range(i+1, num_b):
			b_1 = bishops[i]
			b_2 = bishops[j]

			x = b_1[0] - b_2[0]
			y = b_1[1] - b_2[1]

			if fabs(x) == fabs(y):
				vul_b.append((i,j))

	return len(vul_b)

def main():
	m = int(argv[1])
	bishops = []

	for arg in argv[2:]:
		arg = arg.split(',')

		element = (int(arg[0]), int(arg[1]))
		bishops.append(element)

	solution =  num_bishops_vuln(m, bishops)
	print(solution)

if __name__ == '__main__':
	main()
