"""
Day 10 of 100 days coding 

problem 01: Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
"""
def decode_helper(args: str, n: int) -> int:

    # This problem was asked by Facebook.

    # Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

    # For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    
    if n == 0 or n == 1:

        return 1

    count = 0

    if args[n-1] > "0":

        count = decode_helper(args, n-1)

    if (args[n-2] == "0" or (args[n-2] == "1" and args[n-2] < "27")):

        count += decode_helper(args, n-2)

    return count

def decoder(s: str) -> int:

    return decode_helper(s, len(s))

res = decoder("111")
print(res)