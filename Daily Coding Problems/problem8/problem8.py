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

def count_unival_helper(root):
	if root == None:
		return (True, 0)

	left = count_unival_helper(root.left)
	right = count_unival_helper(root.right)

	total = left[1] + right[1]

	# If both the left and right subtrees are unival
	if left[0] and right[0]:
		if root.left and root.right:
			if root.data == root.left.data == root.right.data:
				total += 1

		elif root.left:
			if root.data == root.left.data:
				total += 1

		elif root.right:
			if root.data == root.right.data:
				total += 1

		else:
			total += 1

		return (True, total)

	return (False, total)


def count_unival(root):
	return count_unival_helper(root)

def main():
	filename = argv[1]
	root = deseriallize(filename)

	sol = count_unival_helper(root)[1]
	print(sol)

if __name__ == '__main__':
	main()
