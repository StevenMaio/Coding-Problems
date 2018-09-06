from sys import argv

def evaluate(exp):
	stack = []

	while len(exp) != 0:
		x = exp.pop(0)
		v = None

		if x == '+':
			v = stack.pop(-1) + stack.pop(-1)
		elif x == '-':
			v = stack.pop(-1) + stack.pop(-1)
		elif x == '*':
			v = stack.pop(-1) * stack.pop(-1)
		elif x == '/':
			v = stack.pop(-2) / stack.pop(-1)

		if v != None:
			stack.append(v)
		else:
			stack.append(x)

	return stack[0]


def main():
	e = [
		15, 7, 1, 1, '+',
		'-', '/', 3, '*', 2,
		1, 1, '+', '+', '_',
	]

	sol = evaluate(e)
	print(sol)

if __name__ == '__main__':
	main()