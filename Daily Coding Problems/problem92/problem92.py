from sys import argv

def top_sort(m):
	n = len(m)
	seq = []
	appended = False

	while len(seq) != n:
		# Restart everything
		appended = False

		for i in range(n):
			# Skip i, if is already included
			if i in seq or appended:
				continue

			v = m[i]

			if sum(v) == 0:
				seq.append(i)
				appended = True

				# Remove traces of this node in the matrix
				for j in range(n):
					m[j][i] = 0

		if not appended:
			return None

	return seq[::-1]

def main():
	if len(argv) != 2:
		print('Error : this program requires 2 arguments')
		return

	filename = argv[1]

	f = open(filename, 'r')
	content = f.read()
	f.close()

	# Take the input and turn it into a hashmap
	edges = {}
	content = content.split('\n')

	for l in content:
		l = l.split(' ')
		v = l[0]

		edges[v] = l[1:]

	# Convert the hash map into an adjacency matrix
	nodes = edges.keys()
	m = []

	n_nodes = len(nodes)

	for i in range(n_nodes):
		row = []

		for j in range(n_nodes):
			row.append(0)

		m.append(row)

	for i in range(n_nodes):
		c_1 = nodes[i]

		for j in range(n_nodes):
			c_2 = nodes[j]

			if c_1 in edges[c_2]:
				m[i][j] = 1

	sol = top_sort(m)
	seq = []

	if not sol:
		print('null')
		return

	for i in sol:
		seq.append(nodes[i])
	print(seq)
	# print(edges)

if __name__ == '__main__':
	main()