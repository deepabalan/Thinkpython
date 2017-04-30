# Write a function called chop that takes a list, modifies it by
# removing the first and last elements, and returns None.


def chop(t):
    t.pop(0)
    t.pop(-1)
    return t

print chop([1, 2, 3, 4])
print chop(['a', 'b', 'c', 'd', 'e'])
