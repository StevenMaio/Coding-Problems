from sys import argv

def findDup(l):
	d = {}

	for n in l:
		if d.get(n):
			return n
		else:
			d[n] = True

def main():
	pass

if __name__ == '__main__':
	main()