# Read the documentation of the dictionary method set default and use
# it to write a more concise version of invert_dict.


def histogram(s):
    t = {}
    for c in s:
        t[c] = t.get(c, 0) + 1
    return t

def invert_dict(d):
    inverse = {}
    for key in d:
        value = d[key]
        inverse.setdefault(value, []).append(key)
    return inverse

def proceed():
    h = histogram(raw_input('Enter a string: '))
    print invert_dict(h)
    a = int(raw_input('Do you want to continue:(1/0): '))
    if a == 1:
        proceed()
    elif a == 0:
        return

proceed()
