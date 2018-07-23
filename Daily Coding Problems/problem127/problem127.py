from sys import argv

class NumberLL:
	'''
	This representation only applies to positive integers
	'''

	@staticmethod
	def fromInt(n):
		# If n is zero, create a 
		if 0 <= n < 10:
			return NumberLL(n)
		else:
			r = n % 10
			n //= 10

			head = NumberLL(r)
			cursor = head

			while n != 0:
				r = n % 10

				cursor.next = NumberLL(r)
				cursor = cursor.next

				n //= 10

			return head

	def __init__(self, data):
		self.data = data
		self.next = None
	
	def __str__(self):
		if not self.next:
			return str(self.data)
		else:
			return '{}{}'.format(str(self.next), self.data)			

	def clone(self):
		node = NumberLL(self.data)
		
		if self.next:
			node.next = self.next.clone()

		return node

	def __add__(self, other):
		if not other:
			return self.clone()
		else:
			s = self.data + other.data
			r = s % 10
			carry = s // 10

			node = NumberLL(r)

			if not self.next and not other.next:
				if carry:
					node.next = NumberLL.fromInt(carry)

			elif not self.next:
				node.next = other.next.clone() + NumberLL.fromInt(carry)

			elif not other.next:
				node.next = self.next.clone() + NumberLL.fromInt(carry)

			else:
				node.next = self.next + other.next + NumberLL.fromInt(carry)

			return node

	def sumDigits(self):
		s = self.data

		if self.next:
			s += self.next.sumDigits()

		return s

	def toInt(self):
		s = self.data

		if self.next:
			s += 10 * self.next.toInt()

		return s


def main():
	x = int(argv[1])
	y = int(argv[2])

	x_ll = NumberLL.fromInt(x)
	y_ll = NumberLL.fromInt(y)
	z = x_ll + y_ll

	assert(z.toInt() == x+y)
	print('{} + {} = {}'.format(x, y, z))

if __name__ == '__main__':
	main()