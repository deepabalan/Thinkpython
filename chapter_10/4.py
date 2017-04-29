# Write a function called middle that takes a list and returns a new
# list that contains all but the first and last elements. So
# middle([1, 2, 3, 4]) should return [2, 3].


def middle(t):
    t.pop(0)
    t.pop(-1)
    return t

print middle([1, 2, 3, 4, 5, 6, 7, 8])
print middle(['a', 'l', 'm', 'i', 'g', 'h', 't', 'y'])
print middle(['d', 'e', 'e', 'p', 'a'])
