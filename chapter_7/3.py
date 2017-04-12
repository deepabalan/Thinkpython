# Write a function named test_square_root that prints a table that
# shows number, square root by newton's method and square root by
# math.sqrt. Compare the two estimates.


import math


def sq_rt(a):
    return math.sqrt(a)


def newton_sqrt(a):
    x = 2.0
    epsilon = 0.00001
    while True:
        y = (x + (a / x)) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return x


def sqr_table(f1, f2):
    for i in range(1, 10):
        diff = abs(f1(i) - f2(i))
        print float(i), f1(i), '\t', f2(i), '\t', diff
    return

sqr_table(sq_rt, newton_sqrt)
