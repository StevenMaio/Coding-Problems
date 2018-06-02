from sys import argv

def parse_string(args):
	nodes_string = args[0].split(',')
	nodes = []

	for x in nodes_string:
		nodes.append(int(x))

	edges = []
	for arg in args[1:]:
		arg = arg.split(',')
		edge = (int(arg[0]), int(arg[1]))

		edges.append(edge)

	return (nodes, edges)

class Graph():
	def __init__(self, nodes, edges, **kwargs):
		directed = kwargs['directed']
		weights = kwargs['weights']

		self.length = len(nodes)
		self.nodes = []

		if weights:
			self.weights = {}

		# Initialize nodes
		for v in nodes:
			self.nodes.append(v)

		# Initialze the adjacency matrix
		self.adjacency_matrix = []
		for i in range(self.length):
			row = []

			for j in range(self.length):
				row.append(None)

			self.adjacency_matrix.append(row)

		# Add the edges to the matrix
		for e in edges:
			self.adjacency_matrix[e[0]][e[1]] = 1

			if not directed:
				self.adjacency_matrix[e[1]][e[0]] = 1

			if weighted:
				self.weights[e] = weights[e]

class DirectedGraph(Graph):
	def __init__(self, nodes, edges):
		Graph.__init__(self, nodes, edges)

		# Remove excess edges
		for e in edges:
			if e[0] != e[1]:
				self.adjacency_matrix[e[1]][e[0]] = None

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

	graph = Graph(nodes, edges)
	directed_graph = DirectedGraph(nodes, edges)

	# Print the directed graph
	print('Directed')
	for row in directed_graph.adjacency_matrix:
		print(row)

	print('')
	print('Undirected')
	# Print the undirected graph
	for row in graph.adjacency_matrix:
		print(row)

if __name__ == '__main__':
	main()
