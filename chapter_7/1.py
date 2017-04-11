# Rewrite the function print_n using iteration instead of recursion.


def print_n(s, n):
    while n > 0:
        print s
        n -= 1
    return

print_n('five', 5)
