from sys import argv
from random import randint

def genRandomNumbers(n=10, numRange=1000):
	l = [randint(0, numRange) for i in range(n)]
	return l

def reverse(lst, i, j):
	return lst[:i] + lst[i:j+1][::-1] + lst[j+1:]

def sortList(lst):
	n = len(lst)

	for i in range(1, n):
		j = i - 1
		a = lst[i]
		b = lst[i-1]

		if a >= b:
			continue
		
		rev = False

		# Find the first element less than a, if it exists
		while j >= 0:
			b = lst[j]

			if b < a:
				lst = reverse(lst, j+1, i)
				lst = reverse(lst, j+2, i)
				rev = True
				break

			j -= 1

		if not rev:
			lst = reverse(lst, 0, i)
			lst = reverse(lst, 1, i)

	return lst

def main():
	if len(argv) < 2:
		print('Error : not enough inputs')
		return

	try:
		n = int(argv[1])

		numbers = genRandomNumbers(n)
		print(numbers)
		sortedNums = sortList(numbers)
		print(sortedNums)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()