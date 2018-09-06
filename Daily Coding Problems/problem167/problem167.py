from sys import argv


def findPairs(words):
	def formsPalindrome(w1, w2):
		'''
		TODO: Implement this more efficiently
		'''
		
		def helper(a, b):
			if a >= b:
				return True
			
			c1 = s[a]
			c2 = s[b]

			if c1 != c2:
				return False
			
			return helper(a+1, b-1)

		k = len(w1) + len(w2) - 1
		s = w1 + w2

		return helper(0, k)

	pairs = []
	n = len(words)

	for i in range(n):
		w1 = words[i]

		for j in range(n):
			if j == i:
				continue

			w2 = words[j]
			if formsPalindrome(w1, w2):
				pairs.append((i, j))

	return pairs

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')
		return

	words = argv[1:]

	sol = findPairs(words)
	print(sol)

if __name__ == '__main__':
	main()