"""
Day 06 of 100 days coding 

problem 01: Find the first reverse of string
Problem 02: Change letter in the string to next letter and convert vowel letter to uppercase
"""

def first_reverse(arg: str) -> str:

    # Find the first reverse of string
    # Examples
    # Input: "coderbyte"
    # Output: etybredoc
    # Input: "I Love Code"
    # Output: edoC evoL I

    lists = arg.split()
    l = []

    if len(lists) > 1:

        for i in range(1, len(lists)):

            l.append(lists[-i][::-1])

            if i == len(lists) - 1:

                l.append(lists[0][::-1])

    else:

        l.append(lists[0][::-1])

    s = " ".join(l)

    return s

# res = first_reverse("I Love Code")

# print(res)

def letter_changes(arg: str) -> str:

    # Change letter in the string to next letter and convert vowel letter to uppercase
    # Examples
    # Input: "hello*3"
    # Output: Ifmmp*3
    # Input: "abc def"
    # Output:  bcd Efg

    lists = arg.split()

    words = []

    for i in lists:

        letter = ""

        for j in i:
            
            if j.isalpha():

                nxt_chr = chr(ord(j) + 1)

                if nxt_chr == 'a' or nxt_chr == 'e' or nxt_chr == 'i' or nxt_chr == 'o' or nxt_chr == 'u':
                    
                    letter += nxt_chr.upper()

                else:

                    letter += nxt_chr

            else:

                letter += j

        words.append(letter)

    return " ".join(words)


res = letter_changes("hello*3")

print(res)