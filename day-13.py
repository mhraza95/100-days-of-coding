"""
Day 12 of 100 days coding 

problem 01: Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
"""

def sub_str(s: str, k: int) -> list:
    
    # This problem was asked by Amazon.

    # Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

    # For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

    l = []

    # Generate all possible substrings in a string
    for i in range(len(s)-1):

        for j in range(i, len(s)-1):

            if len(s[i:j+1]) >= k:

                l.append(s[i:j+1])

    # store string as key as unqiue char count as value
    dic = {i: len(set(i)) for i in l}

    # store len string as key and string as value of dic, when len of string == k 
    dic2 = {len(i): i for i in dic if dic[i] == k}         

    
    return dic2[max(dic2)] #dic2 max index value 



res = sub_str("araaci", 2)
print(res)