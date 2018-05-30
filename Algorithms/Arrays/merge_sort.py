from sys import argv
from random import randint

def merge_sort_helper(a, start, end):
	if start + 1 == end:
		return [a[start]]
	elif start + 2 == end:
		x = a[start]
		y = a[start+1]

		return [min(x,y), max(x,y)]

	mid = int((start+end)/2)
	left = merge_sort_helper(a, start, mid)
	right = merge_sort_helper(a, mid, end)

	ret = []

	while left and right:
		l = left[0]
		r = right[0]

		if l < r:
			ret.append(l)
			left.pop(0)

		else:
			ret.append(r)
			right.pop(0)

	if left:
		ret += left
	elif right:
		ret += right

	return ret

def merge_sort(a):
	return merge_sort_helper(a, 0, len(a))

def main():
	n = int(argv[1])
	x = []

	for i in range(n):
		x.append(randint(-1000, 1000))

	print(x)
	solution = merge_sort(x)
	print(solution)

if __name__ == '__main__':
	main()
