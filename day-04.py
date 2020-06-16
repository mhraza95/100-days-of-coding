"""
Day 04 of 100 days coding 

Problem 01: List of Prime nummbers between 1 to 10
Problem 02: List of Even numbers using list comprehension
"""

def prime_numbers():

    # List of Prime nummbers between 1 to 10

    p = []
    for i in range(2, 10):

        for j in range(2, i):

            if i%j == 0:

                break

        else:

            p.append(i)

    return p


# res = prime_numbers()

# print(res)


def even_numbers():

    # List of Even numbers using list comprehension
    
    num = [i for i in range(1, 10) if i%2 == 0]

    return  num


res = even_numbers()
print(res)