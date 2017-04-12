# estimating value of pi.

import math


print 'math.pi\t', '\t\tRamanujan pi', '\tDifference'


def val_pi():
    return 1 / math.pi

print val_pi(), '\t',


def rama_pi():
    constant = (2 * math.sqrt(2)) / 9801
    result = 0
    k = 0
    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        den = pow(math.factorial(k), 4) * pow(396, 4 * k)
        div = num / den
        result = result + constant * div
        if abs(div < 1e15):
            break
        k += 1
    return result

print '\t', rama_pi(),


def diff(f1, f2):
    return f2() - f1()

print '\t', diff(rama_pi, val_pi)
