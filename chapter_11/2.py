# Dictionaries have a method called get that takes a key and a default
# value. If the key appears in the dictionary, get returns the
# corresponding value; otherwise it returns the default value.
# Use get to write histogram more concisely. You should be able to
# eliminate the if statement.


def histogram(s):
    t = {}
    for c in s:
        t[c] = t.get(c, 0) + 1
    return t


h = histogram('aaaambition')
print h

print h.get('a', 0)
