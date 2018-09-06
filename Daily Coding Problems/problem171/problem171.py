def findMaxOcc(data):
	data.sort()
	n = len(data)

	numPeople = 0
	a = 0
	b = 0

	maxPeople = 0
	maxS = 0
	maxE = 0

	for i in range(n):
		d = data[i]
		
		a = b
		b = d[0]

		if d[2] == 'enter':
			numPeople += d[1]
		else:
			numPeople -= d[1]

		if numPeople > maxPeople:
			maxPeople = numPeople
			maxS = a
			maxE = b

	return (maxS, maxE)

def main():
	dataEntries = [
		(1, 12, 'enter'),
		(2, 3, 'exit'),
		(5, 4, 'enter'),
		(7, 13, 'exit'),
		(9, 20, 'enter'),
	]

	interval = findMaxOcc(dataEntries)
	print(interval)

if __name__ == '__main__':
	main()