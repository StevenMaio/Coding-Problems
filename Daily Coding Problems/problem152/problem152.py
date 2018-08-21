from sys import argv
from random import random

def sample(elems, probabilities):
	c = 0
	rand = random()
	n = len(elems)

	for i in range(n):
		x = elems[i]
		c += probabilities[i]

		if c > rand:
			return x

	return elems[-1]

def main():
	x = [1, 2, 3, 4]
	p = [0.1, 0.5, 0.2, 0.2]

	occurences = {
		1: 0,
		2: 0,
		3: 0,
		4: 0
	}

	for i in range(10000):
		n = sample(x, p)

		count = occurences.get(n)
		occurences[n] += 1

	print(occurences)

if __name__ == '__main__':
	main()