from sys import argv
from graph import deserialize

def print_by_level(root):
	q = [root]

	while len(q) != 0:
		x = q.pop(0)

		print(x.data)

		if x.left:
			q.append(x.left)

		if x.right:
			q.append(x.right)

def main():
	if len(argv) != 2:
		print('Error : program requires more arguments')
		return

	try:
		filename = argv[1]
		root = deserialize(filename)

		print_by_level(root)

	except:
		print('Error : error parsing file')

if __name__ == '__main__':
	main()