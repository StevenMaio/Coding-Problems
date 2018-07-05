from sys import argv

def hop_helper(l, i, n):
	if i == n:
		return True

	k = l[i]
	ret = False

	# If the user can no longer make any more moves, then return False
	if k == 0:
		return False

	while k > 0:
		ret = ret or hop_helper(l, i+k, n)

		if ret:
			return True

		k -= 1

	return ret

def hop(l):
	n = len(l) - 1
	return hop_helper(l, 0, n)

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')
		return

	try:
		l = [int(x) for x in argv[1:]]
		sol = hop(l)

		print(sol)

	except:
		print('Error : invalid arguments')

if __name__ == '__main__':
	main()