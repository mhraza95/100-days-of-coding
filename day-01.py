"""
Day 01 of 100 days coding 

Problem 01: Reverse String
Problem 02: Generate all possible substrings out of a string
Problem 03: Check Generated substrings are palindrom
"""

def reverse_string(string: str):
    """
    Reverse string
    """
    s= string[::-1]

    return s

# res = reverse_string("Hello")

# print(res)

def gen_substring(string: str):
    """
    generate substrings out of a string
    """
    s = []
    for i in range(len(string)):

        for j in range(i):

            s.append(string[j:i])

    return s

# res = gen_substring("abaabbaab")

# print(res)

def palindrom():
    """
    generate substring out of a string,
    and check substrings are palindrom
    """
    pal = []

    sub_str = gen_substring("abaabbaab")

    for i in range(len(sub_str)):

        rev = reverse_string(sub_str[i])

        if rev == sub_str[i]:

            pal.append(rev)

    return pal


res = palindrom()

print(res)

