"""
Day 07 of 100 days coding 

problem 01: Count and display vowels in a string
Problem 02: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
"""


def count_vowel(arg: str) -> str:

    # Count and display vowels in a string
    # Input: "Geeks for  Geeks"
    # Output: {'a': 0, 'e': 4, 'i': 0, 'o': 1, 'u': 0}

    vow = "aeiou"

    arg = arg.casefold()

    count = {}.fromkeys(vow, 0)

    for char in arg:

        if char in  count:

            count[char] += 1

    return count

# res = count_vowel("Geeks for Geeks")
# print(res)

def number_sum(arg1: list, k: int):

    # This problem was recently asked by Google.

    # Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    # For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

    s = set()

    for i in range(len(arg1)):

        temp = k - arg1[i]

        if temp in s:

            break

        s.add(arg1[i])

    return arg1[i], temp

res = number_sum([1, 4, 45, 6, 10, -8], 14)
print(res)
        

