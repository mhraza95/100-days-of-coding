"""
Day 09 of 100 days coding 

problem 01: Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.
"""


def missing_value(arg: list) -> int:

    # This problem was asked by Stripe.

    # Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

    # For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3

    m = max(arg)

    if m < 1:

        return 1

    if m == 1:

        return 2 if arg[0] else 1

    l = [0] * m

    for i in range(len(arg)):

        if arg[i] > 0:

            if l[arg[i] - 1] != 1:

                l[arg[i] - 1] = 1

        
    for i in range(len(l)):

        if l[i] == 0:

            return i + 1
    
    return i + 2


res = missing_value([3, 4, -1, 1])
print(res)