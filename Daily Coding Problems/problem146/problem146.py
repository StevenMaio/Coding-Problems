from sys import argv
from graph import deserialize

def pruneTree(root):
	if root.right != None:
		if pruneTree(root.right):
			root.right = None

	if root.left != None:
		if pruneTree(root.left):
			root.left = None

	if root.right == None and root.left == None and root.data == 0:
		return True
	else:
		return False

def main():
	if len(argv) < 2:
		print('Error: Not enough arguments')

	filename = argv[1]
	root = deserialize(filename)
	pruneTree(root)	

	# Inspect this using pdb?

if __name__ == '__main__':
	main()