from sys import argv
from graph import DirectedGraph, parse_string

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

				if m[j][i]:
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
	nodes, edges = parse_string(argv[1:])

	graph = DirectedGraph(nodes, edges)
	sol = top_sort(graph)
	for row in graph.adjacency_matrix:
		print(row)

	print('\nTopological Ordering:\n{}'.format(sol))

if __name__ == '__main__':
	main()
