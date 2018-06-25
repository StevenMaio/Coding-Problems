from sys import argv

class BinTree():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def preorder(self):
		print(self.data)

		if self.left:
			self.left.preorder()
		if self.right:
			self.right.preorder()

	def inorder(self):
		if self.left:
			self.left.inorder()

		print(self.data)

		if self.right:
			self.right.inorder()

def des_helper(nodes, preO, inO, node, start, end):
	# Base case is when both start and end are the same
	if start == end:
		return

	index = inO.index(node)

	if index != start:
		# First, construct the left sub tree
		left = preO.pop(0)
		node.left = left

		des_helper(nodes, preO, inO, left, start, index - 1)

	if index != end:
		# Now, construct the right sub tree
		right = preO.pop(0)
		node.right = right

		des_helper(nodes, preO, inO, right, index + 1, end)

def deseriallize(filename):
	nodes = {}
	preO = []
	inO = []

	file = open(filename, "r")
	content = file.read()
	file.close()

	content = content.split('\n')
	# pdb.set_trace()

	# First, grab all the name and value pairs
	line = content[0]
	line = line.split(' ')

	for x in line:
		if x == '':
			continue

		x = x.split(',')

		key = int(x[0])
		val = int(x[1])

		node = BinTree(val)

		nodes[key] = node

	# Get the preorder seq
	line = content[1]
	line = line.split(' ')

	for x in line:
		if x == '':
			continue 

		key = int(x)
		preO.append( nodes[key] )

	# Now, get the inorder seq
	line = content[2]
	line = line.split(' ')

	for x in line:
		if x == '':
			continue

		key = int(x)
		inO.append(nodes[key])

	# Perform the recursive operation
	root = preO.pop(0)
	start = 0
	end = len(nodes) - 1

	des_helper(nodes, preO, inO, root, start, end)

	return root

def invert(root):
	temp = root.left
	root.left = root.right
	root.right = temp

	if root.left:
		invert(root.left)

	if root.right:
		invert(root.right)

def main():
	if len(argv) != 2:
		print('Error : program requires only a filename argument')
		return

	filename = argv[1]
	m = deseriallize(filename)

	invert(m)

	m.preorder()
	m.inorder()

if __name__ == '__main__':
	main()