from sys import argv

class Node():
	def __init__(self, data):
		self.data = data
		self.neighbors = []

	def addNeighbor(self, node):
		self.neighbors.append(node)

	def getNeighbors(self):
		return self.neighbors

	def getData(self):
		return self.data

def createGraph(start, end, dictionary):
	def closeEnough(w1, w2):
		n = len(w1)
		hasDiff = False

		for i in range(n):
			c1 = w1[i]
			c2 = w2[i]

			if c1 == c2:
				continue
			else:
				if hasDiff:
					return False
				else:
					hasDiff = True

		return True

	nodesHash = {}
	startNode = Node(start)
	m = len(dictionary)

	nodesHash[start] = startNode

	for i in range(m):
		w = dictionary[i]

		if nodesHash.get(w):
			node = nodesHash[w]
		else:
			node = Node(w)
			nodesHash[w] = node

		if closeEnough(w, start):
			node.addNeighbor(startNode)
			startNode.addNeighbor(node)

		for j in range(i+1, m):
			s = dictionary[j]

			if nodesHash.get(s):
				sNode = nodesHash[s]
			else:
				sNode = Node(s)
				nodesHash[s] = sNode

			if closeEnough(s, w):
				sNode.addNeighbor(node)
				node.addNeighbor(sNode)

	return startNode

def search(start, end):
	visited = {}
	parent = {}

	q = [start]

	while len(q) != 0:
		x = q.pop(0)
		visited[x.getData()] = True

		# End if we've found the target
		if x.getData() == end:
			break

		for v in x.getNeighbors():
			if visited.get(v.getData()):
				continue

			parent[v.getData()] = x.getData()
			q.append(v)

	route = []

	if visited.get(end) == None:
		return None

	route.append(end)
	end = parent.get(end)

	while end != None:
		route.append(end)
		end = parent.get(end)

	return route[::-1]

def main():
	if len(argv) < 2:
		print('Error: not enough arguments')
		return

	try:
		filename = argv[1]
		f = open(filename, 'r')
		contents = f.read()
		f.close()

		contents = contents.split('\n')
		start = contents[0]
		end = contents[1]
		dictionary = contents[2].split(' ')

		s = createGraph(start, end, dictionary)
		r = search(s, end)
		print(r)

	except:
		print('Error: invalid input')

if __name__ == '__main__':
	main()