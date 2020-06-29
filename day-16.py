"""
Day 16 of 100 days coding 

problem 01: Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
"""


def max_value(l: list, k: int) -> list:


    # This problem was asked by Google.

    # Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

    # For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8]  

    max_list = []

    size = len(l)
    for i in range(size):
        
        max_list.append(max(l[i:k+i]))

        if i >= size-k:

            break

    return max_list

res = max_value([10, 5, 2, 7, 8, 7, 12, 13], 3)
print(res)

    
