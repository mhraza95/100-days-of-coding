"""
Day 22 of 100 days coding 

problem 01: Check string s1 and s2 are anagrams
"""

def anagrams(s1: str, s2: str) -> bool :

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):

        return False

    count = {}

    for letter in s1:

        if letter in count:

            count[letter] += 1

        else:

            count[letter] = 1

    for letter in s2:

        if letter in s2:

            count[letter] -= 1
        
        else:

            count[letter] = 1

    for k in count:

        if count[k] != 0:

            return False

    return True


#res = anagrams('dog', 'god')
res = anagrams('clint eastwood', 'old west action')
print(res)



