from sys import argv
from graph import BinTree
from graph.util import deseriallize

class BTWrapper():

	@staticmethod
	def name_nodes(nodes, root, i):
		nodes[i] = root

		if root.left:
			i = BTWrapper.name_nodes(nodes, root.left, i+1)

		if root.right:
			i = BTWrapper.name_nodes(nodes, root.right, i+1)

		return i

	def __init__(self, root):

		self.root = root

		# Initialize the node dict
		self.nodes = {}
		BTWrapper.name_nodes(self.nodes, self.root, 0)

		self.size = len(self.nodes)

def get_dist(node, s, t):
	ret = 0
	ret_b = False


	# pdb.set_trace()
	l = (None, False)
	r = (None, False)

	if node.left:
		l = get_dist(node.left, s, t)

	if node.right:
		r = get_dist(node.right, s, t)

	# Determine if a path has already been found
	if l[1]:
		return l

	if r[1]:
		return r

	if l[0] and r[0]:
		ret += l[0] + r[0] + node.data
		ret_b = True

	elif r[0]:
		ret += r[0] + node.data

	elif l[0]:
		ret += l[0] + node.data

	elif node == s or node == t:
		ret += node.data

	else:
		ret = None

	return (ret, ret_b)

def main():
	if len(argv) != 4:
		print('Error : program needs 4 arguments')

	try:
		filename = argv[1]
		s = int(argv[2])
		t = int(argv[3])

		if s == t:
			print('Error : must be unique nodes')
			return

		root = deseriallize(filename)
		tree = BTWrapper(root)

		s = tree.nodes[s]
		t = tree.nodes[t]

		sol = get_dist(root, s, t)[0]
		print(sol)

	except:
		print('Error : invalid input')

if __name__ == '__main__':
	main()