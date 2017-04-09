# Fermat's Last Theorem says that there are no positive integers a, b,
# and c such that a^n + b^n = c^n for any values of n greater than 2.
# 1. Write a function named check_fermat that takes four parameters - a,
# b, c and n - and that checks to see Fermat's theorem holds. If n is
# greater than 2 and it turns out to be true that a^n + b^n = c the
# program should print, "Holy smokes, Fermat was wrong!" Otherwise the
# program should print, "No, that doesn't work."
# 2. Write a function that prompts the user to input values for a, b, c
# and n, converts them to integers, and uses check_fermat to check
# whether they violate Fermat's theorem.


def check_fermat(a, b, c, n):
    if n > 2:
        lhs = (a**n) + (b**n)
        rhs = c**n
        if lhs == rhs:
            print "Holy smokes, Fermat was wrong!"
        else:
            print "No, that doesn't work."
    else:
        print "ERROR: n should be greater than 2"


def prompt_user():
    a = raw_input('Enter the value of a: ')
    b = raw_input('Enter the value of b: ')
    c = raw_input('Enter the value of c: ')
    n = raw_input('Enter the value of n: ')
    check_fermat(int(a), int(b), int(c), int(n))

prompt_user()
