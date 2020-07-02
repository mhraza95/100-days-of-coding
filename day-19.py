"""
Day 19 of 100 days coding 

problem 01: Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
"""

def reconstruct_words(l: list, s: str) -> list:

    # This problem was asked by Microsoft.

    # Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

    # For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

    new_word = []
    
    word_len = [len(i) for i in l] #list of word len

    for i in range(len(s)):

        small = min(word_len) #smallest word

        large = max(word_len) #largest word

        while small <= large:

            if s[i:small+i] in l: #check sliced word available in words original list

                new_word.append(s[i:small+i]) #add that word to new word list
                break

            small += 1 #next samllest word

    return new_word

# words = ['quick', 'brown', 'the', 'fox']

# sentence = "thequickbrownfox"

words = ['bed', 'bath', 'bedbath', 'and', 'beyond']

sentence = "bedbathandbeyond"

res = reconstruct_words(words, sentence)
print(res)