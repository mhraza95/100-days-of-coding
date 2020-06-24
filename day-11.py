"""
Day 11 of 100 days coding 

problem 01: Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
"""

def largets_sum(l: list) -> int:

    # This problem was asked by Airbnb.

    # Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

    # For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

    n = len(l)

    even_sum = 0

    odd_sum = 0

    third_sum = 0

    for i in range(0, n, 2):

        even_sum += l[i]

    for j in range(1, n, 2):

        odd_sum += l[j]

    for k in range(0, n, 3):

        third_sum += l[k]

    return max(even_sum, odd_sum, third_sum)

res = largets_sum([2, 4, 6, 2, 5])

print(res)
