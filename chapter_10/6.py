# Write a function called is_sorted that takes a list as a parameter
# and returns True if the list is sorted in ascending order and false
# otherwise. You can assume that the elements of the list can be
# compared with the relational operators <, >, etc.


def is_sorted(t):
    return t == sorted(t)

print is_sorted([1, 2, 2])
print is_sorted(['b', 'a'])
