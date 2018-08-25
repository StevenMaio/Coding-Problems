from sys import argv
from heapq import heappush, heappop

'''
The runtime of this solution is dependent on the implementation of the
priority queue used.
'''

def findKClosestP(points, k, centralP):
	def distance(p1, p2):
		return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )**(1/2)

	priorityQ = []

	for p in points:
		d = distance(p, centralP)

		heappush(priorityQ, (d, p))

	k_points = []

	for i in range(k):
		t = heappop(priorityQ)

		k_points.append(t[1])

	return k_points


def main():
	points = [
		(0, 0),
		(5, 4),
		(3, 1)
	]
	centralPoint = (1, 2)
	k = 2

	sol = findKClosestP(points, k, centralPoint)
	print(sol)

if __name__ == '__main__':
	main()