# Use incremental development to write a function called hypotenuse
# that returns the length of the hypotenuse of a right triangle given
# the lengths of the two legs as arguments. Record each stage of the
# development process as you go.

import math


def hypotenuse(a, b):
    side = a**2 + b**2
    for i in range(2, 1000):
        if side % i == 0:
            return a, b, int(math.sqrt(side))
    return a, b        # Not right angled triangle

print hypotenuse(11, 60)
print hypotenuse(3, 4)
print hypotenuse(9, 10)
print hypotenuse(6, 8)
