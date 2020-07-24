"""
Day 24 of 100 days coding 

problem 01: Given an integer array, output all the unique pairs that sum up to a specific value k.
problem 02: Given an array of integers (positive and negative) find the largest continuous sum.
"""

def pair_sum(arr: list, k: int) -> list:

    if len(arr) < 2:

        return

    seen = set()
    output = set()

    for item in arr:

        temp = k - item

        if temp not in seen:

            seen.add(temp)

        else:

            output.add((min(temp, item), max(temp, item)))

    return output, len(output)


# res = pair_sum([1,3,2,2],4)
# print(res)


def find_largest_sum(arr: list) -> int:

    if len(arr) == 0:

        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:

        current_sum = max(current_sum+num, num)

        max_sum = max(current_sum, max_sum)

    return max_sum

res = find_largest_sum([1,2,-1,3,4,10,10,-10,-1])
print(res)

