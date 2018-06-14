from sys import argv
from random import randint

def count_inversions_helper(a, start, end):
	if start + 1 == end:
		return ([a[start]], 0)
	elif start + 2 == end:
		x = a[start]
		y = a[start+1]
		inversions = 0
		if x > y:
			inversions += 1

		return ([min(x,y), max(x,y)], inversions)

	inversions = 0
	mid = int((start+end)/2)
	left_ret = count_inversions_helper(a, start, mid)
	right_ret = count_inversions_helper(a, mid, end)

	left = left_ret[0]
	right = right_ret[0]
	inversions += left_ret[1] + right_ret[1]

	ret = []

	while left and right:
		l = left[0]
		r = right[0]

		if l < r:
			ret.append(l)
			left.pop(0)

		else:
			inversions += len(left)
			ret.append(r)
			right.pop(0)

	if left:
		ret += left
	elif right:
		ret += right

	return (ret, inversions)

def count_inversions(a):
	return count_inversions_helper(a, 0, len(a))[1]

def main():
	n = int(argv[1])
	x = []

	for i in range(n):
		x.append(randint(0, 1000))

	print(x)
	solution = count_inversions(x)
	print(solution)

if __name__ == '__main__':
	main()
