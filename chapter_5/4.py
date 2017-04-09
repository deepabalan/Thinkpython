# 1. Write a function named is_triangle that takes three integers as
# arguments, and that prints either "Yes" or "No", depending on whether
# you can or cannot form a triangle from sticks with the given lengths.
# 2. Write a function that prompts the user to input three stick
# lengths, converts them to intgers, and uses is_triangle to check
# whether sticks with the given lengths can form a triangle.


def is_triangle(a, b, c):
    if (a > (b + c) or b > (a + c) or c > (a + b)):
        print "Oooopss......No"
    elif (a == (b + c) or b == (a + c) or c == (a + b)):
        print "Yes, degenerate triangle."
    else:
        print "Yes"


def prompt_tria():
    a = int(raw_input('value of a: '))
    b = int(raw_input('value of b: '))
    c = int(raw_input('value of c: '))
    is_triangle(a, b, c)


prompt_tria()
