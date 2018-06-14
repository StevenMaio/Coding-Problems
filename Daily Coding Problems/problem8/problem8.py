from sys import argv

'''
def create_tree(filename):
	input_file = open(filename, "r")
	contents = input_file.read()
	input_file.close()

	contents = contents.split()
	root = Tree(int(contents[0][0])

	nodes = [root]

	for row in contents[1]:
		row = row.split(',')

		for i in range(len(row)):
			if i == '':
				continue

			value = int(row[0])
			node = Tree
'''

class Tree():
	self.data = None
	self.left = None
	self.right = None

	def __init__(self, data):
		self.data = data

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
	return count_unival_helper(root)[1]

def main():
	filename = argv[1]
	root = create_tree(filename)

	sol = count_unival_helper(root)
	print(sol)

if __name__ == '__main__':
	main()
