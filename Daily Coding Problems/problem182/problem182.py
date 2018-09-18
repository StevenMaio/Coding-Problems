def isMinimallyConnected(root):
	q = [root]
	visited = {root: True}

	while len(q) != 0:
		x = q.pop(0)

		for u in x.neighbors:
			if visited.get(u):
				return False

			visited[u] = True
			q.append(u)

	return True