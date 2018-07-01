from sys import argv
from graph import deserialize, serialize

def invert(root):
	temp = root.left
	root.left = root.right
	root.right = temp

	if root.left:
		invert(root.left)

	if root.right:
		invert(root.right)

def main():
	if len(argv) != 3:
		print('Error : program requires only a filename argument')
		return

	filename = argv[1]
	out = argv[2]
	m = deserialize(filename)

	invert(m)

	m.preorder()
	m.inorder()

	serialize(m, out)

if __name__ == '__main__':
	main()