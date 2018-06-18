from sys import argv

directions = {
	'N' : (0, 1),
	'S' : (0, -1),
	'E' : (1, 0),
	'W' : (-1, 0),
	'NW' : (-1, 1),
	'NE' : (1, 1),
	'SE' : (1, -1),
	'SW' : (-1, -1),
}

# Return true if a is north of b
def isNorth(a, b):
	return a[1] > b[1]

def isSouth(a, b):
	return a[1] < b[1]

def isEast(a, b):
	return a[0] > b[0]

def isWest(a, b):
	return a[0] < b[0]

test_rule = {
	'N': lambda x, y: isNorth(x, y),
	'S' : lambda x, y : isSouth(x, y),
	'E' : lambda x, y: isEast(x, y),
	'W' : lambda x, y : isWest(x, y),
	'NW' : lambda x, y : isNorth(x, y) and isWest(x, y),
	'NE' : lambda x, y: isNorth(x, y) and isEast(x, y),
	'SW' : lambda x, y : isSouth(x, y) and isWest(x, y),
	'SE' : lambda x, y : isSouth(x, y) and isEast(x, y),
}

def check_rule(rules, sm):
	points = {}

	rule = rules.pop(0)

	# Initialize the origin
	origin = rule[2]
	points[origin] = (0, 0)
	points[rule[0]] = directions[rule[1]]

	# Repeat the process until the rules is empty
	while rules:
		rule = rules.pop(0)

		a = rule[0]
		b = rule[2]
		direct = rule[1]

		# If b is in the points described, then we can describe a
		if b in points.keys():
			x_cord = directions[direct][0] + points[b][0]
			y_cord = directions[direct][1] + points[b][1]

			points[a] = (x_cord, y_cord)

		# If a is in the points described, then we can describe b
		elif a in points.keys():
			x_cord = -directions[direct][0] + points[a][0]
			y_cord = -directions[direct][1] + points[a][1]

			points[b] = (x_cord, y_cord)

		# Otherwise, we don't know enough about either at the moment
		else:
			rules.push(rule)

	a = points[sm[0]]
	b = points[sm[2]]
	direc = sm[1]

	print(points)
	return test_rule[direc](a, b)

def main():
	if len(argv) != 2:
		print('Error : invalid input')
		return

	filename = argv[1]

	f = open(filename, "r")
	content = f.read()
	f.close()

	content = content.split('\n')
	rules = [x.split(' ') for x in content]

	rule_sum = rules[-1]
	rules.pop()

	sol= check_rule(rules, rule_sum)
	print(sol)

if __name__ == '__main__':
	main()