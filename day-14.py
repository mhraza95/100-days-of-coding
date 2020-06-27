"""
Day 14 of 100 days coding 

problem 01: The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
"""

# The Algorithm
# 1. Initialize circle_points, square_points and interval to 0.
# 2. Generate random point x.
# 3. Generate random point y.
# 4. Calculate d = x*x + y*y.
# 5. If d <= 1, increment circle_points.
# 6. Increment square_points.
# 7. Increment interval.
# 8. If increment < NO_OF_ITERATIONS, repeat from 2.
# 9. Calculate pi = 4*(circle_points/square_points).
# 10. Terminate.

import random

def monte_carlo_estimation_pie():

    # This problem was asked by Google.

    # The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

    INTERVAL = 1000

    circle_points = 0
    square_points = 0

    for i in range(INTERVAL**2):

        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        distance = rand_x**2 + rand_y**2

        if distance <= 1:

            circle_points += 1

        square_points += 1

    pi = 4 * (circle_points/square_points)

    return pi

res = monte_carlo_estimation_pie()
print("Final estimation of Pi = {:.3f}".format(res))