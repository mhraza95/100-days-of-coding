"""
Day 29 of 100 days coding 

problem 01: Balanced Parentheses Check - Interview Problem
"""

def balance_check(s: str) -> bool:

	if len(s) % 2 != 0:

		return False

	opening = set("([{")

	matches = set([('(', ')'), ('[', ']'), ('{', '}')])

	stack = []

	for i in s:

		if i in opening:

			stack.append(i)

		else:

			if len(stack) == 0:

				return False

			last_open = stack.pop()

			if (last_open, i) not in matches:

				return False

	return len(stack) == 0

print(balance_check('[]'))
print(balance_check('[{]'))
print(balance_check('[{}]'))



