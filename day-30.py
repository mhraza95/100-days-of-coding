"""
Day 30 of 100 days coding 

problem 01:  Implement a Queue using 2 Stacks - Interview Problem
"""

class Queue2Stacks(object):

	def __init__(self):

		self.instack = []
		self.outstack = []

	def enqueue(self, data : int) -> None:

		self.instack.append(data)

	def dequeue(self) -> int:

		if not self.outstack:

			while self.instack:

				self.outstack.append(self.instack.pop())

		return self.outstack.pop()


q2s = Queue2Stacks()

q2s.enqueue(1)
q2s.enqueue(2)
q2s.enqueue(3)

print(q2s.dequeue())