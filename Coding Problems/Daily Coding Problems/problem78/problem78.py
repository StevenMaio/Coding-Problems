from sys import argv

def merge(lists):
	result = []
	not_empty = False

	# Untiil all of the lists are empty, we find whichever 
	for x in lists:
		if x:
			not_empty = True

	# Find the smallest first element and push it to result
	# repeat until all of the lists are empty
	while not_empty:
		# Reset not_empty and min_element and min_list
		not_empty = False
		min_element = None
		min_list = None

		for l in lists:
			if l:
				if min_element:
					if l[0] < min_element:
						min_element = l[0]
						min_list = l

				else:
					min_element = l[0]
					min_list = l

		result.append(min_list.pop(0))

		# Check to see if there are still empty elements
		for l in lists:
			if l:
				not_empty = True
				continue

	return result

def main():
	lists = []

	for arg in argv[1:]:
		l = []

		arg = arg.split(',')
		
		for x in arg:
			l.append(int(x))

		lists.append(l)

	for x in lists:
		x.sort()

	solution = merge(lists)
	print(solution)

if __name__ == '__main__':
	main()
