from sys import argv

def findClosestLargerNum(arr, index):
	k = arr[index]
	length = len(arr)

	minDis = float('inf')
	minInd = float('inf')

	for i in range(length):
		if i == index:
			continue

		n = arr[i]

		if n > k:
			d = abs(i - index)
			
			if d < minDis:
				minDis = d
				minInd = i

	if minInd < float('inf'):
		return minInd
	else:
		return None

def main():
	arr = [4, 1, 3, 5, 6]
	index = 0

	sol = findClosestLargerNum(arr, index)
	print(sol)

if __name__ == '__main__':
	main()