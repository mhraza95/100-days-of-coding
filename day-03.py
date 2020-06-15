"""
Day 03 of 100 days coding 

Problem 01: LCM of two numbers without GCD
Problem 02: GCD of two numbers
Problem 03: LCM of two numbers using GCD
"""

def LCM(a: int, b: int):

    # LCM of two numbers without GCD

    lar = max(a, b)
    sm = min(a, b)

    i = lar

    while i:

        if i%sm == 0:

            return i

        i += lar


# print(LCM(5, 7))


def GCD(a: int, b: int):

    # GCD of two numbers

    if a == 0:

        return b

    return GCD(b%a, a)

# print(GCD(15, 20))


def LCM(a: int, b: int):

    # LCM of two numbers using GCD

    return ((a*b) / GCD(a, b))

res = LCM(15, 20)
print(res)