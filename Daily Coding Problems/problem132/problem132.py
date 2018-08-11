class HCNode:
	def __init__(self, timestamp):
		self.timestamp = timestamp
		self.next = None

	def getTimestamp(self):
		return self.timestamp

	def getNext(self):
		return self.next

	def setNext(self, nextNode):
		self.next = nextNode

class HitCounter:
	def __init__(self):
		self.head = None
		self._total = 0

	def total(self):
		return self._total

	def record(self, timestamp):
		node = HCNode(timestamp)

		if not self.head:
			self.head = node
		else:
			node.setNext(self.head)
			self.head = node

		self._total += 1

	def range(self, lower, upper):
		if self.total() == 0:
			return 0

		cursor = self.head
		count = 0

		while cursor:
			if lower <= cursor.getTimestamp() <= upper:
				count += 1

		return count