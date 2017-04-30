# Write a function called has_duplicates that takes a list and returns
# True if there is any element that appears more than once. It should
# not modify the original list.


def has_duplicates(t):
    dup_list = []
    for i in t:
        if i not in dup_list:
            dup_list.append(i)
        else:
            return True
    return False

a = [1, 1, 3, 1, 4, 2]
b = ['a', 'b', 'a']
c = [1, 2, 3]

print has_duplicates(a)
print a
print has_duplicates(b)
print b
print has_duplicates(c)
print c
