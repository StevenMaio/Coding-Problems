from sys import argv

def solution(k):
	memo = {}

	# First, fill up memo with all of the squares <= k
	i = 1

	while i*i <= k:
		memo[i*i] = 1
		i +=1

	# import pdb; pdb.set_trace()
	for i in range(1, k+1):
		# Skip
		if memo.get(i) != None:
			continue

		mid = int(i/2) + 1
		minNumSquares = float('inf')

		for j in range(1, mid):
			nSquares = memo.get(j) + memo.get(i-j)

			if nSquares < minNumSquares:
				minNumSquares = nSquares

		memo[i] = minNumSquares

	return memo[k]

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')
		return

	try:
		k = int(argv[1])
		sol = solution(k)

		print(sol)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()