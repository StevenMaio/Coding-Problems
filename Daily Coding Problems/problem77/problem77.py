from sys import argv
import pdb

def merge_intervals(intervals):
	result = []

	intervals.sort()
	index = 0
	length = len(intervals)

	while index < length - 1:
		x = intervals[index]
		y = intervals[index+1]

		if y[0] > x[1]:
			index += 1
			continue

		z = (x[0], max(y[1], x[1]))
		intervals.pop(index)
		intervals.pop(index)

		length -= 1
		intervals.insert(index, z)

	return intervals

def main():
	intervals = []

	for arg in argv[1:]:
		arg = arg.split(',')

		interval = (int(arg[0]), int(arg[1]))
		intervals.append(interval)

	intervals.sort()
	print(intervals)
	solution = merge_intervals(intervals)
	print(solution)

if __name__ == '__main__':
	main()
