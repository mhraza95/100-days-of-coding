"""
Day 26 of 100 days coding 

problem 01: Implementation of Queue
"""

class Queue(object):

	def __init__(self):

		self.items = []

	def  isEmpty(self):
		
		return self.items == []

	def enqueue(self, data):

		return self.items.insert(0, data)

	def dequeue(self):

		return self.items.pop()

	def size(self):

		return len(self.items)

q = Queue()

print("Is Empty {}".format(q.isEmpty()))

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print("Size {}".format(q.size()))

