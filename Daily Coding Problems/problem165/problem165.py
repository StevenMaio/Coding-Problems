from sys import argv

def solve(arr):
	nArr = list(map(lambda x: 0, arr))
	n = len(arr)

	for i in range(n-1)[::-1]:
		a = arr[i]

		for j in range(i, n):
			b = arr[j]

			if a > b:
				nArr[i] = 1 + nArr[j]
				break

	return nArr

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')		
		return

	try:
		arr = list(map(lambda x: int(x), argv[1:]))
		nArr = solve(arr)
		print(nArr)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()