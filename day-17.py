"""
Day 17 of 100 days coding 

problem 01: A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
"""

#Using dynamic programing
def min_cost_house(cm, n, k):

    # This problem was asked by Facebook.

    # A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

    # Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

    cost = [[0 for i in range(k)] for j in range(n)] #cost matrix with 0 values

    cost[0] = cm[0][:] #cost of first house

    for house in range(n): #row

        for color in range(k): #col

            previous = cost[house-1][:color] + cost[house-1][color+1:] #cost n-1 house
            cost[house][color] = cm[house][color] + min(previous) #cost of nth house

    return min(cost[-1])




cm = [ [2, 5],
       [1, 6],
       [2, 7],
       [4, 3]
    ]

res = min_cost_house(cm, 4, 2)
print("Minimum Cost to build house = {}".format(res))