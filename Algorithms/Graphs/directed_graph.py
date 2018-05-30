from sys import argv

class DirectedGraph():
	def __init__(self, nodes, edges):
		self.length = len(nodes)
		self.nodes = []

		# Initialize nodes
		for v in nodes:
			self.nodes.append(v)

		# Initialze the adjacency matrix
		self.adjacency_matrix = []
		for i in range(self.length):
			row = []

			for j in range(self.length):
				row.append(0)

			self.adjacency_matrix.append(row)

		# Add the edges to the matrix
		for e in edges:
			self.adjacency_matrix[e[0]][e[1]] = 1

def top_sort(d_graph):
	"""
	Returns a topological order of the directed graph given
	"""
	seq = []
	length = d_graph.length
	m = d_graph.adjacency_matrix

	while (len(seq) != length):
		no_node_added = True 
		for i in range(length):
			# Skip i if we've already chosen it
			if i in seq:
				continue

			no_incoming_edge = True 

			for j in range(length):
				if j in seq:
					continue

				if m[j][i] == 1:
					no_incoming_edge = False 
					break

			if no_incoming_edge:
				seq.append(i)
				no_node_added = False
				break

		if no_node_added:
			return None
	
	return seq

def main():
	nodes_string = argv[1].split(',')
	nodes = []

	for x in nodes_string:
		nodes.append(int(x))

	edges = []
	for arg in argv[2:]:
		arg = arg.split(',')
		edge = (int(arg[0]), int(arg[1]))

		edges.append(edge)

	graph = DirectedGraph(nodes, edges)
	sol = top_sort(graph)
	for row in graph.adjacency_matrix:
		print(row)

	print('\nTopological Ordering:\n{}'.format(sol))

if __name__ == '__main__':
	main()
