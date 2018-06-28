from sys import argv
from graph import BinTree, deserialize

def find_deep(root, d):
	root.depth = d
	d += 1

	l = None
	r = None

	if root.left:
		l = find_deep(root.left, d)

	if root.right:
		r = find_deep(root.right, d)

	if not l and not r:
		return root

	elif not l:
		return r

	elif not r:
		return l

	else:
		m = max(l.depth, r.depth)
		if l.depth == m:
			return l
		else:
			return r

def find_deepest_node(root):
	return find_deep(root, 0)

def main():
	if len(argv) != 2:
		print('Error : program requires filename argument')
		return

	filename = argv[1]
	tree = deserialize(filename)

	n = find_deepest_node(tree)
	print(n.data)

if __name__ == '__main__':
	main()