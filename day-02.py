"""
Day 02 of 100 days coding 

Problem 01: Find the frequency of all the words in string
Problem 02: Reverse words in a given String in Python
Problem 03: Reverse middle words of a string
"""

def word_freq(string: str):
    """
    Find the frequency of all the words in string
    """
    return {key: string.count(key) for key in string.split()}

# print(word_freq("Gfg is best Gfg"))


def rev_word(string: str):
    """
    Reverse words in a given String in Python
    """
    lists = string.split()

    l = []

    for i in range(1, len(lists) + 1):

        l.append(lists[-i])

    return " ".join(l)

# res = rev_word("geeks quiz practice code")
# print(res)

def rev_middle_word(string: str):
    """
    Reverse middle words of a string
    """
    lists = string.split()

    l = []
    for i in range(len(lists)):

        if i == 0 or i == len(lists) - 1:

            l.append(lists[i])

        else:

            l.append(lists[i][::-1])

    return " ".join(l)

res = rev_middle_word("Hi how are you geeks")
print(res)

