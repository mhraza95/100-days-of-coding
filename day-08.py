"""
Day 08 of 100 days coding 

problem 01: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
"""

def product_array(arg: list) -> list:

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    prod = 1

    lists = []

    for i in arg:

        prod *= i

    for i in arg:

        lists.append(int(prod*(i**-1)))

    return lists

res = product_array([1, 2, 3, 4, 5])

print(res)