"""
Day 28 of 100 days coding 

problem 01: Implementation of Deque
"""

class Deque(object):
	"""docstring for ClassName"""
	def __init__(self):
		
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, data):
		return self.items.append(data)

	def addRear(self, data):
		return self.items.insert(0, data)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

d = Deque()

print("Is empty {}".format(d.isEmpty()))

d.addFront(1)
d.addRear(2)

d.addFront(3)
d.addFront(4)

d.addRear(5)

print(d.removeRear())
print(d.removeFront())

print(d.size())
		