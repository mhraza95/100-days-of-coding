"""
Day 12 of 100 days coding 

problem 01: There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase.
"""

def fib(n: int) -> int:

    if n <= 1:

        return n

    return fib(n-1) + fib(n-2)

def countWays(s: int) -> int:

    # This problem was asked by Amazon.

    # There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
    #  write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

    return fib(s + 1)


res = countWays(5)
print(res)

