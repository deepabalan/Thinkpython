# Write a function called nested_sum that takes a nested list of
# integers and add up the elements from all of the nested lists.


def nested_sum(t):
    total = 0
    for x in t:
        if type(x) == list:
            total += nested_sum(x)
        else:
            total += x
    return total

print nested_sum([1, 2, 3, [4, 5, 10, [1]], [2, 1, 1]])
