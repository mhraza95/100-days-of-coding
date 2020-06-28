"""
Day 15 of 100 days coding 

problem 01: The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
"""
import random

def random_sampling(stream: list) -> str:
    
    # This problem was asked by Facebook.

    # Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

    rand_elem = None

    for i, e in enumerate(stream):

        if i == 0:

            rand_elem = e
        
        elif random.randint(1, i+1) == 1:

            rand_elem = e
    
    return rand_elem


res = random_sampling([1, 2, 3, 4])

print("Random number from {} is {}".format(res, res))