# Write a function called square_root that takes a as a parameter,
# chooses a reasonable value of x, and returns an estimate of the
# square root of a.


def square_root(a):
    x = 5.0
    epsilon = .0000001
    while True:
        print x
        y = (x + (a / x)) / 2
        if abs(y - x) < epsilon:
            break
        x = y

square_root(16)
