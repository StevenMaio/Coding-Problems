def interleave(stack):
	q = []


	if len(stack) == 0:
		return

	# First, we'll empty the stack intothe q until it's empty
	while True:
		x = stack.pop(-1)

		if len(stack) == 0:
			stack.append(x)
			break

	# Check to see if the length of 
	if len(q) == 0:
		return stack

	stack.append(q.pop(0))

	while len(q) != 0:
		z = q.pop(0)

		q.append(z)
		y = q.pop(0)

		while not y is z:
			q.append(y)

		stack.append(z)

		if len(q) == 0:
			break
		else:
			stack.apend(q.pop(0))

	return stack