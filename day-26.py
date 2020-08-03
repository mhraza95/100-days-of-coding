"""
Day 26 of 100 days coding 

problem 01: Implementation of stack
"""

class Stack:

	def __init__(self):

		self.items = []

	def isEmpty(self) -> bool:

		return self.items == []

	def push(self, data: any) -> list:

		self.items.append(data)

	def pop(self) -> any:

		return self.items.pop()

	def peek(self) -> any:

		return self.items[len(self.items) - 1]

	def size(self) -> int:

		return len(self.items)

s = Stack()

#Add element to Stack
s.push(1)
s.push(2)
s.push("hello")

#size of stack
n = s.size()
print("Stack Size {}".format(n))

#delete element 
print(s.pop())

#pick top element
print(s.peek())

#check empty
print(s.isEmpty())