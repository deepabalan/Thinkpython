# Modify reverse_lookup so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.


def reverse_lookup(d, v):
    t = []
    for key in d:
        if key not in t:
            if d[key] == v:
                t.append(key)
    return t, v

h = {'a': 8, 'b': 2, 'c': 3, 'd': 8, 'e': 8}

print reverse_lookup(h, 4)
print reverse_lookup(h, 8)
