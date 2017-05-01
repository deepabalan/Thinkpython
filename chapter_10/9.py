# Write a function called remove_duplicates that takes a list and
# returns a new list with only the unique elements from the original.
# Hint: they don't have to be in the same order.


"""def remove_duplicates(t):
    return list(set(t))


new_list = [1, 1, 2, 3, 4, 4]
print remove_duplicates(new_list)

print new_list
"""

def remove_duplicates(t):
    new_list = []
    for i in t:
        if i not in new_list:
            new_list.append(i)
    return new_list

print remove_duplicates([1, 1, 2, 3, 4, 4])
print remove_duplicates(['s', 'q', 'r', 'q', 'a', 's'])
