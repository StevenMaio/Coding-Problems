def pi():
	# Calculates the next term in the sequence
	def a_i(i=1):
		mesh = 1.0/i

		a = 0

		for j in range(i):
			x = j*mesh
			a += f(x)

		a *= mesh
		return 4*a

	# The function whose intergral we're approximating
	def f(x):
		return (1 - x*x) ** (1/2)

	n = 1000000

	return a_i(n)

def main():
	sol = pi()

	print(sol)

if __name__ == '__main__':
	main()