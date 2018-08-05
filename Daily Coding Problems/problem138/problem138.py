from sys import argv

d = [1, 5, 10, 25]

'''
This solution only works for US denominations because they're all relatively
prime
'''
def min_change(total, d=d):
	def helper(remaining, i):
		c = d[i]

		if remaining == 0:
			return 0
		elif remaining - c >= 0:
			return 1 + helper(remaining - c, i)
		else:
			return helper(remaining, i - 1)

	return helper(total, len(d) - 1)

def main():
	# try:
	n = int(argv[1])

	min_coins = min_change(n)
	print(min_coins)

	# except:
	# 	print('Error : invalid input')

if __name__ == '__main__':
	main()