class PeekableInterface(object):
	def __init__(self, iterator):
		self.iterator = iterator

		if iterator.hasNext():
			self.current = iterator.next()
		else:
			self.current = None

	def peek(self):
		return self.current

	def next(self):
		next = self.current
		self.current = self.iterator.next()

		return next

	def hasNext(self):
		return self.current != None