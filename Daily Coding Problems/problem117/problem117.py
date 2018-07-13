from sys import argv
from graph import deserialize

def find_depth_sum(root):
	q = [root]
	layer = []

	min_depth_sum = root.data
	min_depth = 0
	depth = 0

	while len(q) != 0:
		x = q.pop(0)

		# Append the children to the next layer
		if x.left:
			layer.append(x.left)

		if x.right:
			layer.append(x.right)

		if len(q) == 0:
			x = sum(list(map(lambda x: x.data, layer)))

			if x < min_depth_sum:
				min_depth_sum = x
				min_depth = depth

			q = layer
			layer = []
			depth += 1

	return min_depth
			

def main():
	if len(argv) != 2:
		print('Error : program requires more arguments')
		return

	# try:
	filename = argv[1]
	root = deserialize(filename)

	sol = find_depth_sum(root)
	print(sol)

	# except:
	# 	print('Error : error parsing file')

if __name__ == '__main__':
	main()