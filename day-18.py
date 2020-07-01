"""
Day 18 of 100 days coding 

problem 01: Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
"""

def min_room(interval: list) -> int:

    # This problem was asked by Snapchat.

    # Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

    # For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

    n = len(interval)

    start = [s[0] for s in interval]

    end = [e[1] for e in interval]

    start.sort()
    end.sort()

    count = 0

    for i in range(n):

        if i == n-1:

            break

        if start[i+1] < end[i]:

            count += 1

    return count


res = min_room([(30, 75), (0, 50), (60, 150), (90, 200), (210, 250)])
print(res)