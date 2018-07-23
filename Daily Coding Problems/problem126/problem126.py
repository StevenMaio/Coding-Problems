from sys import argv

def rotate_array(arr, k):
	def rotate(arr):
		for i in range(1, n):
			j = (i-1)%n

			temp = arr[j]
			arr[j] = arr[i]
			arr[i] = temp

	n = len(arr)

	while k > 0:
		rotate(arr)
		k -= 1

def main():
	if len(argv) != 3:
		print('Error : not enough arguments')
		return

	try:
		k = int(argv[1])
		l = argv[2]
		l = l.split(',')
		l = list(map(lambda x: int(x), l))

		rotate_array(l, k)

		print(l)

	except:
		print('Error : invalid arguments')
		return

if __name__ == '__main__':
	main()