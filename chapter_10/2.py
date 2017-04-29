# Use capitalize_all to write a function named capitalize_nested that
# takes a nested list of strings and returns a new nested list with all
# strings capitalized.


def capitalize_nested(t):
    res = []
    for x in t:
        if type(x) == list:
            res.append(capitalize_nested(x))
        else:
            res.append(x.capitalize())
    return res

print capitalize_nested(['a', 'b', ['c', ['e', 'f'] , 'd'], 'g', 'h'])
