from sys import argv

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next

	def getData(self):
		return self.data

	def print(self):
		print(self.getData())

		if self.getNext():
			self.getNext().print()

def sortLL(head):
	slowCursor = head
	fastCursor = head

	# Advance the two cursors until fast is at the tail, which is when slow is
	# at the midpoint
	while fastCursor.getNext():
		fastCursor = fastCursor.getNext()

		if not fastCursor.getNext():
			break

		fastCursor = fastCursor.getNext()
		slowCursor = slowCursor.getNext()

	if fastCursor == head:
		return head

	elif fastCursor == head.getNext():
		if head.getData() < fastCursor.getData():
			return head
		else:
			head.setNext(None)
			fastCursor.setNext(head)
			return fastCursor

	else:
		# Recursively sort the sub linked lists
		temp = slowCursor.getNext()
		slowCursor.setNext(None)

		head1 = sortLL(head)
		head2 = sortLL(temp)

		neuHead = None

		if head1.getData() < head2.getData():
			neuHead = head1
			head1 = head1.getNext()
		else:
			neuHead = head2
			head2 = head2.getNext()

		cursor = neuHead

		while head1 and head2:
			if head1.getData() < head2.getData():
				cursor.setNext(head1)
				head1 = head1.getNext()
				cursor = cursor.getNext()
			else:
				cursor.setNext(head2)
				head2 = head2.getNext()
				cursor = cursor.getNext()

		if head1:
			cursor.setNext(head1)
		elif head2:
			cursor.setNext(head2)

		return neuHead

def main():
	if len(argv) < 2:
		print('Error: not enough arguments')

	head = Node(int(argv[1]))
	cursor = head

	for x in argv[2:]:
		cursor.setNext(Node(int(x)))
		cursor = cursor.getNext()

	head = sortLL(head)
	head.print()

if __name__ == '__main__':
	main()