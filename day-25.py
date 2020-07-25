"""
Day 25 of 100 days coding 

problem 01: Given a string of words, reverse all the words.
problem 02: Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'
"""

def reverse_words(s: str) -> str:

    n = len(s)
    words = s.split(" ")
    
    rev_words = []

    for i in range(len(words)-1, 1, -1):

        rev_words.append(words[i])
    
    return " ".join(rev_words)

# res = reverse_words('Hi John,   are you ready to go?')
# print(res)


def compress_words(s: str) -> str:

    _hash = set()

    _dic = {}

    compress = ""

    for i in s:

        if i in _hash:

            _dic[i] += 1

        else:

            _dic[i] = 1
            _hash.add(i)

    for i in _dic:

        compress += str(i) + str(_dic[i])

    return compress



res = compress_words('AAAAAaaBBBBCCCCc')
print(res)