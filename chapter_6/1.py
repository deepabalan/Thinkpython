# Write a compare function that returns 1 if x > y, 0 if x == y, and -1
# if x < y.


def comp_fun(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1


print comp_fun(14, 10)
print comp_fun(12, 12)
print comp_fun(1, 9)
