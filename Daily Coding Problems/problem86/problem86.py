from sys import argv

def validate(expression):
	containers = ['(', ')']
	open_dict = {
		')': '(',
	}

	stack = []

	for char in expression:
		if char not in containers:
			continue

		if len(stack) == 0:
			stack.append(char)
			continue
	
		if char not in open_dict.keys():
			stack.append(char)
			continue

		top = stack.pop()
		if top != open_dict[char]:
			stack.append(top)
			stack.append(char)

	return len(stack)

def main():
	s = argv[1]
	sol = validate(s)

	print(sol)

if __name__ == '__main__':
	main()