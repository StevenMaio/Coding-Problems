from sys import argv

def getGraycode(n):
	if n == 1:
		return ['0', '1']
	else:
		return ['0'+x for x in getGraycode(n-1)] +\
			['1'+x for x in getGraycode(n-1)[::-1]]

def main():
	if len(argv) != 2:
		print('Error : program requires only an int argument')
		return

	try:
		n = int(argv[1])
		l = getGraycode(n)

		print(l)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()