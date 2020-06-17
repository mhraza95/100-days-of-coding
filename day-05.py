"""
Day 05 of 100 days coding 

problem 01: Remove Special Character from words of string
Problem 02: Find the longest word in string
Problem 03: Find first factorial
"""
def bad_char(arg: str) -> str:

    # Remove Special Character from words of string

    alphabet = ""

    for char in arg:

        if char.isalnum():

            alphabet += char

    return alphabet


def longest_word(arg: str) -> str :

    # Find the longest word in string

    lists = arg.split()

    dic = {bad_char(key): len(bad_char(key)) for key in lists}

    largest = max(dic, key=dic.get)
    
    return largest

# res = longest_word("fun&!! time")
# print(res)


def first_factorial(arg: int) -> int:

    # Find first factorial

    if arg == 0 or arg == 1:

        return 1

    if arg >= 1 and arg <= 18:

        res = arg * first_factorial(arg - 1)
        return res

    return

res = first_factorial(4)

print(res)