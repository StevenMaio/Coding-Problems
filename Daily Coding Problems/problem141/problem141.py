class ThreeStackNode:
	def __init__(self, data, index):
		self.data = None
		self.index = index
		self.next = None

	def getData(self):
		return self.data

	def setData(self, data):
		self.data = data

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next

	def getIndex(self):
		return self.index

class ThreeStack:
	def __init__(self):
		self.head = None
		self.lengths = {}

	def push(self, data, stackIndex):
		node = ThreeStackNode(data, stackIndex)
		head = self.head

		# If the stack is empty, set the head
		if not cursor:
			self.head = node
			self.lengths[stackIndex] = 1
			return

		# Set the head of the linked list to the new node
		node.setNext(head)
		self.head = node

		# Adjust the value of size accordingly
		if self.lengths.get(stackIndex):
			self.lengths[stackIndex] += 1
		else:
			self.lengths[stackIndex] = 1

	def pop(self, stackIndex):
		# Handle the case of the stack[stackIndex] being empty
		if not self.lengths.get(stackIndex):
			return None

		cursor = self.head

		while cursor.getIndex() != stackIndex:
			cursor = cursor.getNext()

		self.lengths[stackIndex] -= 1
		return cursor