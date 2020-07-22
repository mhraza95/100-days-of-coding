"""
Day 23 of 100 days coding 

problem 01: There are two arrays arr1 and arr2, find the missing number
"""

def findMissingNumber(arr1: list, arr2: list) -> int:

    s = set()
    
    for num in arr1:

        if num in arr2:

            s.add(num)

        else:

            return num

    return None

arr1 = [1, 2, 3, 4, 5, 6, 7]

arr2 = [7, 6, 1, 3, 2, 4]

res = findMissingNumber(arr1, arr2)

print(res)
