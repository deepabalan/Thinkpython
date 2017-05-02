# Write a function called bisect that takes a sorted list and a target
# value and returns the index of the value in the list, if it's there,
# or None if it's not.


def bisect(t, v):
    s = sorted(t)
    print s
    for i in s:
        if s[i] == v:
            return i
        else:
            return None

print bisect([4, 3, 2, 1, 9, 6], 2)
# print bisect(['h', 'i', 'm', 'a', 'l', 'y', 'a'], 'h')
