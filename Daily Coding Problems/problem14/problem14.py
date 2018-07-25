def pi():
	def a_i(i=1):
		mesh = 1.0/i

		a = 0

		for j in range(i):
			x = j*mesh
			a += f(x)

		a *= mesh
		return 4*a

	def f(x):
		return (1 - x*x) ** (1/2)

	n = 10000

	a = a_i()
	i = 2

	while i < n:
		a = a_i(i)
		i += 1

	return a

def main():
	sol = pi()

	print(sol)

if __name__ == '__main__':
	main()