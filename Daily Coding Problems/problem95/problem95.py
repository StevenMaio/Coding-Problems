from sys import argv
import pdb

def find_perm_helper(s, start, end):
	# pdb.set_trace()

	if start == end or start + 1 == end:
		return

	# # First, test to see if it cannot be reduced further
	# fin = True
	# for i in range(start+1, end):
	# 	if s[i-1] < s[i]:
	# 		fin = False
	# 		break

	# if fin:
	# 	return

	# First, try to find the next greater char c compared to s[end]
	min_c = None
	min_index = end
	loop = True

	for i in range(start, end)[::-1]:
		c = s[i]
		index = i

		for j in range(start, end):
			d = s[j]
			# If a min hasn't been found and s[i] and s[i] > c, set min
			if not min_c:
				if d > c:
					min_index = j
					min_c = d
					loop = False

			# Determine if s[i] > c and smaller than min
			else:
				if c < d < min_c:
					min_index = j
					min_c = d

		if not loop:
			break

	if not min_c:
		return

	# pdb.set_trace()

	# Swap s[end] with s[index]
	temp = s[index]
	s[min_index] = temp
	s[index] = min_c
	# start = min_index + 1
	end -= 1

	find_perm_helper(s, start, end)	

def find_perm(s):
	start = 0
	end = len(s)

	s_p = []

	for c in s:
		s_p.append(c)

	find_perm_helper(s_p, start, end)

	if s == s_p:
		return None

	else:
		return s_p
	# print(s_p)

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')
		return

	s = argv[1:]

	sol = find_perm(s)

	print(sol)

if __name__ == '__main__':
	main()