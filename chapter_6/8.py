# Write a function called gcd that takes parameters a and b and returns
# their greatest common divisor.


def gcd(a, b):
    if b == 0:
        return a
    else:
        rem = a % b
        return gcd(b, rem)


print gcd(8, 124)
