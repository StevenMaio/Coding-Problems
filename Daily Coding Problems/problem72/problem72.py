from sys import argv
from copy import deepcopy
import pdb

# For now, we'll assume that the graph is topologicaly sorted
def max_path(nodes, edges):
	length = len(nodes)

	adj_dict = {}
	for i in range(length):
		adj_dict[i] = []

	for e in edges:
		adj_dict[e[0]].append(e[1])

	paths = [[0]]

	for i in range(length):
		for p in paths:
			if p[-1] == i and adj_dict[i]:
			
				paths.remove(p)
				
				for v in adj_dict[i]:
					new_p = deepcopy(p)
					new_p.append(v)
					paths.append(new_p)

	max_path = None
	max_value = 0

	# Find the path with max value
	for p in paths:
		vals = {}

		for x in p:
			c = nodes[x]

			if c in vals.keys():
				vals[c] += 1
			else:
				vals[c] = 1

		# Determine if this is the max value path
		if max(vals.values()) > max_value:
				max_value = max(vals.values())
				max_path = p

	print(max_path)
	print(max_value)

def main():
	nodes = argv[1]

	edges = []
	for arg in argv[2:]:
		arg = arg.split(',')
		edge = (int(arg[0]), int(arg[1]))

		edges.append(edge)

	max_path(nodes, edges)

if __name__ =='__main__':
	main()
