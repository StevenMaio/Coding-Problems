from sys import argv
from copy import copy

def deep_copy(s):
	cp = []

	for x in s:
		cp.append(copy(x))

	return cp

def get_power_set(s):
	if s == []:
		return [[]]

	pwr_set = get_power_set(s[1:])

	ret = deep_copy(pwr_set)
	for x in pwr_set:
		x.append(s[0])
		ret.append(x)

	return ret

def main():
	s = argv[1:]

	pwr_set = get_power_set(s)
	print('Number of sets: {}\n{}'.format(len(pwr_set),pwr_set))

if __name__ == '__main__':
	main()
