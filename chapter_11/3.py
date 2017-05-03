# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list. Modify print_hist to
# print the keys and their values in alphabetical order.


def histogram(s):
    t = {}
    for c in s:
        t[c] = t.get(c, 0) + 1
    return t


def print_hist(h):
    for keys, value in sorted(h.items()):
        print keys, value

h = histogram('alphabetical')

print_hist(h)
